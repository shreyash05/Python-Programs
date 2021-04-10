import functools
print(functools.reduce(lambda a,b : a+b, list(map(lambda no: no+2,list(filter(lambda no:(no%2==0),arr=[1,3,2,4,6,5,4]))))))