import pygame
import math
from game.ui.resolution import image_position


class Car:

    def __init__(self):
        self.car_image = self.car_image
        self.x = self.x_position
        self.y = self.y_position
        self.car_speed = 0
        self.car_acceleration = 0.2
        self.max_speed = 3
        self.min_speed = -1
        self.movement_speed = 2
        self.max_movement_speed = 2.5
        self.car_angle = self.car_angle
        self.car_nitro = 5

    def rotate_left(self):
        self.car_angle += self.movement_speed

    def rotate_right(self):
        self.car_angle -= self.movement_speed

    def render_position(self, game_window):
        image_position(game_window, self.car_image, (self.x, self.y), self.car_angle)

    def movement(self):
        half_degree = 180

        plane_angle = self.car_angle * (math.pi / half_degree)

        self.x += -self.car_speed * math.sin(plane_angle)
        self.y += -self.car_speed * math.cos(plane_angle)

    def forward_control(self):

        while self.car_speed <= self.max_speed:
            self.car_speed = self.car_speed + self.car_acceleration

        else:
            self.car_speed = self.max_speed

        self.movement()

    def forward_slowdown(self):

        if self.car_speed > 0:
            self.car_speed = self.car_speed - self.car_acceleration / 6

        else:
            self.car_speed = 0

        self.movement()

    def backward_control(self):

        while self.car_speed <= self.min_speed:
            self.car_speed = -self.car_acceleration

        else:
            self.car_speed = self.min_speed

        self.movement()

    def nitro(self):
        self.car_speed = self.car_speed + self.car_nitro

        self.movement()

    def drift(self):

        while self.movement_speed <= self.max_movement_speed:
            self.movement_speed = self.movement_speed + (self.movement_speed / 8)

        else:
            self.movement_speed = self.movement_speed

    def out_of_track(self):
        self.car_speed = 0
        self.max_speed = 0
        self.movement_speed = 0

        self.max_movement_speed = 0
        self.max_speed -= 10
        self.car_speed -= 10

        self.movement()

    def car_collide(self):
        self.car_speed = 0
        self.max_speed = 0
        self.max_speed = self.max_speed - 2.6
        self.car_speed = self.car_speed - 2.6

        # self.car_image = pink_lambo

        self.movement()

    def border_collide(self, car_hitbox):
        image_hitbox = pygame.mask.from_surface(self.car_image)
        car_position = self.x, self.y
        out_of_track = car_hitbox.overlap(image_hitbox, car_position)

        return out_of_track
