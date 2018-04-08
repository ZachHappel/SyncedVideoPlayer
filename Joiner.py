import pika
from datetime import datetime
import time
import random

def sendMessage():
    pass


user = "Kweb"
group = "PKA"


def rand():
    list = [.1,.2,.3,.4,.5,.6,.7,.8,.9,.10,.11,.12,.13]
    random1 = random.randint(0,12)
    return list[random1]



def joinGroup(groupname, username):

    x = 0
    testDone = False

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=str(groupname))


    print("Group You're Sending To: "+groupname)

    #Announce who joined   -- Taylor
    channel.basic_publish(exchange='',
                          routing_key=str(groupname),
                          body="%s" % username)
    while x < 50:
        #send 100 messages with the times
        specificTime = str((datetime.now()))
        now = (specificTime[14:])
        #now = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        channel.basic_publish(exchange='',
                          routing_key=str(groupname),
                          body='%s: %s'%(username,now))

        print('Sent at: %s' % now)
        x+=1
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
    else:
        pass



joinGroup(group, user)


