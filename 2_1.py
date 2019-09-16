import numpy as np

def target_function(w,b):
    x=2*w+3*b
    y=2*b+1
    z=x*y
    return x,y,z

def single_variable(w,b,t):
    print("\nsingle variable: b ------")
    error=1e-5
    while(True):
        x,y,z=target_function(w,b)
        delta_z=z-t
        print("w=%f,b=%f,z=%f,delta_z=%f"%(w,b,z,delta_z))
        if abs(delta_z)<error:
            break
        delta_b=delta_z/63
        print("delta_b=%f"%delta_b)
        b=b-delta_b

    print("done!")
    print("final b=%f"%b)


def single_variable_new(w,b,t):
    print("\nsingle variable new: b ------")
    error=1e-5
    while(True):
        x,y,z=target_function(w,b)
        delta_z=z-t
        print("w=%f,b=%f,z=%f,delta_z=%f"%(w,b,z,delta_z))
        if abs(delta_z)<error:
            break
        factor_b=2*x+3*y
        delta_b=delta_z/factor_b
        print("factor_b=%f,delta_b=%f"%(factor_b,delta_b))
        b=b-delta_b

    print("done!")
    print("final b=%f"%b)

def double_variable(w,b,t):
    print("\ndouble variable: w,b ------")
    error=1e-5
    while(True):
        x,y,z=target_function(w,b)
        delta_z=z-t
        print("w=%f,b=%f,z=%f,delta_z=%f"%(w,b,z,delta_z))
        if abs(delta_z)<error:
            break
        delta_w=delta_z/18/2
        delta_b=delta_z/63/2
        print("delta_w=%f,delta_b=%f"%(delta_w,delta_b))
        b=b-delta_b
        w=w-delta_w

    print("done!")
    print("final w=%f"%w)
    print("final b=%f"%b)


def double_variable_new(w,b,t):
    print("\ndouble variable new: w,b ------")
    error=1e-5
    while(True):
        x,y,z=target_function(w,b)
        delta_z=z-t
        print("w=%f,b=%f,z=%f,delta_z=%f"%(w,b,z,delta_z))
        if abs(delta_z)<error:
            break
        factor_w,factor_b=calculate_wb_factor(x,y)
        delta_w=delta_z/factor_w/2
        delta_b=delta_z/factor_b/2
        print("factor_w=%f,factor_b=%f,delta_w=%f,delta_b=%f"%(factor_w,factor_b,delta_w,delta_b))
        b=b-delta_b
        w=w-delta_w

    print("done!")
    print("final w=%f"%w)
    print("final b=%f"%b)

def calculate_wb_factor(x,y):
    factor_b=2*x+3*y
    factor_w=2*y
    return factor_w,factor_b

if __name__=='__main__':
    w=3
    b=4
    t=150
    single_variable(w,b,t)
    single_variable_new(w,b,t)
    double_variable(w,b,t)
    double_variable_new(w,b,t)
    
