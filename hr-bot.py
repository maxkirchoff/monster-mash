import re, socket, ssl, subprocess, time, os, json, random, httplib, urllib, ConfigParser
from subprocess import *

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

server = Config.get("irc", "server")
port = Config.getint("irc", "port")
channel = Config.get("irc", "channel")
botnick = Config.get("hr", "nick")
password = Config.get("irc", "password")

def ping(): 
  ircsock.send("PONG :pingis\n")  

def sendMsg(msg):
  ircsock.send("PRIVMSG "+ channel +" :"+ msg +"\n")

def parseNick(msg):
  rx = re.compile("(?:!|^)[^!]*")
  strings = rx.findall(ircmsg)
  username = strings[0]
  return username[1:]

def badWords():
  return Config.get("hr", "bad_words").split(',')
  
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

  bad_words = badWords()

  for bad_word in bad_words:
    if ircmsg.find(bad_word) != -1:
      username = parseNick(ircmsg)
      sendMsg("HR VIOLATION. " + username + " has been fined one HR credit for saying '" + bad_word + "'")
      os.system('say "HR VIOLATION. ' + username + ' has been fined one HR credit"')

  if ircmsg.find("PING :") != -1:
    ping()
