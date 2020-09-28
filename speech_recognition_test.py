#  os.startfile
import speech_recognition as sr 
import pyttsx3  
import subprocess
import os
import re
import fnmatch
import psutil
import sys
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
      

f_drive = r'F:'
e_drive = r'E:'

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
found=0;file=0;
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
            r.pause_threshold = 4
            #listens for the user's input  
            print('listening...')
            audio2 = r.listen(source2, phrase_time_limit=8) 
            print('listening complete')
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            
            print("Did you say "+MyText) 
            try:
                SpeakText(MyText) 
            except:
                print('error')
                print("Unexpected error:", sys.exc_info()[1])
            
            if (MyText[0:6] == 'jarvis' or MyText[0:6] == 'jervis'):
                if (MyText[7:11] == 'open'):
                    msg = MyText[12:].split()
                    if ('in' not in msg):
                        for i in range(len(all_files_val)):
                            for j in all_files_val[i]:
                                if (re.search(MyText[12:], j, re.IGNORECASE) and len(MyText[12:]) != 0):
                                    file_path = all_files_key[i] + '\\' + j
                                    os.startfile(file_path)
        #                            subprocess.call([r'C:\Program Files (x86)\Notepad++\notepad++.exe'])
                                    break
                    else:
                        file_name=''
                        dir_name = [];
                        final_path = ''
                        for kk in msg:
                            if (kk == 'in'):
                                break
                            else:
                                file_name = file_name + ' ' + kk 
                        
                        if (('file' in file_name) == True):
                            file=1
                        file_name = file_name.strip()
                        ind = msg.index('in')
                        for kk in range(ind+1, len(msg)):
                            dir_name.append(msg[kk])
                        try:
                            dir_name.remove('drive')
                        except:
                            pass
                        
                        if ('f' in dir_name):
                            final_path = f_drive
                            dir_name.remove('f')
                        elif ('e' in dir_name):
                            final_path = e_drive
                            dir_name.remove('e')
                        else:
                            final_path = f_drive
                        
                        final_path = final_path + '\\'
                        for kk in dir_name:
                            for root, dirs, files in os.walk(final_path):
                                if (kk in dirs):
                                    final_path = os.path.join(root, kk)
                                    break
                        file_name = file_name.replace('file', '').strip()
                        
                        for root, dirs, files in os.walk(final_path):
                            if (file == 0):
                                for jj in dirs:
                                    if (re.search(file_name, jj.lower(), re.IGNORECASE) and len(MyText[12:]) != 0):
                                        final_path = os.path.join(root, jj)
                                        os.startfile(final_path)
                                        found=1;
                                        break
                            else:
                                for jj in files:
                                    if (re.search(file_name, jj.lower(), re.IGNORECASE) and len(MyText[12:]) != 0):
                                        print(files)
                                        print(root)
        #                            if (file_name in dirs):
                                        final_path = os.path.join(root, jj)
                                        os.startfile(final_path)
                                        found=1;
                                        file = 0
                                        break
                            if (found == 1):
                                break
                        
#                        all_curr_dir = os.listdir(target_path)
#                        for kk in dir_name:
#                            if (kk in all_curr_dir):
#                                final_path = os.path.join(target_path, kk)
#                                all_curr_dir = os.listdir(final_path)
#                            
#                        
#                        print('t= ', target_path, file_name)
#                        file_name = file_name.strip()
                        
                        
                        
                        
#                        for root, dirs, files in os.walk(target_path):
##                            print(dirs)
#                            if ((dir_name in dirs) == True):
#                                new_path = os.path.join(root , dir_name)
#                                print(new_path)
#                                for root2, dirs2, files2 in os.walk(new_path):
#                                    for jj in files2:
#                                        if (re.search(file_name, jj, re.IGNORECASE) and len(MyText[12:]) != 0):
#                                            file_path = os.path.join(root2, jj)
#                                            print(file_path)
#                                            os.startfile(file_path)
#                                            found=1
#                                            break 
#                                    if (found==1):
#                                        break
#
#                                if (found==1):
#                                    break
                            
                    for i in other_files:
                        filename = i.split('\\')[-1:][0]
                        if (re.search(MyText[12:], filename, re.IGNORECASE) and len(MyText[12:]) != 0):
                            os.startfile(i)
                 
                if (MyText[7:12] == 'close'):
                    for proc in psutil.process_iter():
                        if (MyText[13:] in proc.name().lower()):
                            proc.kill()
                        try:
                            aa = proc.cmdline()
                            if (re.search(MyText[13:], aa[2], re.IGNORECASE) and len(MyText[12:]) != 0):
                                proc.kill()
                        except:
                            pass
                    
                if (MyText[7:] == 'quit'  or MyText[7:] == 'exit'):
                    SpeakText(MyText)
                    break
                
                if (MyText[7:] == ('are you running')):
                    SpeakText('yes sir')
                    print('yes sir')
            
            else:
                print(MyText)
            
            
#                raise
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 


#a=input('press')

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
#while True: 
#    time.sleep(10) 




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
        
