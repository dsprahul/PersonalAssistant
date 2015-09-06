# Reads in a snetence string; 
# Maps it to a predefined function and supplies required parameters which are extracted from the string
# Only difference from keyword processor is these predefined functions take input parameters 

# Okay, reference tutorial for string ops in Python: http://www.tutorialspoint.com/python/python_strings.htm
#						     https://docs.python.org/3/library/stdtypes.html#textseq
#						     https://docs.python.org/3/library/text.html



value = "I have to go to gym at 5:30 p.m. remind me"

# Sentence processing starts here ...

# First check if string is full of neither numbers nor alphas alone as both 'Alarm' and 'scheduler' functions demands mix. 
if (not(value.isdigit()) and not(value.isalpha())):
	# Alright, the string is eligible for either of 'em. So, lets find for which one.
	timeval = (max(0,(value.find('a.m.')))or (max(0,value.find('p.m.'))) or (max(0,value.find('hours'))) #Keywords for time spec
	print timeval
	reminderval = (max(0,value.find('remind'))) or (max(0,value.find('notify'))) #Keywords for reminder, NLP
	alarmval = (max(0,value.find('alarm'))) or (max(0,value.find('wake'))) #Keywords for setting an alarm, NLP

	# Truth values established at this point, lets extract the parameters and map it to respective functions. 
	
	# Reminder function
	if (reminderval):
		# Reminder should be set. At what time & what should I remind you about?
		print timeval
