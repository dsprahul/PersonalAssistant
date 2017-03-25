from pykeyboard import PyKeyboard 
import time
import speech_recognition as sr


k = PyKeyboard()

r = sr.Recognizer("en-IN")
m = sr.Microphone()
r.pause_threshold = 0.5

print("Starting up ..")

with m as source:
	r.adjust_for_ambient_noise(source)
	print(u"Minimum thres was set to {}".format(r.energy_threshold))
	while True:
	        audio = r.listen(source)
	        try:
		        value = r.recognize(audio)
		    	if (value == 'open command prompt'):
				k.press_key('Control_L')
				k.press_key('Alt_L')
				k.tap_key('t')
				k.release_key('Control_L')
				k.release_key('Alt_L')
			elif (value == 'go'):
				k.tap_key('Return')
			elif (value == 'music'):
				k.type_string('mpsyt')
				k.tap_key('Return')
				k.type_string('.')
				# Tell him you're ready! Put Google stt here : https://github.com/Glutanimate/simple-google-tts
				print ("What do you wanna listen?")
			elif (value == 'search in music'):
				k.type_string('.')
			else:
				k.type_string(value)
				k.tap_key('Return')
	        except LookupError:
	            print(" ... Gave up! ...")




