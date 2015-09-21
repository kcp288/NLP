# KiraPrentice-HW2.py
import nltk, re

pattern = re.compile(r'((\+[0-9][0-9]?[0-9]?)?(-|\s)*(\()*[2-9][0-9]{2}(\))*(-|\s)?[2-9][0-9]{2}(-|\s)?[0-9]{4})')

input_file = open('./example.txt', 'r').readlines()
output = open('./output_file.txt', 'w')

#text = input_file.read()
#print text

x = ''
for line in input_file:
	s = line.split()
	for w in s:
		match = pattern.search(w)
		if match:
			print(match.group(0))
			output.write(match.group(0))
			output.write('\n')
	# search
	#match = pattern.search(line)
	#if match: 
#		print(match.group(0))
	


'''

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
for w in input_file:
	if re.search()
for line in input_file:
	for w in line:
		if re.search(r'[0-9]', line)
		print 
	for match in re.finditer(pattern, line):
		print(match.groups())



raw = input_file.read()



#tokens = nltk.word_tokenize(raw2)
#text = nltk.Text(raw)

#print(text);


print("Done")
'''
#input_file.close()
output.close()