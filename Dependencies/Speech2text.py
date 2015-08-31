# Solderon.py 
# Voice controllable generic robotic arm.
# Speech Recognition by Google, Firmata protocol for Arduino, Natural Language Processing by BITSians and other awesome stuff! 


import speech_recognition as sr

r = sr.Recognizer("en-IN")
m = sr.Microphone()
r.pause_threshold = 0.5

print("Starting up ..")
with m as source:
    r.adjust_for_ambient_noise(source)
    print(u"Minimum thres was set to {}".format(r.energy_threshold))
    while True:
        print("Listening ... ")
        audio = r.listen(source)
        print("Processing ... ")
        try:
            value = r.recognize(audio)
	    print value
        except LookupError:
            print(" ... Gave up! ...")




