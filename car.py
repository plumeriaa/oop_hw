"""
자동차 클래스를 만들어주세요.
-모델, 색, 현재 속도를 속성으로 갖고
-속도를 올려주는 accelerate 메소드
-속도를 낮춰주는 brake 메소드
-현재 속도를 리턴해주는 get_speed 메소드
"""

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
    
    def brake(self, amount):
        self.speed -= amount

    def get_speed(self):
        return self.speed
    
car = Car("Genesis GV80", "Beak Black")
car.accelerate(100)
car.brake(50)
print(car.get_speed())