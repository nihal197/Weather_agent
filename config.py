
"""Module that holds the configuration for app.py including
API keys, temperature and forecast defaults and limits

This is meant to be used with the sample weather agent for Dialogflow, located at
https://console.dialogflow.com/api-client/#/agent//prebuiltAgents/Weather

This requires setting the WWO_API_KEY constant in config.py to a string with
a valid WWO API key for retrieving weather up to 14 days in the future. Get an
WWO API key here: https://developer.worldweatheronline.com/api/
"""

WWO_API_KEY = 'bc9b8582a8eb42f185354232180107'
MAX_FORECAST_LEN = 13
_DEFAULT_TEMP_UNIT = 'F'

_TEMP_LIMITS = {
    'hot': {'C': 25, 'F': 77},
    'warm': {'C': 15, 'F': 59},
    'chilly': {'C': 15, 'F': 41},
    'cold': {'C': -5, 'F': 23}
}
