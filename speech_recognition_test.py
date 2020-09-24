#  os.startfile
import speech_recognition as sr 
import pyttsx3  
import subprocess
import os
import re
import fnmatch
import psutil
#######################################################################
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      

all_files={};
path = r'E:\shortcuts'
for root, dirs, files in os.walk(path):
    all_files[root] = files

all_files_val = list(all_files.values())
all_files_key = list(all_files.keys())

rootPath = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
pattern = '*.lnk'
other_files = [];
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
#        print( os.path.join(root, filename))
        other_files.append(os.path.join(root, filename))
        
#gl_file = glob(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs' + '\*.lnk')
#print(gl_file)

while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
            r.pause_threshold = 3
            #listens for the user's input  
            print('listening...')
            audio2 = r.listen(source2) 
            print('listening complete')
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            if (MyText[0:6] == 'jarvis' or MyText[0:6] == 'jervis'):
                if (MyText[7:11] == 'open'):
                    msg = MyText[12:].split()
                    if (len(msg) < 2):
                        for i in range(len(all_files_val)):
                            for j in all_files_val[i]:
                                if (re.search(MyText[12:], j, re.IGNORECASE) and len(MyText[12:]) != 0):
                                    file_path = all_files_key[i] + '\\' + j
                                    os.startfile(file_path)
        #                            subprocess.call([r'C:\Program Files (x86)\Notepad++\notepad++.exe'])
                                    break
                    else:
                        print('enter')
                    for i in other_files:
                        filename = i.split('\\')[-1:][0]
                        if (re.search(MyText[12:], filename, re.IGNORECASE) and len(MyText[12:]) != 0):
                            os.startfile(i)
                 
                if (MyText[7:12] == 'close'):
                    for proc in psutil.process_iter():
                        if (MyText[13:] in proc.name().lower()):
                            proc.kill()
                    
                if (MyText[7:] == 'quit'  or MyText[7:] == 'exit'):
                    SpeakText(MyText)
                    break
            
            else:
                print(MyText)
            
            print("Did you say "+MyText) 
            SpeakText(MyText) 
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 


#import speech_recognition as sr
#def callback(recognizer, audio):                          # this is called from the background thread
#    print(audio)
#    try:
#        print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
#    except LookupError:
#        print("Oops! Didn't catch that")
#r = sr.Recognizer()
#r.listen_in_background(sr.Microphone(), callback)
#
#import time
#while True: time.sleep(0.1) 



#output = os.popen('wmic process get description, processid').read() 
#
#print(output)


#import psutil
#
#for proc in psutil.process_iter():
#    
#    if ('Calculator' in proc.name()):
#        print('done')
#        proc.kill()
        
