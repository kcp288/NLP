import nltk, time, numpy

input_file = open('./training.pos', 'r')
output = open('./output_count.txt', 'w')

# All lines that are not
input_length = sum(1 for line in input_file if line.strip())

rows = input_length
columns = 3 

# Initialize table as 0
table = [[0 for x in range(columns)] for x in range(rows)] 

# Start timer
t = time.time()

print "This program runs slowly with large files! Please be patient..."

input_file = open('./training.pos', 'r')

lastElem = 0

for line in input_file:
	# Skip blank lines
	if not line.strip():
		continue 

	# If not blank
	s = line.split()
	token = s[0]
	pos = s[1]

	index = 0
	execute = False

	for i in range(rows): 
		#for j in range(columns):
		# If found in table, increment count and break out of loop
		if (table[i][0] == token and table[i][1] == pos):
			table[i][2] = table[i][2] + 1 # add to count
			break
		elif (table[i][0] == 0):
			index = i
			execute = True
			break
	
	# If not found in table, set next index to token
	if (execute):
		table[index][0]	= token
		table[index][1] = pos
		table[index][2] = 1	
		lastElem = index			

# Cut off empty table and sort alphabetically
del table[lastElem:]
table = sorted(table,key=lambda l:l[0])

length = len(table)

# Write all results to output
for i in range(length):
	outputstring = table[i][0] + " " + table[i][1] + " " + str(table[i][2]) + '\n'
	output.write(outputstring)

input_count = open('./output_count.txt', 'r')
output_count_length = sum(1 for line in input_count)

print "Printed", output_count_length, "lines to output_count.txt"

output = open('./output_percentages.txt', 'w')

# Here's where we calculate POS likelihood
counter = 0

for i in range(length):
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
		for i in range(num_same):
			x = float(table[indices[i]][2])
			y = float(count)
			percentage = x / y
			output_string = table[indices[i]][0] + ' ' + table[indices[i]][1] + ' ' + str(percentage)  + '\n'
			output.write(output_string)
	
	# If last element
	else:
		x = float(table[i][2])
		y = float(count)
		percentage = x / y
		output_string = table[i][0] + ' ' + table[i][1] + ' ' + str(percentage)  + '\n'
		output.write(output_string)


read_percentages = open('./output_percentages.txt', 'r')
output_percentage_length = sum(1 for line in read_percentages)
print "Printed", output_percentage_length, "lines to output_percentages.txt"

print "This took: ", time.time()-t, "seconds"
print "Done"

input_file.close()
output.close()
