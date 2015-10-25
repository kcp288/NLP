import os, time, hashlib, math
from operator import itemgetter
from decimal import *

dict = {}
dict_idf = {}

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
			get_tokens(f)

	# Remove any tokens that have less than 1 occurrence
	for k in dict.keys():
		if (dict[k] == 1): 
			del dict[k]

	for k in dict.keys():
		#print "Token: ", k
		idf_calc(k, num_docs)


	sorted_idf = sorted(dict_idf.items(), key=itemgetter(1))

	output = open('output_idf.txt', 'ab')
	for i in sorted_idf:
		output.write(str(i) + '\n')

	output.close()

	print('done')
	print "This took: ", time.time()-t, "seconds"

def get_tokens(input_file):
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
			# If word is in dictionary, increment val
			if dict.has_key(word):
				newval = dict[word] + 1
				dict[word] = newval
			# If not, add new entry
			else:
				dict[word] = 1
	read_file.close()

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