import nltk, time

input_file = open('./training.pos', 'r')
output = open('./output_file.txt', 'w')

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

# Display top-left element.
del table[lastElem:]
print(table)

print "This took: ", time.time()-t, "seconds"

input_file.close()
output.close()
