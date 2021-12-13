import os, sys, time

#########################################################################################
#########################################################################################

finput, foutput = sys.argv[1:]

# Section 1: Reading into memory, and possibly time-inefficient
OUT = open(foutput,'w')
with open(finput) as IN:
	lines = []
	t1 = time.time()
	for line in IN:
		if "<constraint name=" in line:
			lst = line.strip().split()
			lines.append(lst)
sortedList = sorted(lines)
old = ''
for each in sortedList:
	# Assign the values after '=' in variable name= to the variable variableContents
	# This involves replacing '"', and ')', and adding a ',' instead of '(', and then splitting at ','
	variableContents = each[1].replace('(',',').replace(")",' ').replace('name=',' ').replace('"',' ').split(',')
	# The contents of variableContents are then joined and saved as the variable 'variable'. This involves starting of with the 0th element and joining elements 1 to -1 (2nd last) between parentheses.
	variable = variableContents[0]+'\t'+'\t'.join(variableContents[1:-1])
	# 'old' carries the name of the variable from the previous line. This enables printing each row in the input file into a column in the output file.
	if variable == old:
		OUT.write('\t{0}'.format(float(each[5].replace('"',' ').replace('/',' ').replace('>',' ').split('=')[1])))
	else:
		OUT.write('\n{0}\t{1}'.format(variable, float(each[5].replace('"',' ').replace('/','').replace('>',' ').split('=')[1])))
		old = variable
t2 = time.time()
print ('This process took ', (t2-t1)/60.0 , 'mins')