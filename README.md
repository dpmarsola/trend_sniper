IMPORTANT NOTE
=============================================
This application only works on Windows machines because it requires the python library "Metatrader5", and that library is available for Windows machines only.

RUNNING THE APP
=============================================
There are 2 ways of running this app:
- Via CLI command

    ```./init.sh cli```
    
    This will start the interactive screen where you can enter the arguments for the search.

- Via Web Server

    ```./init.sh server```

    This will start a web server on 127.0.0.1:8000 (default).
    To open up another port or to listen to connections from everyone, use:  ```.... server 0.0.0.0:<port>```


    Example of the http request:

    ```/trendsniper/?ticker=ITSA4&timeframe=D1&initial_period=2025-08-01&end_period=2025-08-30&options=adr&options=guppy&options=atr&options=macd&options=show-raw-data```
