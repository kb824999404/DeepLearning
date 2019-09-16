import numpy as np
import matplotlib.pyplot as plt

a=np.array([1,2,3,4,5,6]).reshape(2,3)
b=np.array([1,1,1,1,1,1]).reshape(2,3)

print("a:")
print(a)

print("b:")
print(b)

print("a*b:")
print(a*b)

print("np.multiply(a,b):")
print(np.multiply(a,b))

print("np.dot(a,b.T)")
print(np.dot(a,b.T))


data=np.random.randn(3,4)           #标准正态分布:均值0方差1的正态分布
print(data)

data=np.random.rand(3,4)            #正态分布随机样本位于[0,1)中
print(data)

data=np.random.random(size=[3,4])   #返回指定size的[0,1)随机数矩阵
print(data)

a=np.random.normal(0,2,100)         #正态分布或高斯分布中取随机值 返回均值为mean, 标准差为stdev的size个数
print(a.mean())
print(a.std())
print(a)

b=np.random.randint(0,1000,10)      #随机从[1,1000)中取10个数
print(b)