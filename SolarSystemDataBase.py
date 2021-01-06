from os import read
from constants import *
import json
import pymongo
from pymongo import MongoClient

class SolarSystemRepository:
	def __init__(self):
		mclient = MongoClient(URI)
		# database = mclient.solar_system
		# self._Bodies = database.Bodies 
		database = mclient.get_database(SOLAR_SYSTEM_DATABASE)
		self._Bodies = database.Bodies

	def read(self, conditions):
		return self._Bodies.find_one(conditions,{"_id":0})

# data = {"englishName":"Earth"}

# print(SolarSystemRepository().read(data))