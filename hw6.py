import nltk, time, numpy


def main():
	# If entering input, use below:
	'''
	input_file = input("Enter path of file to score (in 'quotes'): ")
	scorer(input_file)
	'''

	# Start timer
	t = time.time()

	# Run hardcoded file in the HMM scorer algorithm
	scorer('./test2.txt')

	print('done')
	print "This took: ", time.time()-t, "seconds"

# Function that generates a loading bar
def loading_bar(bar):
	bar = bar + '.'
	print bar
	return bar

def scorer(toTag):
	print "Entered scorer"
	# Open file to tag and output_count file
	# Output_count contains count for each Word/POS combo
	lines = [line.rstrip('\n') for line in open('./training.pos')]

	#input_file = open('./training.pos', 'r')
	output = open('./output_count.txt', 'w')

	# Get length of input
	#input_length = sum(1 for line in input_file if line.strip())

	print "Total lines:", len(lines)
	
	''' LIKELIHOOD CALCULATION ''' 

	ct = 0
	bar = ''
	interval = len(lines)/30


	dict = {}

	for line in lines:

		# Render loading bar
		if (ct%interval == 0): 
			bar = loading_bar(bar)
			ct = ct + 1

		if not line.strip():
			continue

		s = line.split()
		
		token = s[0]
		pos = s[1]
		entry = token + ' ' + pos
		print entry

		# If word in dictionary, increment frequency
		if dict.has_key(entry):
			newval = dict[entry] + 1
			dict[entry] = newval
		else:
			dict[entry] = 1


	# Write all results to output
	for k,v in dict.items(): 
		print (k,v)
		towrite = k + ' ' +  str(v)
		output.write(towrite)

	#table = sorted(table,key=lambda l:l[0])

	'''
	input_count = open('./output_count.txt', 'r')
	output_count_length = sum(1 for line in input_count)

	output = open('./output_percentages.txt', 'w')

	# Here's where we calculate POS likelihood
	counter = 0
	ct = 0
	bar = ''
	for i in range(length):
		if (ct%interval == 0): bar = loading_bar(bar)
		++ct

		token = table[i][0]
		pos = table[i][1]
		count = table[i][2]
		
		# Avoid out of range error
		if (i < length-1):
			index = i
			indices = []
			indices.append(index) # Add index of number

			# Check if there are probabilities
			while (table[index+1][0] == token):
				count = count + table[index+1][2]
				index = index+1
				indices.append(index) # Add index of same word

			# When no more, calculate percentages
			num_same = len(indices)

			percentages = [num_same]
			for j in range(num_same-1): 
				x = float(table[indices[j]][2])
				y = float(count)
				percentage = x / y
				output_string = table[indices[j]][0] + ' ' + table[indices[j]][1] + ' ' + str(percentage)  + '\n'

				output.write(output_string)
		
		# If last element
		else:
			x = float(table[i][2])
			y = float(count)
			percentage = x / y
			output_string = table[i][0] + ' ' + table[i][1] + ' ' + str(percentage)  + '\n'
			output.write(output_string)


	read_percentages = open('./output_percentages.txt', 'r')

	# Prior probabilities
	# Table2 is used for this :)

	pos_list = [[0 for x in range(2)] for x in range(len(table2))] 
	last_index = 0

	for i in range(len(table2)):
		pos = table2[i][1]

		index = -1
		for j in range(len(pos_list)):
			if (pos == pos_list[j][0]):
				index = j

		# index = pos_list.index(pos) if pos in pos_list[i], else -1

		if (index != -1):
			pos_list[index][1] = pos_list[index][1] + 1

		else:
			pos_list[last_index][0] = pos
			pos_list[last_index][1] = 1
			last_index = last_index + 1

	del pos_list[last_index:]

	# POS with smallest probability
	if_not_in_corpus = '.'
	#pos_list[0][0]
	'''
	print "4entered loop"
	# calculate(toTag, if_not_in_corpus);
	# input_file.close()
	output.close()


def calculate(input_fl, random):
	input_file = open(input_fl, 'r')
	output_hmm = open('./output_tagged.txt', 'w')
	read_percentages = open('./output_percentages.txt', 'r')
	# table = read_percentages.read().split('\n')
	# print(table)

	
	percent_length = 0
	for line in read_percentages: 
		percent_length = percent_length + 1

	rows = percent_length
	columns = 3 

	# Initialize table as 0
	read_percentages = open('./output_percentages.txt', 'r')
	table = [[0 for x in range(columns)] for x in range(rows)]
	index = 0
	# Read all percentages into table
	interval = percent_length/30
	print "percent_lenght", percent_length, "interval", interval
	ct = 0	
	bar = ''
	for line in read_percentages:

		if (ct%interval == 0): bar = loading_bar(bar)
		++ct

		if (index == len(table)-1):
			break
		s = line.split()
		table[index][0] = s[0]
		table[index][1] = s[1]
		table[index][2] = s[2]
		index = index + 1

	ct = 0
	bar = ''
	for line in input_file:

		if (ct%interval == 0): bar = loading_bar(bar)
		++ct

		# Skip blank lines
		if not line.strip():
			continue 

		# If not blank
		s = line.split()
		token = s[0]
		
		pos = ''
		output_line = ''
		found = False
		i = 0
		while (i < len(table)):
			if (token == table[i][0]):
				found = True
				if (table[i][2] == 1.0):
					pos = table[i][1]
					output_line = s[0] + ' ' + pos + '\n'
					print_output = ''.join(output_line)
					output_hmm.write(print_output)
					break
				else:
					index_first = i
					index_last = i
					all_same = []

					while (table[index_last][0] == token):
						all_same.append(table[index_last])
						index_last = index_last + 1

					all_same = sorted(all_same,key=lambda l:l[2]) # sort by percentages
					pos = all_same[0][1]

					output_line = s[0] + ' ' + pos + '\n'
					print_output = ''.join(output_line)
					output_hmm.write(print_output)
					break
			i = i+1
		
		# Assign randomly based on earlier calculations
		if (found == False):
			pos = random
			output_line = s[0] + ' ' + pos + '\n'
			print_output = ''.join(output_line)
			output_hmm.write(print_output)

	print("Tagging output printed to: output_tagged.txt") 

	print("\n\nA bit about the tagger...this tagger uses likelihood of POS tag for individual words, along with likelihood percentages for each POS tag overall, to calculate the POS of a word. The tagger was trained on training.pos and tested with development.txt. Good luck!\n\n")
	
	#input_file.close()
	output_hmm.close()
	
main()
