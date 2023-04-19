mygand = {
    "child": {

        "name": "loda",
        "year": 2001
    },
    "child2": {

        "name": "loda2",
        "year": 2000
    }
}


nit = {
    
    
    'nitin':"madarchod",
    "sachin":9,
    "adarsh":[1,2,3,4],
    "123":{ "32":90,"2":[{}]},
    
}

print(nit["123"])


for x in nit:
    print(nit[x])


()






jam = {
    "k" :8 ,
    "k1":[1,2,3],
    "k2":{"y1":45},
    "k3":{"l1":3,"l2":45,"l3":[1,2,3,4]}
    
}
def kala(jam):
    
    for x in jam:
        if x=="k2":
            return jam[x]
            
x=kala(jam)
print(x)


print(mygand)


child1 = {
        "name": "Emil",
        "year": 2004
}
child2 = {
        "name": "Tobias",
        "year": 2007
}
child3 = {
        "name": "Linus",
        "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)


myfamily = {
    "gogi1": {
        "name": "mall",
        "year": 3086
    },
    "gogi2": {
        "name": "muku",
        "year": 6789
    }
}

print(myfamily["gogi2"]["name"])


class Person:
    def __init__(self, fname, lname,age,sex):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.sex = sex

    def printname(self):
        print(self.firstname, self.lastname)
        print(self.age)
        print(self.sex)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe","69","male")
x.printname()


class Person:
    x = Person("nitin","thakur","22","male")
    x.printname()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + ", age is " + str(self.age))

p1 = Person("John", 36)
p2 = Person("nitin",34)
del p1
#p1.myfunc()
p2.myfunc()
