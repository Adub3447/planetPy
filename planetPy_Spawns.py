# planetPy_Spawns.py
# handles classes and functions related to spawning game objects

import pygame
import os
import random
from planetPy_UI import *


# region ---Design Planets---
class Planet:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = self.image.get_rect(center=position)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
def spawnPlanets(num_Planets, screen_width, screen_height, assets):
    """Spawns a given number of planets with random positions and images."""
    spawned_Planets = []
    planet_images = [assets["metal_planet"], assets["food_planet"], assets["goods_planet"]]
    
    for _ in range(num_Planets):
        planet_image = random.choice(planet_images) 

        # Use the image dimensions to calculate valid spawn coordinates
        rand_x = random.randint(planet_image.get_width(), screen_width - planet_image.get_width() - uiOffset)
        rand_y = random.randint(planet_image.get_height(), screen_height - planet_image.get_height() - uiOffset)
        position = (rand_x, rand_y)
        spawned_Planets.append(Planet(position, planet_image))

    return spawned_Planets

planets = []
# endregion design planets


# region ---Design Stations---
class Station:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = self.image.get_rect(center=position)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
def spawnStation(planet_x, planet_y, assets):
    """Spawns a station with random position."""
    spawned_Stations = []
    station_types = [assets["station_built"], assets["station_unbuilt"]]
    station_Built = False
    if station_Built:
        station_image = station_types[0]
    else:
        station_image = station_types[1]
        
        # spawn with center of rect orbitoffset from planetxy
        rand_x = random.randint(station_image.get_width(), screen_width - station_image.get_width() - uiOffset)
        rand_y = random.randint(station_image.get_height(), screen_height - station_image.get_height() - uiOffset)
        position = (rand_x, rand_y)
        spawned_Stations.append(Planet(position, station_image))

    return spawned_Stations

stations = []
# endregion design stations