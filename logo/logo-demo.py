from tealight.logo import (move, 
                           turn,
                           color)

print "This is tealight!"

colors = ["red", "black", "blue"]

for i in range(1,150,1):
  move(1)
  turn(35)
  c = colors[i%3]
  color(c)