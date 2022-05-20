def f(x):
    return (0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5) #trigo func
a = 0
b = 0.8
n = 10
h = (b-a)/n #width of trapezoid

Sample = h * (f(a)+f(b)) #start value of summation
for i in range(1,n):
    Sample+=f(a+i*h)

Int = Sample*h
print('Int = %0.4f' %Int)
