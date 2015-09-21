import nltk, time

grammar = nltk.data.load('file:mygrammar.cfg')
sentence = "The pond is a splotch of placid water amid endless ripples of grazing land here in western Wyoming".split()
times = []

print("CFG/Recursive descent parser:")

def rd_print():
  t = time.time()
  rd_parser = nltk.RecursiveDescentParser(grammar)
  for tree in rd_parser.parse(sentence):
  	print(tree)
  times.append(time.time()-t)
  times.append("for RD_print")

print("Shift reduce parser:")
def sr_print():
  # 2 means From Left
  t = time.time()
  sr_parser = nltk.ShiftReduceParser(grammar)
  for tree in sr_parser.parse(sentence):
  	print(tree)
  times.append(time.time()-t)
  times.append("for SR_print")

print("Left Corner parser:")
def lc_print():
  t = time.time()
  lc_parser = nltk.LeftCornerChartParser(grammar, trace=2)
  for tree in lc_parser.parse(sentence):
  	print(tree)
  times.append(time.time()-t)
  times.append("for LC_print")

rd_print()
sr_print()
lc_print()
print(times)


