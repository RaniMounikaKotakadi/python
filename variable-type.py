#This funtion will tell you what is the given variable type
def TellVariableType():
    #n = input ("Enter something and it will tell you what type it is ")
    n = 10
    print ( type (n) )
    i = 'abc'
    print ( type (i) )
    p = [1,2,3]
    print ( type (p) )
def TellVariableType_withinputatruntime():
    q = input ("Enter something and it will tell you what type it is ")
    print ( type (q) )
    #At runtime everything you have given is considered as string.

TellVariableType()
TellVariableType_withinputatruntime()
