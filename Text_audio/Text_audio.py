from email.mime import audio
# pip install gtts
from gtts import gTTS
# pip install playsound
from playsound import playsound

audio = 'speech.mp3'
language = "en"
sp = gTTS(text= "Enter your text here", lang= language, slow= False)
sp.save(audio)
playsound(audio)
