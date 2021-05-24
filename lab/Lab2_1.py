import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

def f1(x):
	return 1/(1+25*x*x)
def f2(x):
	return x/(1+math.pow(x,4))
def f3(x):
	return np.arctan(x)
# xn yn 插值节点 x是需要求值的点
# xn 是一个数组，包含 x0 x1 .. xn
def Lanrange(xn,yn,x):
	n = len(xn)-1
	lagrange = 0
	for i in range(n+1):
		li =1
		for j in range(n+1):
			if(j!=i):
				li*=(x-xn[j])/(xn[i]-xn[j])
		lagrange += yn[i]*li
	return lagrange

# xn yn 用来画原函数的点
# LagXn LagYn 用来画Lagrange插值函数的点
# DiscreteXn DiscreteYn 插值节点。
def Draw(xn, yn, LagXn, LagYn,DiscreteXn,DiscreteYn,info):
	plt.plot(LagXn, LagYn, label="拟合曲线Ln(x)", color="black")
	plt.plot(xn,yn,label="实际曲线f(x)",color="green",linestyle = ':')
	plt.scatter(DiscreteXn, DiscreteYn, label="插值节点", color="red")
	#使用中文字符集
	mpl.rcParams['font.sans-serif'] = ['SimHei']
	mpl.rcParams['axes.unicode_minus'] = False
	plt.title("拉格朗日插值拟合数据 n="+str(len(DiscreteXn)-1))
	plt.legend(loc="upper left")
	plt.savefig("./"+info+".png")
	plt.show()


def main1():
	for n  in range(2,16):
		xn=[]
		yn=[]
		DiscreteXn = []
		DiscreteYn = []
		LagXn=[]
		LagYn=[]
		for i in range(n+1):
			xi = -1+2*i/n
			DiscreteXn.append(xi)
			DiscreteYn.append(f1(xi))
		for i in range(100*n+1):
			xi = -1+2*i/(100*n)
			LagXn.append(xi)
			LagYn.append(Lanrange(DiscreteXn,DiscreteYn,xi))
		for i in range(100*n):
			xi = -1+2*i/(100*n)
			xn.append(xi)
			yn.append(f1(xi))
		Draw(xn, yn, LagXn, LagYn,DiscreteXn,DiscreteYn,"f1_n="+str(n))

def main2():
	for n  in range(2,16):
		xn=[]
		yn=[]
		DiscreteXn = []
		DiscreteYn = []
		LagXn=[]
		LagYn=[]
		for i in range(n+1):
			xi = -5+10*i/n
			DiscreteXn.append(xi)
			DiscreteYn.append(f2(xi))
		for i in range(100*n+1):
			xi = -5+10*i/(100*n)
			LagXn.append(xi)
			LagYn.append(Lanrange(DiscreteXn,DiscreteYn,xi))
		for i in range(100*n):
			xi = -5+10*i/(100*n)
			xn.append(xi)
			yn.append(f2(xi))
		Draw(xn, yn, LagXn, LagYn,DiscreteXn,DiscreteYn,"f2_n="+str(n))

def main3():
	for n  in range(2,16):
		xn=[]
		yn=[]
		DiscreteXn = []
		DiscreteYn = []
		LagXn=[]
		LagYn=[]
		for i in range(n+1):
			xi = -5+10*i/n
			DiscreteXn.append(xi)
			DiscreteYn.append(f3(xi))
		for i in range(100*n+1):
			xi = -5+10*i/(100*n)
			LagXn.append(xi)
			LagYn.append(Lanrange(DiscreteXn,DiscreteYn,xi))
		for i in range(100*n):
			xi = -5+10*i/(100*n)
			xn.append(xi)
			yn.append(f3(xi))
		Draw(xn, yn, LagXn, LagYn,DiscreteXn,DiscreteYn,"f3_n="+str(n))



if __name__ == "__main__":
	main1()
	main2()
	main3()