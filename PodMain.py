from selenium import webdriver
import time
from Tkinter import *
import Tkinter
from collections import defaultdict
import sys
import socket
import select
import pika
from datetime import datetime
import random




#Remove when site runs server ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rand():
    list = [1.1, 24.2, 8.3, 19.9, 6.89, 1.6, 2.7, 1.2, 1.9, 8.70, 2.11, 9.67, 7.0]
    random1 = random.randint(0, 12)
    return list[random1]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def createGroup(name):
    global amount
    x = 0
    incoming = []

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    user = ""
    group = name

    channel.queue_declare(queue=group)

    dictTimes = {}

    for x in range(0, amount):
        dictTimes['%s' % x] = ''


    def calcDiff(recieved, sent):
        print("This is recieved and sent 2;5: " + str(recieved[2:5]) + " " + str(sent[2:5]))
        if recieved[:2] != sent[:2]:
            pass

        if recieved[2:5] != sent[2:5]:  # REMOVE!!!#
            difSecond = int(recieved[6:12]) + (1000000 - int(sent[6:12])) + (rand() * 1000)

            print("a")
            return (difSecond)
        if recieved[2:5] == sent[2:5]:
            difSecond = int(recieved[6:12]) - int(sent[6:12]) + int(rand() * 100000)

            print("b")
            return (difSecond)




    def calcAvg(y):
        added = 0
        for x in range(len(y)):
            print("Adding: " + str(y[x]))
            added += y[x]
        avg = added / len(y)
        print("this is avg: " + str(avg))
        million = float(1000000)
        delay = (float(avg) / million)
        print("MATH; Added = %s, Len = %s" % (added, len(y)))
        return delay


    def callback(ch, method, properties, body):
        diffList = []
        global incoming
        if body[0].isalpha() == True:
            print(str(body))
            started = True
            return
        specificTime = str((datetime.now()))
        now = (specificTime[14:])
        # now = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        times = (" [x] Received @ %s | Sent @ " % now + str(body))
        # print("this is calc: "+str(calcDiff(str(now),str(body))))
        diffList.append(calcDiff(str(now), str(body)))
        print(times)
        print(str(now)[6:12])

        x+=1
        print("This is x:" + str(x))
        if x == 14:
            print('Done')
            secondDelay = calcAvg(diffList)
            print("This is second delay: " + str(secondDelay))
            # print("This is average latency: "+ str(calcAvg(diffList)) +" seconds.")
            # print(incoming)
            channel.stop_consuming()
            return
    print("tf")
    channel.basic_consume(callback,
                          queue=group,
                          no_ack=True)

    print("!!!")
    channel.start_consuming()






def joinGroup(groupname, username):
    x = 0
    testDone = False

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=str(groupname))

    print("Group You're Sending To: " + groupname)

    # Announce who joined   -- Taylor
    channel.basic_publish(exchange='',
                          routing_key=str(groupname),
                          body="%s." % username)
    while x < 50:
        # send 100 messages with the times
        specificTime = str((datetime.now()))
        now = (specificTime[14:])
        # now = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        channel.basic_publish(exchange='',
                              routing_key=str(groupname),
                              body='%s' % now)

        print('Sent at: %s' % now)
        x += 1
        time.sleep(rand())

    if x == 50:
        testDone = True
        channel.basic_publish(exchange='',
                              routing_key=str(groupname),
                              body='Done')
        return
    else:
        pass

    if testDone == True:
        connection.close()
        firstwindow()
    else:
        pass





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

top = Tk()

term = StringVar()
url = StringVar()

size = StringVar()

groupSize = 0
whichBrowser = None

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def browserChrome():
    global whichBrowser
    whichBrowser = "Chrome"

def browserFirefox():
    global whichBrowser
    whichBrowser = "Firefox"

def browserSafari():
    global whichBrowser
    whichBrowser = "Safari"

def browserIE():
    global whichBrowser
    whichBrowser = "IE"

def openlink(url):
    ff = webdriver.Chrome()
    ff.get(url)
    ff.execute_script('document.getElementsByTagName("video")[0].pause()')
    time.sleep(3)

def loadBrowsers():
    pass

def playVideo():
    pass

def pauseVideo():
    pass

def restartVideo():
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#top = Tk()

term = StringVar()
url = StringVar()
size = StringVar()
createPressed = False
groupSize = 0
whichBrowser = None

def browserChrome():
    global whichBrowser
    whichBrowser = "Chrome"

def browserFirefox():
    global whichBrowser
    whichBrowser = "Firefox"

def browserSafari():
    global whichBrowser
    whichBrowser = "Safari"

def browserIE():
    global whichBrowser
    whichBrowser = "IE"

def openlink(url):
    ff = webdriver.Chrome()
    ff.get(url)
    ff.execute_script('document.getElementsByTagName("video")[0].pause()')
    time.sleep(3)

def loadBrowsers():
    pass

def playVideo():
    pass

def pauseVideo():
    pass

def restartVideo():
    pass

def groupnumber(num):
    global groupSize
    groupSize = int(num)


def firstwindow():
    canvas = Tkinter.Canvas(top, height=50, width=0)

    labelfont = ('times', 20, 'bold')
    widget = Label(top, text='Synced Video Player')
    widget.config(bg='white', fg='black')
    widget.config(font=labelfont)
    widget.config(height=10, width=20)
    #widget.pack(expand=YES, fill=BOTH)
    addbutton = Tkinter.Button(top, text="Create Group", command = createWindow)
    addbutton.pack(side=LEFT)
    addbutton1 = Tkinter.Button(top, text="Join Group", command = joinWindow)
    addbutton1.pack(side=LEFT)
    canvas.pack()

