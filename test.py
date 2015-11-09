import os, time, hashlib, math
from operator import itemgetter
from decimal import *

dict = {}
dict_closed = {}
dict_idf = {}
closed_class_stop_words = ['a','the','an','and','or','but','about','above','after','along','amid','among',\
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on',\
                           'onto','out','over','past','per','plus','since','till','to','under','until','up',\
                           'via','vs','with','that','can','cannot','could','may','might','must',\
                           'need','ought','shall','should','will','would','have','had','has','having','be',\
                           'is','am','are','was','were','being','been','get','gets','got','gotten',\
                           'getting','seem','seeming','seems','seemed',\
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my',\
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another',\
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not',\
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more',\
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite',\
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such',\
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which',\
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday',\
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever',\
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he',\
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs',\
                           'you','your','yours','me','my','mine','I','we','us','much','and/or'
                           ]

def main():
	
	# Start timer
	t = time.time()

	# clear last run
	output = open('output_idf.txt', 'w')
	output.write('')

	# count docs in dir
	path, dirs, files = os.walk("./all-OANC-dir").next()
	#path, dirs, files = os.walk("./all-OANC-test").next()
	num_docs = len(files)
	print "Total number of documents: ", num_docs

	for path, dirs, files in os.walk("./all-OANC-dir"):
	#for path, dirs, files in os.walk("./all-OANC-test"):
		for f in files:
			get_tokens2(f)

	# Remove any tokens that have less than 1 occurrence
	for k in dict.keys():
		if (dict[k] == 1): 
			del dict[k]

	for k in dict.keys():
		idf_calc(k, num_docs)


	# REG 

	sorted_idf = sorted(dict_idf.items(), key=itemgetter(1))

	output = open('output_idf.txt', 'wb')
	for i in sorted_idf:
		output.write(str(i) + '\n')

	output.close()

	# CLOSED CLASS
	dict_idf.clear()
	for k in dict_closed.keys():
		idf_calc(k, num_docs)

	sorted_idf_closed = sorted(dict_idf.items(), key=itemgetter(1))

	output_closed = open('output_idf_closed.txt', 'wb')


	for i in sorted_idf_closed:
		output_closed.write(str(i) + '\n')

	output_closed.close()
	print('done')
	print "This took: ", time.time()-t, "seconds"

def get_tokens2(input_file):
	file_path = "./all-OANC-dir/" + input_file
	read_file = open(file_path, 'r')
	#dict = {}

	for line in read_file:
		# Skip blank lines
		if not line.strip():
			continue 

		# If not blank
		s = line.split()
		for i in range(len(s)):
			word = s[i]

			if is_closed(word):
				continue

			# If word is in dictionary, increment val
			if dict.has_key(word):
				newval = dict[word] + 1
				dict[word] = newval
			# If not, add new entry
			else:
				dict[word] = 1

	read_file.close()

def is_closed(word):
	if word in closed_class_stop_words:
		if dict_closed.has_key(word):
			newval = dict_closed[word] + 1
			dict_closed[word] = newval
			# If not, add new entry
		else:
			dict_closed[word] = 1
		return True

	else:
		return False

def idf_calc(token, num_docs):
	#output = open('output_idf.txt', 'ab')

	docs_containing_term = 0

	for path, dirs, files in os.walk("./all-OANC-dir/"):
		for f in files:
			file_path = "./all-OANC-dir/" + f
			if token in open(file_path).read():
				docs_containing_term = docs_containing_term + 1

	# Calculate idf
	idf = math.log(num_docs / docs_containing_term)
	dict_idf[token] = idf

main()