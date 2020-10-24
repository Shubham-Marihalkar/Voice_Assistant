#import dependancies
from import_libs import *
from command_processing import process_command
from voice_settings import *


######################################   M A I N   F U N C T I O M   ##################################

if __name__ == "__main__":
    voicegenerator()
    #greet()

    while True:
        query = takecommand().lower()
        if "hey" in query or "hay" in query or "hai" in query or "hello" in query:
            playsound.playsound('response1.mp3', True)
            time.sleep(0.02)
            #till user wants to end conversatiion
            end=False
            while not(end):
                query = takecommand().lower()
                end,exec_=process_command(query)
                if not(end) and exec_:
                    playsound.playsound('response2.mp3', True)
                    time.sleep(0.02)
        
            
                
            
       
        

        
