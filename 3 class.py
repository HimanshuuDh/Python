"""
author: brighter
date: 18/03/26
this program converts distance form miles to km
"""

miles = float(input("enter the distance in miles: "))

while miles !=-1:
      km =miles * 1.60934
      print("the converted value is ", km, "kms")
      miles = float(input("enter the distance in miles"))

print("thank you !")