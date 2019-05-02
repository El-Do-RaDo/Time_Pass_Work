import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
l = [3,4,5,6,7,8,9]
x=l
y= [0,1,2,3,4,5,6]
plt.plot(x,y)
xs = np.array(x)
ys = np.array(y)

def slop(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)**2) - mean(xs**2)))
    return m

m = slop(xs,ys)
print(m)

def intp(xs,ys,m):
	i = (mean(ys) - (m*mean(xs)))
	return i
i = intp(xs,ys,m)
print(i)

#prediction

pre = float(input("Enter the value of x to perdict: "))

def pr(i,m,pre):
	ans = (i + (m*pre))
	return ans
print(pr(i,m,pre))
plt.show()
