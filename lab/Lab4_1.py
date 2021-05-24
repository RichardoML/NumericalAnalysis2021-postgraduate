import math

def Trapzoid(f,a,b):
	return (b-a)*(f(a)+f(b))/2
def Simpson(f,a,b):
	return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6
def GuassLegendre(f,a,b):
	t1 = (a+b)/2-(b-a)*(1/math.sqrt(3))/2
	t2 = (a+b)/2+(b-a)*(1/math.sqrt(3))/2
	return (b-a)*(f(t1)+f(t2))/2
# 复化梯形求积公式
def ComplexTrapzoid(f,a,b,n):
	h=(b-a)/n
	sum = 0
	for k in range(n):
		sum += Trapzoid(f,a+k*h,a+(k+1)*h)
	return sum

# 复化Simpson求积公式
def  ComplexSimpson(f,a,b,n):
	h=(b-a)/n
	sum =0
	for k in range(n):
		sum += Simpson(f,a+k*h,a+(k+1)*h)
	return sum

def CompexGuassLegendreI(f,a,b,n):
	h = (b-a)/n
	sum = 0
	for k in range(n):
		sum += GuassLegendre(f,a+k*h,a+(k+1)*h)
	return sum

def f1(x):
	return 1/(x*x-1)
def f2(x):
	return 1/(x*x+1)
def f3(x):
	return math.pow(3,x)
def f4(x):
	return x*math.exp(x)

def test():
	print("(1):")
	CompTrap = -2*ComplexTrapzoid(f1,2,3,1792)
	CompSimp = -2*ComplexSimpson(f1,2,3,21)
	CompGuaLeg = -2*CompexGuassLegendreI(f1,2,3,19)
	Exact = math.log(2,math.exp(1))-math.log(3,math.exp(1))
	print("复化梯形求积计算值",CompTrap,"误差",Exact-CompTrap)
	print("复化Simpson求积计算值",CompSimp,"误差",Exact-CompSimp)
	print("复化Guass-Legendre求积计算值",CompGuaLeg,"误差",Exact-CompGuaLeg)
	print("准确值",Exact)
	print("(2):")
	CompTrap = 4*ComplexTrapzoid(f2,0,1,3652)
	CompSimp = 4*ComplexSimpson(f2,0,1,29)
	CompGuaLeg = 4*CompexGuassLegendreI(f2,0,1,26)
	Exact = math.pi
	print("复化梯形求积计算值",CompTrap,"误差",Exact-CompTrap)
	print("复化Simpson求积计算值",CompSimp,"误差",Exact-CompSimp)
	print("复化Guass-Legendre求积计算值",CompGuaLeg,"误差",Exact-CompGuaLeg)
	print("准确值",Exact)
	print("(3):")
	CompTrap = ComplexTrapzoid(f3,0,1,2457)
	CompSimp = ComplexSimpson(f3,0,1,14)
	CompGuaLeg = CompexGuassLegendreI(f3,0,1,12)
	Exact = 2/math.log(3,math.exp(1))
	print("复化梯形求积计算值",CompTrap,"误差",Exact-CompTrap)
	print("复化Simpson求积计算值",CompSimp,"误差",Exact-CompSimp)
	print("复化Guass-Legendre求积计算值",CompGuaLeg,"误差",Exact-CompGuaLeg)
	print("准确值",Exact)
	print("(4):")
	CompTrap = ComplexTrapzoid(f4,1,2,7019)
	CompSimp = ComplexSimpson(f4,1,2,24)
	CompGuaLeg = CompexGuassLegendreI(f4,1,2,22)
	Exact = math.exp(1)*math.exp(1)
	print("复化梯形求积计算值",CompTrap,"误差",Exact-CompTrap)
	print("复化Simpson求积计算值",CompSimp,"误差",Exact-CompSimp)
	print("复化Guass-Legendre求积计算值",CompGuaLeg,"误差",Exact-CompGuaLeg)
	print("准确值",Exact)
	return

if __name__ == '__main__':
	test();