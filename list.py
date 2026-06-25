age=[10,23,13,14,56]
print(age)
#accessing through index
print(age[3])
print(age[-4])
#change through index
age[4]=40
print(age)
#adding element
age.append(60)
print(age)
#insert function
age.insert(2,30)
print(age)
#remove function dierct value
age.remove(10)
print(age)
#pop function using index
age.pop(3)
print(age)
#slice function
print(age[2:4])
#length of list
print(len(age))
#sort function
age.sort()
print(age)
#reverse list
age.reverse()
print(age)
#using for loop in list
for age in age:
    print(age)
#adding two lists
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
#repetition in list
d=2*a
print(d)

