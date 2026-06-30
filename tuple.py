num=(11,12,13,14,15,11,16,17,18)
print(num)
#type function
print(type(num))
#access through index
print(num[4])
#count function
print(num.count(11))
#index function
print(num.index(14))


#changement in tuple by coverting it into a list
list=list(num)
list.append(48)
print(list)
list.insert(4,60)
print(list)
list.remove(16)
print(list)
list.pop(3)
print(list)
list.sort()
print(list)
list.reverse()
print(list)


#coverting list into tuple
num=tuple(list)
print(num)
