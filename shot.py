from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self,x,y, rotation, SHOT_RADIUS):
        super().__init__( x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*(PLAYER_SHOOT_SPEED)   
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)