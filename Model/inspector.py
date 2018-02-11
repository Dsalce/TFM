




import csv
import sys
import string
class Inspector(object):


	def __init__(self,id):
      self.totalDefect=0
      self.propor={}
      self.defects={}
      self.id=id



    def  calcNumDefect(self,listDefect):
        self.totalDefect=len(listDefect)
        for def in listDefect:
        	self.defects[def]=lista.count(def)

        for def in list(self.defects.keys()):
        	self.propor[def]=self.defects[def]/self.totalDefect




