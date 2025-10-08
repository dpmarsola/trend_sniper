from django.shortcuts import render
from django.http import HttpResponse
from ts_app.backend import trendsniper as ts
from django.template import loader

def ts_backend(request):
    
    template = loader.get_template('index.html')
    
    if request.method == 'GET':
        
        ticker = request.GET.get('ticker')
        timeframe = request.GET.get('timeframe')
        initial_period = request.GET.get('initial_period')
        end_period = request.GET.get('end_period')
        options = request.GET.getlist('options')
        
        ticker_data = { "ticker": ticker, "timeframe": timeframe, "initial_period": initial_period, "end_period": end_period}
        result = ts.parse_input_from_backend_request(ticker_data, options)

        if "json" in options or "pandasdataframe" in options:
            return HttpResponse(result)
        else:
            context = {
                'mpld3_result': result
            }

            return HttpResponse(template.render(context, request))
