# Reads in a snetence string; 
# Maps it to a predefined function and supplies required parameters which are extracted from the string
# Only difference from keyword processor is these predefined functions take input parameters 

# Okay, reference tutorial for string ops in Python: http://www.tutorialspoint.com/python/python_strings.htm
#						     https://docs.python.org/3/library/stdtypes.html#textseq
#						     https://docs.python.org/3/library/text.html



value = "I have to go to gym at 5:30 p.m. remind me"
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
	#timeval = (max(0,(value.find('a.m.')))or (max(0,value.find('p.m.'))) or (max(0,value.find('hours'))))
	#Keywords for reminder, NLP
	for word in reminderList :
		temp = max(0,(value.find(word)))
		reminderval = reminderval or temp
	#reminderval = (max(0,value.find('remind'))) or (max(0,value.find('notify'))) 
	#Keywords for setting an alarm, NLP
	for word in alarmList :
		temp = max(0,(value.find(word)))
		alarmval = alarmval or temp
	#alarmval = (max(0,value.find('alarm'))) or (max(0,value.find('wake'))) 

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
		timeString = words[timeIndex -1]
		print timeString+' '+words[timeIndex]
				
