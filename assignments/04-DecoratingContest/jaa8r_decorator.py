import datetime
import urllib.request
from tkinter import messagebox
import webbrowser
import time

data = urllib.request.urlopen("https://raw.githubusercontent.com/jasona99/ImportantFiles/master/file.txt")

def weekly(func):
    def wrap(*args, **kargs):
        print("We'll get to everything in just a mo.")
        cur_time = datetime.datetime.now().time()
        hour = cur_time.hour
        if (datetime.datetime.today().weekday()) == 0:
            print("Happy Monday, losers!")
            if cur_time.hour == 13:
                print("Looks like it's class time!")
                print("Enjoy!")
                for line in data:
                    print(line)
                    time.sleep(2)
        return func(*args, **kargs)
    return wrap

@weekly
def decor(func):
    def wrapper(*args, **kargs):
        print("Ah, so you want to print?", "Sure, we'll get to it.")
        input("Press enter to continue...")
        messagebox.showerror("Print Error", "Unable to print.")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=2)
        return func(*args, **kargs)
    return wrapper

@decor
def banana():
    return "Banana"

print(banana())
