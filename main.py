class cat:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
        print("I am a cat.My name is " ,self.name,"and my age is ",self.age)

    def sound(self):
        print("I make meow sound")

class dog:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("I am a dog. My name is " ,self.name,"and my age is",self.age)

    def sound(self):
        print("I make bark sound")

cat1=cat("Cindy",3)
dog1=dog("Milo",5)

for animal in (cat1,dog1):
    animal.info()
    animal.sound()

    