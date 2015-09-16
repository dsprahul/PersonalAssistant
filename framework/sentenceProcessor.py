# Reads in a snetence string; 
# Maps it to a predefined function and supplies required parameters which are extracted from the string
# Only difference from keyword processor is these predefined functions take input parameters 

# Okay, reference tutorial for string ops in Python: http://www.tutorialspoint.com/python/python_strings.htm
#						     https://docs.python.org/3/library/stdtypes.html#textseq
#						     https://docs.python.org/3/library/text.html



# Alarm Class


import time
import threading
from gtts import gTTS
import subprocess

class Alarm(threading.Thread):

    def __init__(self, hours, minutes, content):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
	self.content = str(content)
        self.keep_running = True
        from gtts import gTTS
        import subprocess

    def run(self):
        try :
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
		    tts = gTTS(text=self.content,lang='en')
		    tts.save("Speak.mp3")
		    subprocess.Popen('play Speak.mp3',shell=True)
                    return
            time.sleep(5)
	except :
	    return		        
    def just_die(self):
        self.keep_running = False



def t12Tot24(timeString, timeSuffix):

	""" Converts 12h mode to 24h mode when necessary"""
	if (timeSuffix == 'hours'):
		alarm_HH = timeString[:(len(timeString)-2)]
		alarm_MM = timeString[(len(timeString)-2):(len(timeString))]
		return (alarm_HH, alarm_MM)

	elif (timeSuffix == 'a.m.'):
		tWords = timeString.split(':')
		alarm_HH = tWords[0]
		alarm_MM = tWords[1]
		return (alarm_HH, alarm_MM)
		
	elif (timeSuffix == 'p.m.'):
		tWords = timeString.split(':')
		alarm_HH = int(tWords[0]) + 12
		alarm_MM = int(tWords[1])
		return (alarm_HH, alarm_MM)




value = "I have to go to gym at 10:09 p.m. remind me"
words = value.split()

# Lists of keywords 
timeList = ['a.m.', 'p.m.', 'hours']
reminderList = ['remind', 'notify']
alarmList = ['alarm','wake']
(timeval, reminderval, alarmval) = (0,0,0)
# Sentence processing starts here ...

# First check if string is full of neither numbers nor alphas alone as both 'Alarm' and 'scheduler' functions demands mix. 
if (not(value.isdigit()) and not(value.isalpha())):
	# Alright, the string is eligible for either of 'em. So, lets find for which one.
	#Keywords for time spec
	# Rahul, implement keywords list idea. 
	for word in timeList :
		temp = max(0,(value.find(word)))
		timeval = timeval or temp
	#Keywords for reminder, NLP
	for word in reminderList :
		temp = max(0,(value.find(word)))
		reminderval = reminderval or temp
	#Keywords for setting an alarm, NLP
	for word in alarmList :
		temp = max(0,(value.find(word)))
		alarmval = alarmval or temp

	# Truth values established at this point, lets extract the parameters and map it to respective functions. 

	# Reminder function
	if (reminderval):
		# Reminder should be set. At what time & what should I remind you about?
		# Extracting time: the word right before 'a.m.' or 'p.m.' or 'hours'
		for word in timeList :
			try :
				timeIndex = words.index(word)
			except :
				pass

		# Understand OOP --> Rahul, postponed.
		# Implementing time patch.
		timeString = words[timeIndex -1]
		timeSuffix = words[timeIndex]
		(alarm_HH, alarm_MM) = t12Tot24(timeString, timeSuffix)
		print (alarm_HH, alarm_MM)

		# Extract content for alarm/Scheduler
		# Rahul, get rid off prepositions from 'content'
		content = 'No Not that!' 

		# Non blocking, independent processes. 
		alarm = Alarm(alarm_HH, alarm_MM, content)
		alarm.start()

		
		
				
