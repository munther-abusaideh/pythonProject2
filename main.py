def Function1 (*args,**kwargs):
    Numbers=args[0]
    Numbers=Numbers.split()
    Numbers=sorted(Numbers)
    for val in kwargs.values():
        if val.lower()== "l":
            return float(Numbers[-1])
        elif val.lower()== "s":
            return float(Numbers[0])
        else:
            return "ERROR !!! "
result1=Function1(input(), a=input())
result2=Function1(input(), a=input())
print(result1)
print(result2)