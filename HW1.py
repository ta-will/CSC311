#Tevin Williams

_txtfile = open("HW1.txt", "w");
myString = "CSC311 Network and Data Communication";

#def outputPart(*myList):
#	i = 5;
#	for i in range(0, len(myList), 1):
#		toTxt = str(myList[i]);
#		_txtfile.write(toTxt);
#		_txtfile.write('\n');
	
#	return;



#Part A
a = myString * 2;
b = myString[-17] + myString[-11] + myString[-5] + myString[-1] + myString[0];
c = myString[5:11];
d = myString[:7];
e = myString[20:];
f = len(myString);

partA = [a, b, c, d, e, f];

i = 0;

for i in range(0, 6, 1):
	_txtfile.write(str(partA[i]));
	_txtfile.write('\n');

_txtfile.write('\n');
#outputPart(partA);

#Part B
L = [2, 3, 5, 7, 11, 9, 13, 23, 29, -1];

a = L[-3];
b = L[3:7];
c = L.append(37);
d = L.insert(7, 29);
e = L.sort();
f = L.reverse();
g = len(L);

M = [a, b, c, d, e, f, g];

i = 0;

for i in range(0, 7, 1):
	_txtfile.write(str(M[i]));
	_txtfile.write('\n');

_txtfile.write('\n');

#Part 3
t = (1, 2, 3, 4, 5, 6);

a = t[3];
b = t[-3];
c = t = 4, 8, 12, 16;
d = len(t);

M = [a, b, c, d]

i = 0;

for i in range(0, 4, 1):
	_txtfile.write(str(M[i]));
	_txtfile.write('\n');

#Part 4
D = {"Fortran":1956, "Cobol":1960, "Lisp":1960, "C":1972, "Pascal":1972, "Python":1991};

a = D["Cobol"];
b = D["Python"] -= 2;
c = len(D);
_txtfile.close();
