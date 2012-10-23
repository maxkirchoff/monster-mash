import socket, ssl, subprocess, time, os, json, random, httplib, urllib, ConfigParser
from subprocess import *

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

server = Config.get("irc", "server")
port = Config.getint("irc", "port")
channel = Config.get("irc", "channel")
botnick = Config.get("points", "nick")
password = Config.get("irc", "password")

def ping(): 
  ircsock.send("PONG :pingis\n")  

def sendmsg(msg): 
  ircsock.send("PRIVMSG "+ channel +" :"+ msg +"\n")

def voice(ircstr):
  (_, _, voicestr) = ircstr.partition("!v")
  voicestr = voicestr.upper()
  sendmsg(voicestr)
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port)) 
ircsock = ssl.wrap_socket(s)
ircsock.send("PASS "+ password +"\n") 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +"QA PUSHER BOT!!!! \n") 
ircsock.send("NICK "+ botnick +"\n") 
ircsock.send("JOIN "+ channel +"\n")

while 1: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r') 
  print(ircmsg)
   
  if ircmsg.find(":!v") != -1:
    voice(ircmsg)

  if ircmsg.find("point") != -1:
    sendmsg("POINTS....IT'S WHATS FOR DINNER")

  # currently does this everytime he talks...need to rework it
  #if ircmsg.find("brent") != -1:
  #  sendmsg("BRENT CAN'T HELP YOU NOW. SCORE THE POINTS OR ELSE.")

  # currently does this everytime he talks...need to rework it
  #if ircmsg.find("zac") != -1:
  #  sendmsg("DID SOMEONE HEAR CRYING? LIKE A LITTLE BABY.")

  if ircmsg.find("win") != -1:
    sendmsg("POINTS ARE FOR WINNERS!")

  if ircmsg.find("points_monster") != -1:
    sendmsg("MY MOM CALLED ME TEDDY")

  if ircmsg.find("PING :") != -1:
    ping()