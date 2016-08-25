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

#outputPart(partA);

_txtfile.close();
