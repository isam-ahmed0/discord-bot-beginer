import time
import os
from bot import bot, message_queue, pin_queue, shut

def cli():
    os.system("cls" if os.name == "nt" else "clear")
    print("loading...")
    time.sleep(4)
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        print("___________________")
        print("Isam's Discord bot")
        print("1. send msg")
        print("2. help")
        print("3. pin msg")
        print("4. Shut down bot")
        print("5. exit")
        choose = input("Choose option: ")
        
        if choose == "1":
            ch = input("Enter channel id: " )
            msg = input("Enter message: ")

            if ch and msg:
                message_queue.put((ch, msg))
        elif choose == "2":
            print("")
            print("This is a discord bot")
            print("")
            input("Enter to continue")
        elif choose == "3":
            cid = input("Enter channel id: ")
            msgid = input("Enter msg id: ")
            if cid and msgid:
                pin_queue.put((cid, msgid))
        elif choose == "4":
            shut()
        elif choose == "5":
            shut()
            break
        else:
            print(f"\n{choose} is not valid")
            input("Enter to continue")