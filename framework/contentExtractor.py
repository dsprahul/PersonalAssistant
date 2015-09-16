# Content extractor logic from that case study. 
# This program takes an array of truthvalues of words in sentence. That will be a vector 
# of binary, vector length being length of sentence. 
# And gives out starting index and length of longest streak of zeros in the sentence
# That's our content, a little tailoring/ sentence processing would yield us proper phrase

# Initializing length of content 
contentLength = 0 

# Truth Values vector of sentence
sentenceTruthValues = [1,1,0,0,0,0,0,1,0,1,0,0,0,1,1]

# Now lets input this into contentExtractor to get content's starting index and length
for index in sentenceTruthValues :
	
	if (sentenceTruthValues[index] == 0):
	# Might be a starting point of a phrase
	index01 = index
	while (index01 < index+(len(sentenceTruthValues) - index))

