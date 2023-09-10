'''a = 0

print(a) if no value assigned to a then it will generate error'''

a,b =1,0
try:
    k = a // b  # raises divide by zero exception.
    print(k)

except Exception:            #if here zerodevisionerror exception clss then that will execute and finally execute Exception class will not execute if it is after 0divsionerrror class
    print("inside Exception")

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")


finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')