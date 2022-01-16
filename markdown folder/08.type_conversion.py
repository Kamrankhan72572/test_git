x=10         #integer
y=10.2       #float
z="hello"    #string
#implicit type conversion
x=x*y
print(type(x))
print(type(x*y))
print(x,"type of xis:",type(x))                      # float with integer will be float
print(type(x))

 # explicit  type conversion
age=input("what is your age ?")
age=int(age)               # 1st way to covernt string in integer
print(type(age))

age=input("what is your age ?")   # 2nd way to convert string into integer
print(type(int(age)))

age=input("what is your age ?")
print(age,type(int(age)))            # 3rd way to convert string into integer
 # in case of float every functions output will float.

name=input("what is your name?")
print(name,type(int(name)))

name=input("what is your name?")
print(name,type(str(name)))