def joinWindow():
    myName = StringVar()
    group2Join = StringVar()

    joinW = Tk()
    joinCanvas = Tkinter.Canvas(joinW, height=10, width=10)
    joinL1 = Label(joinW, text="Group Name:")
    joinE1 = Entry(joinW, textvariable = group2Join)
    joinMyNameLabel = Label(joinW, text="Your Name:")
    joinMyNameEntry = Entry(joinW, textvariable=myName)

    joinL1.pack()
    joinE1.pack()
    joinMyNameLabel.pack()
    joinMyNameEntry.pack()
    joinGroupName = joinE1.get()
    joinGroupMyName = joinMyNameEntry.get()


    def joinPress():

        print(str(joinE1.get()),joinMyNameEntry.get())
        #print(str(joinGroup(joinE1.get(), joinMyNameEntry.get())))
        joinGroup(str(joinE1.get()), str(joinMyNameEntry.get()))


    joinButton = Tkinter.Button(joinW, text="Join", command=joinPress)
    joinButton.pack()
    joinCanvas.pack()
    joinW.mainloop()




def createWindow():
    global createPressed
    global groupSize
    peopleJoining = True
    checking = True
    bottom = Tk()
    canvascreate = Tkinter.Canvas(bottom, height=10, width=10)
    L1 = Label(bottom, text="Group Name:")
    E1 = Entry(bottom, bd=5, textvariable=term)

    howmanyLabel = Label(bottom, text="How many in group?")
    howmany = Entry(bottom, text="How many in group?", textvariable = size)



    def groupWindow():
        global amount
        global groupSize
        howmanyLabel.pack_forget()
        howmany.pack_forget()
        L1.pack_forget()
        E1.pack_forget()
        makeBtn.pack_forget()
        groupName = (E1.get())
        createGroup(groupName)
        groupNameLabel = Label(bottom, text=groupName)
        #calcLatency(groupName)
        amount = int(howmany.get())
        print("this is amount:"+str(amount))

        #waitLabel = Label(bottom, text = "Please wait while everyone joins and their latency is calculated for "+str(groupSize))

        numbofPeople = Label(bottom, text = "Current Size of Group: "+str(groupSize))
        groupNameLabel.pack()
        numbofPeople.pack()
        browser = Menubutton(bottom, text="Browser", relief=RAISED)
        browser.grid()
        browser.menu = Menu(browser, tearoff=0)
        browser["menu"] = browser.menu
        browser.menu.add_checkbutton(label="Chrome",
                                     command=browserChrome)
        browser.menu.add_checkbutton(label="Firefox",
                                     command=browserFirefox)
        browser.menu.add_checkbutton(label="Safari",
                                     command=browserSafari)
        browser.menu.add_checkbutton(label="IE",
                                     command=browserIE)
        browser.pack()
        blankSpace = Label(bottom, text = "        ")
        blankSpace2 = Label(bottom, text="                                             ")
        pleaseWait = Label(bottom, text="Please wait until everyone joins.")
        urlLabel = Label(bottom, text = "Url:")
        linkEntry = Entry(bottom, textvariable = url)
        blankSpace.pack()
        urlLabel.pack()
        linkEntry.pack()

        def openControls():
            controlwindow = Tk()
            #playIcon = ImageTk.PhotoImage(file="play.png")
            #pauseIcon = ImageTk.PhotoImage(file = "pause.png")
            #restartIcon = ImageTk.PhotoImage(file = "restart.png")
            def checkGroupSize():
                waitLabel = Label(controlwindow,
                                  text="Please wait while everyone joins and their latency is accounted for.")
                global amount
                global groupSize
                if amount != groupSize:
                    waitLabel.pack()
                elif amount == groupSize:
                    waitLabel.pack_forget()
                    pass  #### Add play!

            controlCreate = Tkinter.Canvas(controlwindow, height=10, width=10)
            playButton = Tkinter.Button(controlwindow, text ="Play", command = checkGroupSize)
            pauseButton = Tkinter.Button(controlwindow, text = "Pause",command = pauseVideo)
            restartButton = Tkinter.Button(controlwindow, text = "Restart",command=restartVideo)
            #playButton.config(image=playIcon)
            #pauseButton.config(image=pauseIcon)
            #restartButton.config(image=restartIcon)
            #playButton.image = playIcon
            #pauseButton.image = pauseIcon
            #restartButton.image = restartButton
            playButton.pack(side = LEFT)
            pauseButton.pack(side = LEFT)
            restartButton.pack(side = RIGHT)
            controlCreate.pack()







        loadVideo = Tkinter.Button(bottom, text ="Load Video", command = loadBrowsers)
        controlButton = Tkinter.Button(bottom, text ="Open Controls", command = openControls)
        loadVideo.pack(side = LEFT)
        controlButton.pack(side = RIGHT)
        blankSpace2.pack()
        pleaseWait.pack()
        bottom.mainloop()
        createGroup(str(groupName))


    makeBtn = Tkinter.Button(bottom, text="Create Group Server and Join", command= groupWindow) #### fix
    L1.pack()
    E1.pack()
    howmanyLabel.pack()
    howmany.pack()

    makeBtn.pack()
    canvascreate.pack()
    bottom.mainloop()













firstwindow()
#ff.save_screenshot("/Users/python/Documents/Podcast/ENV/webpage.png")
top.mainloop()