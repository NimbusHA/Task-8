import requests
import speech_recognition as sr     
import subprocess
from gtts import gTTS

r = sr.Recognizer() 

while True:
	message = ''
	with sr.Microphone() as source: 
		r.adjust_for_ambient_noise(source, duration=1)
		print("Speak Something :")
		audio = r.listen(source)  
		try:
			message = r.recognize_google(audio) 
			print("You said : {}".format(message))
		except:
			print("Sorry could not recognize your voice")
	if len(message)==0:
		continue

	bot_message = ""
	inp = message
	res = requests.post( json={"message": inp})

	for i in res.json():
		bot_message = i['text']
		print('Bot said: ' + str(bot_message + '\n'))





