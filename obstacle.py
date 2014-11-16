import pygame.draw
from object import Object
from player import Player

#Defines an object which will allow a player to pass through the object
#If the player's state matches the allowed state of the obstacle.
class Obstacle(Object):


	def __init__(self, xPos, yPos, xDim, yDim, state):
		Object.__init__(self, xPos, yPos, xDim, yDim)
		self.allowed_state = state
		
		if(self.allowed_state == 'solid'): self.color = (255, 0, 0)
		elif(self.allowed_state == 'liquid'): self.color = (0, 0, 255)
		elif(self.allowed_state == 'gas'): self.color = (255, 255, 255)

	def update(self):
		Object.update(self)
		#self.x_position -= Obstacle.movement_speed

	def is_colliding(self, _object):
		#If it's a player check if it's allowed
		#if(hasattr(_object, 'state')):
		#	if(_object.state == self.allowed_state): 
		#		return False
		#At this point, object is not allowed, test for normal collisions
		return Object.is_colliding(self, _object)
