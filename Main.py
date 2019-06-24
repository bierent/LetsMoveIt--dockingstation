#!/usr/bin/python3
import socket               # import modules
import time                                 
import RPi.GPIO as GPIO                     
import select

GPIO.setwarnings(False)             # disable warnings        
GPIO.setmode(GPIO.BCM)              # use GPIO as number, not the pins       
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # inwards
GPIO.setup(24, GPIO.OUT)          # outwards

GPIO.output(24, False)

s = socket.socket()                 # create a socket object
#s.settimeout(1.0)

port = 8080                         # eserve a port for your service

host = "145.93.32.216"              # the server's address
s.connect((host, port))             # bind to port
#print (s.recv(1024).decode())       # print connected adress
#s.setblocking(0)
s.send('Connected'.encode())        # confirm connection


while(1):

  data = ''
  
  if (GPIO.input(23) == GPIO.HIGH):
    #print('input')
    s.send('received'.encode())

  ready = select.select([s], [], [], 0.1)
  if ready[0]:
    data = s.recv(1024).decode()        #receive commando and print
  
  
  #print('eej')
  #print(data)
  if data == 'lift':

     GPIO.output(24, True)
     #s.send('The lift is going up'.encode())        # confirm connection
     #time.sleep(1)
     #GPIO.output(24, False)
     
     
      
  if not data:
    GPIO.output(24, False)

  
'''     
while(1):

  if (GPIO.input(23) == True):
    print('input')
    s.send('received'.encode())


  #time.sleep(0.1)
'''


  
      
       
       
