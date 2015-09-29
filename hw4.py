import nltk, time

class Entry:
	
	def __init__(self, word):
		self.word = word
		self.pos = ''
		self.count = 0

	def increment(self):
		self.count = self.count+1

	def display(self):
		print self.word, self.pos, self.count

def contains(table, token):
	for i in table:
		if i.word == token:
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
	ndx = contains(table, token)

	if (ndx != -1 && table[ndx].pos == pos):
		# See if POS is the same, increment count
		#if (table[ndx].pos == pos && table):
		table[ndx].increment()
			

		# If not, create a new entry, first instance of token|POS

	else:
		new_entry = Entry(token)
		new_entry.pos = pos
		new_entry.increment()
		table.append(new_entry)



# table.word.sort()
# Print table
#for i in range(0, len(table)):
#	print table[i].word, table[i].pos, table[i].count
print "This took: ", time.time()-t

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