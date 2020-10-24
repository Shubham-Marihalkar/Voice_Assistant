from import_libs import *
from voice_settings import *
from functionalities_function_defs import *

def process_command(query):
    if True:
            #hot word detection
            query = query.replace("mari", "")
            query = query.replace("maari", "")
            query = query.replace("hey", "")
          # Logic for executing tasks based on query
            if 'time now' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<5:
                    speak(f"Sir, the time is {strTime}")
                    speak("Sir its been long time you are working ,please have some rest")
                elif hour>=5 and hour<12:
                    speak("Good Morning!")   
                elif hour>=12 and hour<18:
                    speak("Good Afternoon!")   
                else:
                    speak("Good Evening!")  
            
            elif 'date today' in query or "today's date" in query:
                print(time.ctime())
                speak(time.ctime())

            elif 'hello there' in query:
                speak("Hello sir")

            elif "are you there" in query:
                speak("yes sir,Please tell me how may I help you")
    
            elif 'bye' in query:
                speak("Bye for now sir,hope we will meet very soon")
                #end short coversation
                return True,True

            elif'tell me' in query or 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("tell me", "")
                query = query.replace("about", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except:
                    webbrowser.open("https://google.com/search?q=%s" % query)
                    speak('Sir,the search result are')

            elif 'thanks' in query or 'thank you' in query:
                speak('you are welcome sir')

            elif 'weather' in query:
                # to search
                if 'forecast' in query or 'show' in query or "of" in query:
                    query = query.replace("show", "")
                    query=query.replace(" of ","")
                    query=query.replace(" ","")
                    city=query
                    
                    city=city.replace("weather","")
                    city=city.replace("forecast","")
                    city=city.replace("for","")
                    print(city+"'s weather is")
                    try:
                        query1='q='+city;
                        w_data=weather_data(query1);
                        print_weather(w_data, city)
                        print()
                        for url in search(query, tld="co.in", num=3, stop = 3, pause = 2):                
                            #print(url)
                            print()
                        webbrowser.open(url)
                        speak('Sir,the weather forcast is')
                    except:
                        for url in search(query, tld="co.in", num=3, stop = 3, pause = 2):
                            print()
                            #print(url)
                        webbrowser.open(url)
                        speak('Sir,the weather forcast is')





            elif 'alright' in query or 'ok' in query or 'okay' in query or  'right' in query :
                speak('Hmm')
            else:
                print("\n")
                return False,False

            return False,True
                
            

