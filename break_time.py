import webbrowser
import time


total_break=3
break_count=0

print("This program begun at:" + time.ctime())

while(break_count < total_break):
    time.sleep(0.3)
    webbrowser.open("https://www.jetbrains.com/help/pycharm/2017.1/creating-and-running-your-first-python-project.html")
    break_count=break_count+1
 