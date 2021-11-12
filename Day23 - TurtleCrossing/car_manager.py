from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RIGHT_SCREEN = 300
NUM_CARS = 30
SPAWN_CHANCE = 30
NUM_ROADS = 6

class Car(Turtle):
    def __init__(self, start_pos):
        super().__init__(shape='square')
        self.penup()                      # Stop turtle from drawing
        self.setx(RIGHT_SCREEN)           # Place the car on the right of the screen
        self.sety(start_pos)
        self.resizemode('user')           # Allow the shape to be changed
        self.shapesize(stretch_len=1.5)   # Change the shape to be twice the width of its height
        self.color(random.choice(COLORS)) # Apply a random color
        self.parked = True                # Value to check if car is moving on a road

    def update(self, speed):
        self.setx(self.xcor() - speed)
        if self.xcor() < -RIGHT_SCREEN - 30:
            self.clear()
            return True
        return False
    
    def getX(self):
        return self.xcor()

class CarManager:
    def __init__(self, screen_size):
        self.car_list = []
        # Set up a list for the roads, which are spaced evenly
        self.roads = []
        road_space = (screen_size * 0.9) / NUM_ROADS        
        # The roadblocks list will be a list of timers which ensure no two cars appear at the same time.
        self.roadblocks = []

        for x in range(1, NUM_ROADS + 1):
            self.roads.append(-(screen_size/2) + (x * road_space))
            self.roadblocks.append(0)
        
    def update(self, level):
        for car in self.car_list:
            if car.update(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))):
                self.car_list.remove(car)
        for x in range(len(self.roads)):
            chance_range = 100 - level * 5
            if chance_range <= SPAWN_CHANCE + 10:
                chance_range = SPAWN_CHANCE + 10
            chance = random.randint(0, chance_range)
            if chance <= SPAWN_CHANCE:
                if self.roadblocks[x] <= 0:
                    car = Car(self.roads[x])
                    self.car_list.append(car)
                    self.roadblocks[x] = 30 - (level * 10)
                    if self.roadblocks[x] < 2: 
                        self.roadblocks[x] = 2
            self.roadblocks[x] -= 1
    
    def collision_check(self, other):
        for car in self.car_list:
            if car.pos()[0] < 24 and car.pos()[0] > -24:
                if car.pos()[1] - 10 <= other.pos()[1] + 10 and car.pos()[1] + 10 >= other.pos()[1] - 10:
                    return True  
        return False

    pass
