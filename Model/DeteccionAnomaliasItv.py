"""
Main class
Entry point

"""

import sys
from sys import path
import os



sys.path.append(os.path.dirname(path[0]))




from Controller.controllerMain import *

class Main(object):
   

    def __init__(self):
        #Controller instance
        self.controller = MainController()
    

if __name__ == '__main__':
   
    main = Main()
  