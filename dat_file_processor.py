from array import array
import os,sys
import subprocess
import glob
from os import path

global sum1,sum2
sum1=0
sum2=0

try:
      f = open(sys.argv[1],'r').readlines()[4:]
      first_6_lines = f.pop(0)
      array= []
      for line in f:
            parts = line.split() # split line into parts
            if len(parts) > 1:   # if at least 2 parts/columns
                 # print ("  ", float(parts[0]), "  ",  float(parts[1]), " = ",  float(parts[0]) ** 2  *  float(parts[1]))
                  if float(parts[0])  >= 0.5 and float(parts[0]) <= 1:
                        sum1=sum1+float(parts[0])**2 * float(parts[1])
                  if float(parts[0])  >= 1.1 and float(parts[0]) <= 1.8:
                        sum2=sum2+float(parts[0])**2 * float(parts[1])
except  ValueError :
      print ("ERROR: XML code are elimating from file")
except ZeroDivisionError:
      print ("ERROT: Sum1 and Sum2 may be zero, Divison can not be possible")
             
output=sum2/sum1

print("Final Output = ", output)
