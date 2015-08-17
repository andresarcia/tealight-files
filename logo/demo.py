from tealight.net import connect, send
import datetime

connect("myapp")

def handle_message(msg):
  print "Received: "+msg
  print age()