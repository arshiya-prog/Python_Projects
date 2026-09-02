from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.seth(180)
            new_car.penup()
            initial_pos_y = random.randint(-250, 250)
            new_car.goto(300, initial_pos_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT