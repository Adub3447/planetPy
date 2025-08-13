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
        
def spawnPlanets(num_Planets,screen_width, screen_height, assets):
    """Spawns a given number of planets with random positions and images."""
    spawned_Planets = []
    planet_images = [assets["metal_planet"], assets["food_planet"], assets["goods_planet"]]
    
    for i in range(num_Planets):
        planet_image = random.choice(planet_images) 
        
        #delete if UI offset works
        # casting for use in randint
        image_width = int(planet_image.get_width())
        image_height = int(planet_image.get_height())
        #screen_width = int(screen_width)
        #screen_height = int(screen_height)

        # Use the image dimensions to calculate valid spawn coordinates
        rand_x = random.randint(image_width, screen_width - image_width - 1)    # 1 is used to temp replace uiOffset
        rand_y = random.randint(image_height, screen_height - image_height - 1)
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
    rand_x = random.randint(station_image.get_width(), planet_x - station_image.get_width() - 1)    # 1 used to temp replace uiOffset
    rand_y = random.randint(station_image.get_height(), planet_y - station_image.get_height() - 1)
    position = (rand_x, rand_y)
    spawned_Stations.append(Station(position, station_image))

    return spawned_Stations

stations = []
# endregion design 


# region ---Design Ships---
class Ship:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = self.image.get_rect(center=position)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

def spawnShip(station_x, station_y, assets):
    """Spawns a ship with test position."""
    spawned_Ships = []
    ship_types = [assets["ship_food"], assets["ship_metal"], assets["ship_pirate"]]
    ship_image = ship_types[1]

   # ship_type = "metal"
    # replace this with select case
    #if ship_type == "food":
    #    ship_image = ship_types[0]
    #if ship_type == "metal":
    #    ship_image = ship_types[1]
    #if ship_type == "pirate":
    #        ship_image = ship_types[2]
    #else:
    #    print("no conditions met")

        
    # spawn with center of rect orbitoffset from planetxy
   # rand_x = random.randint(ship_image.get_width(), station_x - ship_image.get_width() - 1)    # 1 used to temp replace uiOffset
    #rand_y = random.randint(ship_image.get_height(), station_y - ship_image.get_height() - 1)
    position = (station_x, station_y)
    spawned_Ships.append(Ship(position, ship_image))
    return spawned_Ships

ships = []
# endregion design ships
