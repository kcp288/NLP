# KiraPrentice-HW2.py
import nltk, re

input_file = open('./NLP_HW1.txt', 'r')
output = open('./output_file.txt', 'w')

raw = input_file.read()
text1 = raw.split()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(text1)

print(text.concordance("adjective"))

'''
output.write(
	[w for w in text if re.search('s/(19|20)[0-9][0-9]/[&]/g', w)]) 

output.write (
	text.findall(r"<\w*> <and> <other> <\w*s>"))



// Identify dollar amounts

's/(19|20)[0-9][0-9]/[&]/g' all-OANC.txt > output_file

// Identify telephone numbers
'''

text.close()
output.close()