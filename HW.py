# KiraPrentice-HW2.py
import nltk, re

def main():
	
	input_file = input("PHONE NUMBER: Enter input text file path (in 'quotes'): ")
	output = input("PHONE NUMBER: Enter output text file path (in 'quotes'): ")
	phone(input_file, output)
	print('done')


	input_file = input("MONEY: Enter input text file path (in 'quotes'): ")
	output = input("MONEY: Enter output text file path (in 'quotes'): ")
	money(input_file, output)
	print('done')

def phone(input_file, output):
	# Phone number regex
	pattern = re.compile(r'((\+[0-9][0-9]?[0-9]?)?(-|\s)*(\()*[2-9][0-9]{2}(\))*(-|\s)?[2-9][0-9]{2}(-|\s)?[0-9]{4})')

	input_file = open(input_file, 'r').readlines()
	output = open(output, 'w')

	for line in input_file:
		s = line.split()
		for w in s:
			match = pattern.search(w)
			if match:
				output.write(match.group(0))
				output.write('\n')

	output.close()

def money(input_file, output):
	# Money regex
	pattern = re.compile(r'(\$([0-9]+)?(\.[0-9][0-9]?)?((,[0-9][0-9][0-9])+)?(\.[0-9][0-9])?( ((hundred|thousand)|(b|m|tr)(illion)))?( dollars?)?)')

	input_file = open(input_file, 'r').readlines()
	output = open(output, 'w')

	for line in input_file:
		s = line.split()
		for w in s:
			match = pattern.search(w)
			if match:
				output.write(match.group(0))
				output.write('\n')

	output.close()

main()
