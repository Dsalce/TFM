import sys
from sys import path
import os



sys.path.append(os.path.dirname(path[0]))




from Controller.controllerMain import *
class Main(object):
    controller=None

    def __init__(self):
        
        controller = MainController()
    

if __name__ == '__main__':
   
    main = Main()
  