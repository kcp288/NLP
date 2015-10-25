import os, time, hashlib

def main():
	
	#input_file = input("Enter path of file to score (in 'quotes'): ")
	# scorer(input_file)
	# Start timer
	t = time.time()

	# count docs in dir
	path, dirs, files = os.walk("./all-OANC-dir").next()
	num_docs = len(files)
	print "Total number of documents: ", num_docs


	'''
	if 'blabla' in open('example.txt').read():
	    print "true"
	'''

	test_io('./TheRepublic.txt')

	# for doc in dir
	#idf_calc('./TheRepublic.txt')

	print('done')
	print "This took: ", time.time()-t, "seconds"

def test_io(input_file):
	read_file = open(input_file, 'r')
	dict = {}

	for line in read_file:
		# Skip blank lines
		if not line.strip():
			continue 

		# If not blank
		s = line.split()
		for i in range(len(s)):
			word = s[i]
			print "Word", word
			# If word is in dictionary, increment val
			if dict.has_key(word):
				newval = dict[word] + 1
				dict[word] = newval
			# If not, add new entry
			else:
				dict[word] = 1

	print dict
	read_file.close()

#def idf_calc():
	#idf = math.log(num_docs / docs_containing_term)


main()