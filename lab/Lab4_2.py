import math
from sympy import *

def Simpson(f, a, b):
	return (b - a) * (f(a) + 4 * f((a + b) / 2) + f(b)) / 6

# 复化Simpson求积公式 n表示分段数 步长1/n
def  ComplexSimpson(f,a,b,n):
	h=(b-a)/n
	sum =0
	for k in range(n):
		sum += Simpson(f,a+k*h,a+(k+1)*h)
	return sum

# 变步长Simpson求积公式
def VariableStepSimpson(f,a,b,e):
	i = 1
	Sn = ComplexSimpson(f,a,b,i)# Sn初始化为S1
	S2n = ComplexSimpson(f,a,b,2*i)# S2n初始化为S2
	e_S2n = (1/15)*abs(S2n - Sn)
	while(e_S2n > e):
		i = i*2
		Sn = S2n
		S2n = ComplexSimpson(f,a,b,2*i)
		e_S2n = (1 / 15) * abs(S2n - Sn)
	return 2*i,S2n

def f1(x):
	return math.pow(x,6)/10-x*x+x
def f2(x):
	return x*math.sqrt(x)
def f3(x):
	return 1/(math.sqrt(x))

def main():
	print("(1):")
	VariStep = VariableStepSimpson(f1,0,2,0.5*math.pow(10,-7))
	print("复化Simpson:",ComplexSimpson(f1,0,2,76))
	print("变步长Simpson:","2n:",VariStep[0],"积分值:",VariStep[1])
	print("(2):")
	VariStep = VariableStepSimpson(f2,0,1,0.5*math.pow(10,-7))
	print("变步长Simpson:","2n:",VariStep[0],"积分值:",VariStep[1])
	print("(3):")
	VariStep = VariableStepSimpson(f3,5,200,0.5*math.pow(10,-7))
	print("复化Simpson:",ComplexSimpson(f3,5,200,1742))
	print("变步长Simpson:","2n:",VariStep[0],"积分值:",VariStep[1])

if __name__ == '__main__':
	main();