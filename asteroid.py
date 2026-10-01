from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            width=LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(angle)
            second_velocity = self.velocity.rotate(-1 * angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(*self.position, radius=radius)
            asteroid_two = Asteroid(*self.position, radius=radius)
            asteroid_one.velocity = first_velocity * 1.2
            asteroid_two.velocity = second_velocity * 1.2
