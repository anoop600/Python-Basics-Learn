computer = ["cpu", "monitor", "memory", "hdd", "mouse", "keyboard"]

another_list  = computer

print(id(computer))
print(id(another_list))

computer += ["ups"]
print(computer)

another_list  = computer

print(id(computer))
print(id(another_list))

a=b=c=d=e=another_list

print(a)

b.append("Cream")
print(b)
print(c)
print(d)
print(e)