from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly
import plotly.graph_objects as go
import json
import ta
from plotly.subplots import make_subplots

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for flash messages

# Load the dataset
df = pd.read_csv('stocks.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

def get_stock_data(ticker, period='1y'):
    """Get stock data from local dataset"""
    try:
        # Filter data for the specific ticker
        stock_data = df[df['Name'] == ticker].copy()
        
        if stock_data.empty:
            raise ValueError(f"No data found for ticker: {ticker}")
            
        # Filter for the last year of data
        stock_data = stock_data.last(period)
        
        return stock_data
        
    except Exception as e:
        print(f"Error getting data for {ticker}: {str(e)}")
        return pd.DataFrame(columns=['open', 'high', 'low', 'close', 'volume', 'Name'])

def add_technical_indicators(df):
    """Add technical indicators to the dataframe"""
    if df.empty:
        return df
        
    try:
        # Add Moving Averages
        df['SMA_20'] = ta.trend.sma_indicator(df['close'], window=20)
        df['SMA_50'] = ta.trend.sma_indicator(df['close'], window=50)
        
        # Add RSI
        df['RSI'] = ta.momentum.rsi(df['close'], window=14)
        
        # Add MACD
        macd = ta.trend.MACD(df['close'])
        df['MACD'] = macd.macd()
        df['MACD_Signal'] = macd.macd_signal()
        
        return df
    except Exception as e:
        print(f"Error calculating indicators: {str(e)}")
        return df

def create_plot(df, ticker):
    """Create interactive plot using Plotly"""
    if df.empty:
        return json.dumps({'data': [], 'layout': {}})
        
    try:
        # Create figure with secondary y-axis
        fig = make_subplots(rows=3, cols=1, 
                           shared_xaxes=True,
                           vertical_spacing=0.05,
                           row_heights=[0.6, 0.2, 0.2])

        # Add candlestick chart
        fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['open'],
                                    high=df['high'],
                                    low=df['low'],
                                    close=df['close'],
                                    name='OHLC'),
                      row=1, col=1)

        # Add SMA lines
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'],
                                name='SMA 20',
                                line=dict(color='orange')),
                      row=1, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'],
                                name='SMA 50',
                                line=dict(color='blue')),
                      row=1, col=1)

        # Add RSI
        fig.add_trace(go.Scatter(x=df.index, y=df['RSI'],
                                name='RSI',
                                line=dict(color='purple')),
                      row=2, col=1)
        
        # Add MACD
        fig.add_trace(go.Scatter(x=df.index, y=df['MACD'],
                                name='MACD',
                                line=dict(color='blue')),
                      row=3, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=df['MACD_Signal'],
                                name='Signal Line',
                                line=dict(color='red')),
                      row=3, col=1)

        # Update layout
        fig.update_layout(
            title=f'{ticker} Stock Analysis',
            yaxis_title='Price',
            yaxis2_title='RSI',
            yaxis3_title='MACD',
            xaxis_rangeslider_visible=False,
            height=800,
            template='plotly_dark'
        )

        return fig.to_html(full_html=False)
    except Exception as e:
        print(f"Error creating plot: {str(e)}")
        return json.dumps({'data': [], 'layout': {}})

# Get unique stock names for the dropdown
stock_names = sorted(df['Name'].unique())

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    plot_div = None
    stats = None
    ticker = None
    period = None
    if request.method == 'POST':
        ticker = request.form['ticker']
        period = request.form['period']
        stock_data = df[df['Name'] == ticker].copy()
        if stock_data.empty:
            flash('No data found for the selected stock')
        else:
            stock_data = add_technical_indicators(stock_data)
            plot_div = create_plot(stock_data, ticker)
            stats = calculate_statistics(stock_data)
    return render_template('index.html', stock_names=stock_names, plot_div=plot_div, stats=stats, ticker=ticker, period=period)

@app.route('/future', methods=['GET', 'POST'])
def future_prediction():
    if request.method == 'POST':
        ticker = request.form['ticker']
        days = int(request.form['days'])
        # Placeholder: generate random future prices
        last_price = df[df['Name'] == ticker]['close'].iloc[-1]
        np.random.seed(42)
        future_prices = [last_price + np.random.randn() for _ in range(days)]
        dates = pd.date_range(start=pd.Timestamp.today(), periods=days)
        prediction = list(zip(dates.strftime('%Y-%m-%d'), future_prices))
        return render_template('future.html', stock_names=stock_names, prediction=prediction, ticker=ticker, days=days)
    return render_template('future.html', stock_names=stock_names)

def calculate_statistics(df):
    return {
        'Current Price': f"${df['close'].iloc[-1]:.2f}",
        '52 Week High': f"${df['high'].max():.2f}",
        '52 Week Low': f"${df['low'].min():.2f}",
        'Average Volume': f"{df['volume'].mean():,.0f}",
        'RSI': f"{df['RSI'].iloc[-1]:.2f}",
        'MACD': f"{df['MACD'].iloc[-1]:.2f}"
    }

if __name__ == '__main__':
    app.run(debug=True) 