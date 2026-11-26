from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update (self, dt):
        self.position += (self.velocity * dt)

    def split (self) -> None:

        self.kill()
        
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
    
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vel = self.velocity.rotate(angle)
        sec_vel = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid (self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = new_vel * 1.2

        asteroid_two = Asteroid (self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = sec_vel
