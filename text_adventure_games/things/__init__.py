# This pulls all the these classes from these respective files into "things" package namespace
# So when we import the things package, python executes the this __init__.py file and pulls these class in for us to directly mention and use
from .base import Thing
from .characters import Character
from .locations import Location
from .items import Item

# This defines what gets exported when you do : from text_adventure_games.things import *
__all__ = [Thing, Character, Location, Item]
