from tealight.net import connect, send
from datetime import age

connect("myapp")

def handle_message(msg):
  print "Received: "+msg
  print age()