# Stock Trend Prediction System

A Flask-based web application for analyzing historical stock data, visualizing trends, and making informed investment decisions. The application provides an intuitive interface for stock analysis with interactive charts and technical indicators.

## Features

- Interactive web interface with modern, responsive design
- Real-time stock data analysis and visualization
- Interactive candlestick charts with technical indicators
- Multiple timeframe analysis (1 month to 5 years)
- Key statistics and performance metrics
- Pattern recognition for identifying trends
- User-friendly dashboard with stock selection
- Responsive design for all devices

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Stock-Trend-Prediction.git
cd Stock-Trend-Prediction
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your stock data is in the `stocks.csv` file with the following columns:
   - Date
   - Symbol
   - Open
   - High
   - Low
   - Close
   - Volume

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Features in Detail

### Dashboard
- Interactive stock selection dropdown
- Customizable analysis period
- Real-time chart updates
- Key statistics display

### Analysis Page
- Detailed price analysis with candlestick charts
- Technical indicators (SMA, EMA, RSI)
- Volume analysis
- Pattern recognition
- Fullscreen chart view
- Responsive design for all screen sizes

### Technical Indicators
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- Volume analysis
- Trend identification

## Project Structure

```
Stock-Trend-Prediction/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── stocks.csv            # Stock data file
├── static/              # Static files (CSS, JS)
└── templates/           # HTML templates
    ├── base.html        # Base template
    ├── index.html       # Landing page
    ├── dashboard.html   # Dashboard page
    └── analysis.html    # Analysis results page
```

## Dependencies

- Flask: Web framework
- Pandas: Data manipulation
- Plotly: Interactive visualizations
- Bootstrap: Frontend framework
- Font Awesome: Icons

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is for educational and research purposes only. The analysis and patterns identified should not be used as financial advice or for actual trading decisions. Always consult with a qualified financial advisor before making investment decisions.