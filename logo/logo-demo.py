from tealight.logo import (move, 
                           turn,
                           color)

print "This is tealight!"

colors = ["red", "blue", "green"]

for i in range(1,100,1):
  move(i)
  turn(35)
  c = colors[(i / 5)%3]
  color(c)
