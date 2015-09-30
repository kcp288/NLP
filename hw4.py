import nltk, time

input_file = open('./training.pos', 'r')
output = open('./output_file.txt', 'w')


input_length = sum(1 for line in input_file if line.strip() )

rows = input_length
columns = 3
# Initialize as 0
table = [[0 for x in range(columns)] for x in range(rows)] 

'''table[0][0] = 'cat'
table[0][1] = 'VBP'
table[0][2] = 1'''

t = time.time()

input_file = open('./training.pos', 'r')

for line in input_file:
	# Skip blank lines
	if not line.strip():
		continue 

	# If not blank
	s = line.split()
	token = s[0]
	pos = s[1]

	index = 0

	for i in range(rows): 
		#for j in range(columns):
		# If found in table, increment count and break out of loop
		if (table[i][0] == token and table[i][1] == pos):
			table[i][2] = table[i][2] + 1 # add to count
			break;
	
	# If not found in table, set next index to token					
	for i in range(rows):
		if (table[i][0] == 0):
			table[i][0] = token
			table[i][1] = pos
			table[i][2] = 1
			break;


# Display top-left element.
print(table[800])


# Display entire list.
#print(table)

'''
# Loop over rows.
for row in elements:
    # Loop over columns.
    for column in row:
        print(column, end="")
    print(end="\n")

class Entry:
	
	def __init__(self, word):
		self.word = word
		self.pos = ''
		self.count = 0

	def increment(self):
		self.count = self.count+1

	def display(self):
		print self.word, self.pos, self.count

def contains(table, token, pos):
	for i in table:
		if (i.word == token and i.pos == pos):
			return table.index(i) # Index
	return -1

input_file = open('./training.pos', 'r')
output = open('./output_file.txt', 'w')


table = []
pos_prob = []

t = time.time()
for line in input_file:
	# Skip blank lines
	if not line.strip():
		continue 

	# If not blank
	s = line.split()
	token = s[0]
	pos = s[1]

	# Search to see if 
	ndx = contains(table, token, pos)

	if (ndx != -1):
		# See if POS is the same, increment count
		#if (table[ndx].pos == pos && table):
		table[ndx].increment()
			

		# If not, create a new entry, first instance of token|POS

	else:
		new_entry = Entry(token)
		new_entry.pos = pos
		new_entry.increment()
		table.append(new_entry)


'''
# table.word.sort()
# Print table
#for i in range(0, len(table)):
#	print table[i].word, table[i].pos, table[i].count
print "This took: ", time.time()-t, "seconds"

input_file.close()
output.close()

'''	
	try: 
		ndx = table.index(token) 
		# If already in table

		break

	except:
		ValueError:
			break

for line in words:
	if "AA" in line: 
		# Split items into list items
		s = line.split()

		# See if "AA" is within word
		if s.count("AA") == 0:
			continue	
		else:
			ndx = s.index("AA")
			count_aa += 1

		# Format output to contain only surrounding phones

		# If "AA" is first phone
		if ndx==1:
			# If "AA" is only phone
			if len(s) == 2: 
				trunc = s[0] + ', ' + s[ndx] + '\n'

			# Else, take AA and following phone
			else: 
				trunc = s[0] + ', ' + s[ndx] + ', ' + s[ndx+1] + '\n'
		
		# If "AA" is last phone
		elif ndx==(len(s)-1):
			trunc = s[0] + ', ' + s[ndx-1] + ', ' + s[ndx] + '\n'

		# Somewhere in the middle but way more fresher
		else :
			trunc = s[0] + ', ' + s[ndx-1] + ', ' + s[ndx] + ', ' + s[ndx+1] + '\n'

		printAA = ''.join(trunc)
		output.write(printAA),
		output_aa.write(printAA),
'''