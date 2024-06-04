from importlib import resources
#from os import path
import pygame
#from extranion.asset.a import Asset, AssetType
from extranion.config import cfg
from extranion import game

class AssetItem:
	def __init__(self, category, atype, filepath, conf):
		self.category = category
		self.atype = atype
		self.data = None
		if self.atype == "image":  self.data = pygame.image.load(filepath)
		elif self.atype == "font": self.data = pygame.font.Font(filepath, conf["size"])

	def get(self):
		return self.data

_assets={}

def load(category, name):
	if game.DEBUG: print(f"asset.load {category} {name}")
	conf=cfg(f"{name}")
	atype=conf["atype"]
	filepath=resources.files("extranion.data").joinpath(atype).joinpath(conf["file"])
	asset = AssetItem(category, atype, filepath, conf)
	_assets[name] = asset

def unload(category=None):
	global _assets
	if category:
		for k in list(_assets.keys()):
			if _assets[k].category == category:
				del _assets[k]
	else:
		_assets = {}

def get(name):
	if name in _assets:
		return _assets[name].get()
	else:
		print(f"ERROR: Asset {name} not found")
		return None
	#if sheet_name:
	#	if sheet_name in self.__assets:
	#		return self.__assets[sheet_name].payload.get_image(asset_name)
	#	return pygame.Surface((0,0)), pygame.Rect(0,0,0,0)
	#else:
	#	if asset_name in self.__assets:
	#		if self.__assets[asset_name].asset_type == "image":
	#			return self.__assets[asset_name].payload, self.__assets[asset_name].payload.get_rect()
	#		elif self.__assets[asset_name].asset_type == "FlipBook":
	#			return self.__assets[asset_name].payload.get_image(sequence)
	#		else:
	#			print("Found")
	#			return self.__assets[asset_name].payload
	#	else:
	#		print("Warning! asset get found none")
	#		return None
