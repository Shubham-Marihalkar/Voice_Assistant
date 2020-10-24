from import_libs import *

''' weather report functions'''
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	#webbrowser.open("http://api.openweathermap.org/data/2.5/weather?"+query+"&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric");
	return res.json();
def print_weather(result,city):
	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	speak("Wind speed: {} meter per second".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	speak("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
	speak("Weather: {}".format(result['weather'][0]['main']))



''' function to search file location of given file '''
def find_files(filename, search_path):
   result = []
    # Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root,""))
   return (str(result))