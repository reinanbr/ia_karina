import speech_recognition as sr

r = sr.Recognizer()

#karina = sr.AudioFile('karina.wav')
mic = sr.Microphone()
print(sr.Microphone.list_microphone_names())
with mic as source:
	print('listenning...')
	audio = r.listen(source)
	print('listenned')
	res = r.recognize_google(audio)
	print(res)
