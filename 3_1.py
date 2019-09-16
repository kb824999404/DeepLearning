import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm

file_name="../../data/3_1.npz"

def TargetFunction(x,w,b):
    y=w*x+b
    return y

def CreateSampleData(w,b,n):
    file=Path(file_name)
    if file.exists():
        data=np.load(file)
        x=data["data"]
        y=data["label"]
    else:
        x=np.linspace(0,1,num=n)
        noise=np.random.uniform(-0.5,0.5,size=(n))
        y=TargetFunction(x,w,b)+noise
        np.savez(file_name,data=x,label=y)
    return x,y

def CostFunction(x,y,z,count):
    c=(z-y)**2
    loss=c.sum()/count/2
    return loss

def ShowResult(ax,x,y,a,loss,title):
    ax.scatter(x,y)
    ax.plot(x,a,'r')
    titles=str.format("{0} Loss={1:01f}",title,loss)
    ax.set_title(titles)

def CalculateCostB(x,y,n,w,b):
    B=np.arange(b-1,b+1,0.05)
    Loss=[]
    for i in range(len(B)):
        z=w*x+B[i]
        loss=CostFunction(x,y,z,n)
        Loss.append(loss)
    plt.title("Loss according to b")
    plt.xlabel("b")
    plt.ylabel("J")
    plt.plot(B,Loss,"x")
    plt.show()

def CalculateCostW(x,y,n,w,b):
    W=np.arange(w-1,w+1,0.05)
    Loss=[]
    for i in range(len(W)):
        z=W[i]*x+b
        loss=CostFunction(x,y,z,n)
        Loss.append(loss)
    plt.title("Loss according to w")
    plt.xlabel("w")
    plt.ylabel("J")
    plt.plot(W,Loss,"o")
    plt.show()

def CalculateCostWB(x,y,n,w,b):
    W=np.arange(w-1,w+1,0.05)
    B=np.arange(b-1,b+1,0.05)
    Loss=[]
    for i in range(len(B)):
        for j in range(len(W)):
            z=W[i]*x+B[j]
            loss=CostFunction(x,y,z,n)
            Loss[i,j]=loss
    fig=plt.figure()
    ax=fig.gca(projection="3d")
    ax.plot_surface(W,B,Loss)
    plt.show()

def show_cost_for_4b(x,y,n,w,b):
    fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
    a1=w*x+b-1
    loss1=CostFunction(x,y,a1,n)
    ShowResult(ax1,x,y,a1,loss1,"z=2x+2")
    a2=w*x+b-0.5
    loss2=CostFunction(x,y,a2,n)
    ShowResult(ax2,x,y,a2,loss2,"z=2x+2.5")
    a3=w*x+b
    loss3=CostFunction(x,y,a3,n)
    ShowResult(ax3,x,y,a3,loss3,"z=2x+3")
    a4=w*x+b+0.5
    loss4=CostFunction(x,y,a4,n)
    ShowResult(ax4,x,y,a4,loss4,"z=2x+3.5")
    plt.show()

def show_all_4b(x,y,n,w,b):
    