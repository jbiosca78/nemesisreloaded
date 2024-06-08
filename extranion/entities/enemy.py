from extranion.entities.entity import Entity
import pygame
from extranion.config import cfg
from extranion import log

class Enemy(Entity):

	def __init__(self, position, spritesheet):
		super().__init__(spritesheet=spritesheet, position=position, spriterow=2)

		self._space_rect=cfg("layout.game.space_rect")

	def update(self, delta_time):
		super().update(delta_time)

		# get move directions
		#moving_x=0
		#moving_y=0
		#self._acceleration=0.02
		#self._speed_max=3

		## increase velocity in moving direction
		#self.velocity.x += moving_x*self._acceleration
		#if self.velocity.x>self._speed_max: self.velocity.x=self._speed_max
		#if self.velocity.x<-self._speed_max: self.velocity.x=-self._speed_max
		#if moving_x==0: self.velocity.x*=(1-self._speed_decay)
		#self.velocity.y += moving_y*self._acceleration
		#if self.velocity.y>self._speed_max: self.velocity.y=self._speed_max
		#if self.velocity.y<-self._speed_max: self.velocity.y=-self._speed_max
		#if moving_y==0: self.velocity.y*=(1-self._speed_decay)
		#self.spriterow=moving_x+1 # seleccionamos animación

		# check boundaries
		#sprite_width=self.spritesheet[self.spriterow][0].get_width()
		#sprite_height=self.spritesheet[self.spriterow][0].get_height()
		#if self.position.x<self._space_rect[0]:
		#	self.position.x=self._space_rect[0]
		#	if self.velocity.x<0: self.velocity.x=0
		#if self.position.x>self._space_rect[2]-sprite_width:
		#	self.position.x=self._space_rect[2]-sprite_width
		#	if self.velocity.x>0: self.velocity.x=0
		#if self.position.y<self._space_rect[1]:
		#	self.position.y=self._space_rect[1]
		#	if self.velocity.y<0: self.velocity.y=0
		#if self.position.y>self._space_rect[3]-sprite_height:
		#	self.position.y=self._space_rect[3]-sprite_height
		#	if self.velocity.y>0: self.velocity.y=0

	def render(self, canvas):
		super().render(canvas)

	def input(self, key, pressed):
		if key in self._keymap["up"]:
			self._input_pressed["up"] = pressed
			log.debug(f"up = {pressed}")
		elif key in self._keymap["down"]:
			self._input_pressed["down"]  = pressed
			log.debug(f"down = {pressed}")
		elif key in self._keymap["left"]:
			self._input_pressed["left"] = pressed
			log.debug(f"left = {pressed}")
		elif key in self._keymap["right"]:
			self._input_pressed["right"] = pressed
			log.debug(f"right = {pressed}")

		#if event.type == pygame.KEYDOWN:
		#	if event.key in self._keymap["left"]:
		#	#if event.key == pygame.K_LEFT:
		#		_dir=-1
		#	elif event.key == pygame.K_RIGHT:
		#		_dir=1
		#if event.type == pygame.KEYUP:
		#	_dir=0