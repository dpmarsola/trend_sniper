from django.shortcuts import render
from django.http import HttpResponse
from ts_app.backend import trendsniper as ts
from django.template import loader

def ts_backend(request):
    
    if request.method == 'GET':
        ticker = request.GET.get('ticker', 'ITSA4')
        timeframe = request.GET.get('timeframe', 'W1')
        initial_period = request.GET.get('initial_period', '2025-01-01')
        end_period = request.GET.get('end_period', '2025-08-01')
        options = request.GET.getlist('options')
        
        ticker_data = { "ticker": ticker, "timeframe": timeframe, "initial_period": initial_period, "end_period": end_period}
        result = ts.parse_input_from_backend_request(ticker_data, options)

        return HttpResponse(f"TrendSniper analysis completed. {ticker_data}, Options: {options}, Result: {result}")

    template = loader.get_template('index.html')
    return HttpResponse(template.render())