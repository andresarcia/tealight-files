from tealight.logo import (move, 
                           turn,
                           color)

print "This is tealight!"

colors = ["red", "blue", "green"]

for i in range(50,200,5):
  move(i)
  turn(150)
  c = colors[(i / 5)%3]
  color(c)
