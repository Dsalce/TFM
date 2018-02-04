# -*- coding: utf-8 -*


import csv
import sys
import string
import numbers
import time


class itv(object):
   
       
    
    def __init__(self):
      self.dic={}
      self.headers=[]








    def setDic(self,dic):
      self.dic=dic
    def setHeader(self,header):
      self.headers=header


    def getHeader(self):
       return self.headers

    def getDic(self):
       return self.dic

    def lenDic(self):
       return len(self.dic[self.headers[0]])

    def lenHeader(self):
       return len(self.headers)













