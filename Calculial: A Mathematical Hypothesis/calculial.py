# Write a set of programs that attempt to revolutionize the understanding of superposiion and the energy inequality.

##  

###

import math
import cmath
import matplotlib

from matplotlib import pyplot

pi = math.pi;
# print(pi);

#i = cmath.sqrt(-1);
# e = i**2;
originallist = [];
x = 1;
y = 1;
z = 1;
c = 2.9979 * 10**8;
t = 13800000000;
a = 1;
b = 2**3;
#c = cmath.sqrt(10);
D = 93000000000
array = [0, (t**2), (a*x**2), b*(y**3), (D)]

array_two = [0, t**2, x**2, y**3, D]

pyplot.plot(array, array_two);

pyplot.title('array versus array_two');
pyplot.xlabel('array');
pyplot.ylabel('array_two');
pyplot.show();