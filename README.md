# PersonalAssistant
Voice controlled Raspberry Pi for task scheduling, reminder, Google searches, music, quotes and jokes.

Uses Google Speech Recognition, mpsyt youTube command prompt controller and Google text to speech.

# Dependencies < as on Raspbian-2015-01>
- pip (to install a few packages) :: sudo apt-get install python-pip
- PyUserInput :: https://github.com/SavinaRoja/PyUserInput/wiki/Installation
- gTTS 1.0.2 :: https://pypi.python.org/pypi/gTTS/1.0.2
- Google Speech Recognition by Uberi :: https://github.com/Uberi/speech_recognition
- PyAudio :: sudo apt-get install python-pyaudio
- 


# To-do list:
- Developing sentence processing framework to extract content from sentence
- Adding NLP for generic instruction processing
- Adding a hardware interrupt for setting various default states


# Advanced to-do list: 
- Identifing individual by voice
- Input speech preprocessing to remove noise w.r.t a particular person
