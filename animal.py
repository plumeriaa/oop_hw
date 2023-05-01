"""
Animal 클래스를 만들어서
-이름과 나이를 속성으로 
-speak를 메소드로 갖게 해주세요.

Dog 클래스와 Cat 클래스를 각각 Animal 상속을 받아 만들어 주세요.
-speak 메소드를 각각의 클래스에 맞게 구현해주세요.
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Animal is speaking.")

class Dog(Animal):
    def speak(self):
        print("Woof woof!")

class Cat(Animal):
    def speak(self):
        print("Meow meow!")

anim1 = Animal("Ani", 3)
anim1.speak()

dog1 = Dog("Dog", 3)
cat1 = Cat("Cat", 2)

dog1.speak()
cat1.speak()