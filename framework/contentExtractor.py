# Content extractor logic from that case study. 
# This program takes an array of truthvalues of words in sentence. That will be a vector 
# of binary, vector length being length of sentence. 
# And gives out starting counter and length of longest streak of zeros in the sentence
# That's our content, a little tailoring/ sentence processing would yield us proper phrase

# Initializing length & counter of content 
contentLength = 1 
contentIndex = 0
temp = 1
# Truth Values vector of sentence
sentenceTruthValues = [1,1,0,0,1,1,1,0,0,1,0,0,0,0,1]
counter = -1
# Now lets input this into contentExtractor to get content's starting counter and length
for index in sentenceTruthValues :
	counter +=1
	if (sentenceTruthValues[counter] == 0):
	# Might be a starting point of a phrase
		counter01 = 0
		while (counter01 < (len(sentenceTruthValues) - counter)):
			# Loop runs for a maximum of (sentence-presentWord) words
			counter01 +=1
			if (sentenceTruthValues[counter+counter01] == 0):
				temp +=1 # Measuring length of string

			elif (sentenceTruthValues[counter+counter01] == 1):
				if (temp >= contentLength):
					# Check if this phrase is longest. 
					# Yes? Store the outputs
					contentLength = temp
					contentIndex = counter
					# Reset temp for next use
					temp = 1
					# Bad bit encountered, break out of while to process rest of sentence 
					# using outer 'for'. Rahul, Inefficient, it keeps converging here 
					# until it crosses that phrase length, do something to skip this sentence
					break

				# Okay, looks like this ain't the longest of contents we've seen
				# Just clean temp for next use and break out of while
				temp = 1
				break
	

			else :
				# WTF is that bit?!			
				pass
	else :
		pass
else :
	# for loop is fucked! 
	print "Uh oh!"

	

