# Created: 03/18/19
# Author: Connor McNaboe
# Purpose: User class, defines user functions (will be added to over time)
from random import *

class User(object): 

    def __init__(self, username): 
        self._usrname = "defualt_username" + str(randint(1, 1000))

    def getUserName(self): 
        self.usrname = input("Please enter a desired username: ")
        