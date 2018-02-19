#! python

import webbrowser, pyperclip, sys

statement = sys.argv[1:]
if len(statement) >= 1:
    statement = ' '.join(statement)
else:
    statement = pyperclip.paste

webbrowser.open('https://drive.google.com/drive/u/0/search?q='+statement)
