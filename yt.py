import webbrowser
import time
yt = ("")
def makeytlink():
    import random
    ytcharacters = ("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm-_")
    k=("")
    i=("")
    j=("")
    for _ in range(11):
        k = ( k + random.choice(ytcharacters) )
        print (k)
        yt = k
    url = "https://www.youtube.com/watch?v=" + k
    browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(browser)
    webbrowser.open(url) 
while ( 1 == 1 ):
    inp = input("press enter to generate a new yt link")
    makeytlink()