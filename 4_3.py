import numpy as np
import matplotlib.pyplot as plt

from HelperClass.DataReader_1_0 import *

file_name="Data/ch04.npz"

class NeuralNet_0_1(object):
    def __init__(self,eta):
        self.eta=eta
        self.w=0
        self.b=0

    def __forward(self,x):
        z=x*self.w+self.b
        return z

    def __backword(self,x,y,z):
        dz=z-y
        db=dz
        dw=dz*x
        return dw,db

    def __update(self,dw,db):
        self.w=self.w-self.eta*dw
        self.b=self.b-self.eta*db
    
    def train(self,dataReader):
        for i in range(dataReader.num_train):
            x,y=dataReader.GetSingleTrainSample(i)
            z=self.__forward(x)
            dw,db=self.__backword(x,y,z)
            self.__update(dw,db)

    def inference(self,x):
        return self.__forward(x)


def ShowResult(net,dataReader):
    X,Y=dataReader.GetWholeTrainSamples()
    plt.plot(X,Y,"b.")
    PX=np.linspace(0,1,10)
    PZ=net.inference(PX)
    plt.plot(PX,PZ,"r")
    plt.title("Air Conditioner Power")
    plt.xlabel("Number of Servers(K)")
    plt.ylabel("Power of Air Conditioner(KW)")
    plt.show()

if __name__=='__main__':
    sdr=DataReader_1_0(file_name)
    sdr.ReadData()
    eta=0.1
    net=NeuralNet_0_1(eta)
    net.train(sdr)
    print("w=%f,b=%f"%(net.w,net.b))
    result=net.inference(1.346)
    print("result=",result)
    ShowResult(net,sdr)