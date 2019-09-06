from datetime import date

# Path to the file that contains the values send by the sensor in this day
UNIVERSAL_SENSOR = 'data/universal/universal_data_'+date.today().strftime("%d-%m-%Y")+".txt"
UNIVERSAL_BG = "#8abbff"            # Background color for everything
UNIVERSAL_FONT = "Bahnschrift"      # Font for every button or label

OPENWEATHER_API_KEY = "7bba42c4b4362ab23bf498ea7207a210"    # API key for using OpenWeather