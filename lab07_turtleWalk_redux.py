'''
CSC101 Lab 7
Part 2: Turtle walking inside rectangle
Tyler Smith
10/7/2020
'''

import random     
import turtle

turtle.shape('turtle') # make turtle look like ... a turtle!


def is_point_in_rectangle(x, y, x1, y1, x2, y2):
   result = (x1 <= x <= x2) and (y1 <= y<= y2)
   return result

def main():
   # Draw rectangle with corners (-213, -113) and (213,113)
   
   # Place turtle back at (0,0)
   
   # Simulation of turtle in rectangle starts here
   
   while True: 
      
      turtle.left(random.randint(-30,30))
      turtle.forward(10)
   
      x, y = turtle.position()
      
      if not is_point_in_rectangle(x, y, -213, -113, 213, 113):
         turtle.left(180)
         turtle.forward(10)
         
  
main()       
turtle.done()