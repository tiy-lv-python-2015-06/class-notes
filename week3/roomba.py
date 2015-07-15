from math import radians, sin, cos
import random


class Room:
    # Height and Width
    # Tracking clean squares
    # Percent clean

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clean_squares = set()

    @property
    def area(self):
        return self.width * self.height

    @property
    def percent_clean(self):
        return len(self.clean_squares) / self.area

    def clean(self, x, y):
        self.clean_squares.add((int(x), int(y)))

    def is_clean(self, x, y):
        return (int(x), int(y)) in self.clean_squares

    def in_room(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

class Roomba:
    # move
    # Turn
    # Position
    # angle
    # speed

    def __init__(self, x, y, angle=10, speed=1):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    @property
    def position(self):
        return self.x, self.y

    @position.setter
    def position(self, position):
        self.x, self.y = position

    @property
    def next_position(self):
        move_x = sin(radians(self.angle)) * self.speed
        move_y = cos(radians(self.angle)) * self.speed

        return self.x + move_x, self.y + move_y

    def move(self):
        self.position = self.next_position

    def turn(self, angle):
        self.angle += angle
        self.angle %= 360

    def collide(self):
        self.turn(random.randint(90, 270))

class Simulation:
    # Track room
    # Track the roomba
    # step through
    # full run
    # Record the data
    # stop the simulation

    def __init__(self, room, roomba):
        self.room = room
        self.roomba = roomba
        self.steps = 0

    def step(self):
        if not self.room.in_room(*self.roomba.next_position):
            self.roomba.collide()
        else:
            self.roomba.move()

        self.room.clean(*self.roomba.position)

        self.steps += 1

    def run(self):
        results = {0.5: None, 0.9: None, 1.0: None}

        while self.room.percent_clean < 1.0 and self.steps < self.room.area * 100:
            self.step()

            for percentage in results.keys():
                if percentage <= self.room.percent_clean and results[percentage] is None:
                    results[percentage] = self.steps
        return results

if __name__ == '__main__':
    room = Room(10, 10)
    my_roomba = Roomba

    roomba = my_roomba(0, 0)
    sim = Simulation(room, roomba)
    print(sim.run())