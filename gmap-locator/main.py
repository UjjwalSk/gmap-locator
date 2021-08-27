import sys
import os
import webbrowser


def run():
    try:
        return __import__("pyperclip")
    except:
        os.system('pip install pyperclip')
        return __import__("pyperclip")


pyperclip = run()
if(len(sys.argv) > 1):
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/"+address)
