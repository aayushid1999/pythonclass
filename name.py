name="aayushi dassani"
print(name[1])
print(name[-2])
print(name[1:-1])
print(len(name)-1)
print(f"{2+2}+{10%3}")
print(name.title())
##print(name.strip())
print(name.replace("dassani","k"))
print(name.find("dassani"))
print(name.find("aayushi"))

fruits=["apple","banana","orange"]
fruits.sort()
print(fruits)

fruits={"apple","banana","cherry"}
brands={"keventers","washington","spencer","apple"}
fruits.intersection(brands)
fruits.add("guava")
print(fruits)
fruits.discard("spencer")
print(fruits)
fruits=["mango","banana","peach"]
fruits.pop(0)
print(fruits)
fruits.remove("peach")
print(fruits)
x=10,fruits.copy()
x=fruits.copy()
print(x)
print(type(x))
fruits.pop(0)
print(fruits)
fruits=list(("apple","banana","cherry"))
print(fruits)
print(len(fruits))
