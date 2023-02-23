import speech_recognition as sr 
import requests
from googletrans import Translator
import googletrans
import pyttsx3 

# create a recognizer object 
r = sr.Recognizer() 
  
# obtain audio from the microphone 
with sr.Microphone() as source: 
    print("Speak:") 
    audio = r.listen(source) 
  
try:     
    # recognize Persian language using Google Speech Recognition     
    text = r.recognize_google(audio, language='fa-IR')     
    print("You said : {}".format(text)) 
  
except:     
    print("Sorry could not recognize what you said")

#----------------------------------------------------------------------------

#importing the necessary libraries

#creating an instance of the Translator class 
translator = Translator() 
  
#taking Farsi text as input from the user 
farsi_text = text
  
#translating the Farsi text to English using translate() method 
translation = translator.translate(farsi_text, dest='en') 
  
#printing the translated text in English 
print("Translated Text in English: ", translation.text)

#---------------------------------------------------------------------------

text_1 = translation.text
url = 'http://api.openai.com/v1/engines/davinci/completions'
data = {'prompt': text_1, 'max_tokens': 50}
headers = {'Authorization': 'Bearer <Your API Key>'}
response = requests.post(url, json=data, headers=headers).json()
print(response['choices'][0]['text'])

#---------------------------------------------------------------------------

# Create a translator object
translator = Translator()

# Get the English text from the user 
english_text = response['choices'][0]['text']

# Translate the text to Farsi 
farsi_text = translator.translate(english_text, dest='fa').text 
print("Translated Farsi Text: ", farsi_text) 
  
# Read the output to the user 

engine = pyttsx3.init()  # object creation 
  
""" RATE"""  # setting up new voice rate 
rate = engine.getProperty('rate')   # getting details of current speaking rate 
engine.setProperty('rate', 125)     # setting up new voice rate  

 #VOLUME   # setting up volume level  between 0 and 1  
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                                                          engine.setProperty('volume',1.0)    # setting up volume level between 0 and 1  

    #VOICE   # changing index, changes voices. o for male 

voices = engine.getProperty('voices')       #getting details of current voice 
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. o for male   

engine.say(farsi_text)                    # say method calling    

engine.runAndWait()                        # run and wait method

