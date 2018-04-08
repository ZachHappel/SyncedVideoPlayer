import pika
from datetime import datetime
import random
from collections import defaultdict

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


user = "Taylor"
group = 'PKA'

channel.queue_declare(queue=group)

def rand():
    list = [1.1,24.2,8.3,19.9,6.89,1.6,2.7,1.2,1.9,8.70,2.11,9.67,7.0]
    random1 = random.randint(0,12)
    return list[random1]

incoming = []
diffList = []
rawTimes = []
nameList = []
nameSize = []
finalTimes = {}
strictlyTimes = defaultdict(list)

def calcDiff(recieved, sent):
    print("This is recieved: "+recieved)
    print("This is sent: "+sent)
    print("This is recieved and sent 2:5: "+str(recieved[2:5]) +" "+str(sent[2:5]))

    if recieved[:2] != sent[:2]:
        pass

    if recieved[2:5] != sent[2:5]:                                          #REMOVE!!!#
        difSecond = int(int(recieved[6:12]) + (1000000 - int(sent[6:12]))) #+ (rand()*1000))

        print("a")
        print("DIFFERENCE: " + str(difSecond))
        return (difSecond)
    if recieved[2:5] == sent[2:5]:
        difSecond = int(recieved[6:12]) - int(sent[6:12])# + int(rand()*100000)

        print("b")
        print("DIFFERENCE: "+str(difSecond))
        return (difSecond)

                # Works





        ##


def calcAvg(y):
    added = 0
    for x in range(len(y)):
        print("Adding: "+str(y[x]))
        added+=y[x]
    avg = added/len(y)
    print("this is avg: "+str(avg))
    million = float(1000000)
    delay = (float(avg)/million)
    print("MATH; Added = %s, Len = %s" % (added, len(y)))
    return delay



x = 0
def callback(ch, method, properties, body):
    global x
    global diffList
    global incoming
    #if body[0].isalpha() == True:
    #    started = True
     #   return
    specificTime = str((datetime.now()))
    now = (specificTime[14:])
    #now = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    times = ("%s , R: " %body +str(now))
    #print("this is calc: "+str(calcDiff(str(now),str(body))))
    #diffList.append(calcDiff(str(now),str(body)))
    #print("This is Body: "+str(body))
    #print("This is Now: "+str(now))
    if times.isalpha() == True:
        strictlyTimes[times] = None
    else:
        rawTimes.append(times)

    print(str(now)[6:12])

    x+=1
    print("This is x:" +str(x))
    if x == 20:
        print('Done')
        #secondDelay = calcAvg(diffList)

        for l in range(len(rawTimes)):
            n = 0
            test = rawTimes[l]
            for y in range(len(test)):
                if test[y].isalpha() == True:
                    n+=1
                else:
                    consumer = (test[:n])
                    if consumer not in nameList and consumer.isalpha() == True:
                        nameList.append(consumer)
                    else:
                        pass
        #print("This is second delay: " +str(secondDelay))
        #print("This is average latency: "+ str(calcAvg(diffList)) +" seconds.")
        #print(incoming)
        print(rawTimes)
        print(nameList)

        #for m in range(nameList):


        #Uses name in the begining of each value in rawTimes to add to each seperate Key in the strictlyTimes dictionary
        for x in range(0, len(rawTimes)):
            for y in range(0, len(nameList)):
                nameToSearch = str(nameList[y])
                singleRawTime = str(rawTimes[x])
                finalTimes[nameToSearch] = None
                if nameToSearch in singleRawTime:
                    lenOfNamePlusOne = int(len(nameToSearch)+2)
                    strictlyTimes[nameToSearch].append(singleRawTime[lenOfNamePlusOne:])  # This is error, originally was .append(singleRawTime[7:])
                    #print(str(rawTimes[x]))
                else:
                    pass
        counter = ['a','b']
        def calcDiffN(dic):
            for x in range(len(dic)):
                print("1")
                oneList = (dic[dic.keys()[x]])
                name = dic.keys()[x]
                print("This is name: "+str(name))
                for goThroughTimes in range(len(oneList)):
                    timeToAdd = 0
                    timesCycled = 0
                    #(counter[x])
                    time = (oneList[goThroughTimes])
                    print(time)
                    sen = str(time[:12])
                    rec = str(time[18:])
                    print("This is recieved: " + rec)
                    print("THis is len of recieved: "+str(len(rec)))
                    print("This is sent: " + sen)
                    if len(rec) == 0:
                        pass
                    else:
                        print("Not Zero")
                        timesCycled +=1
                        timeToAdd +=int(calcDiff((rec), (sen)))

                        print("This is len times: "+str(finalTimes['Taylor']))
                        if goThroughTimes == len(oneList)-1 :
                                finalTimes[name] = (timeToAdd/timesCycled)

                        #print("this is calc diff ^")
        #def calcAll





        channel.stop_consuming()
        print("This is strictlyTimes: ")
        print(strictlyTimes)
        print("       space              ")
        calcDiffN(strictlyTimes)
        print("this is the length of dic:" +str(len(strictlyTimes)))
        print(finalTimes)


        return



channel.basic_consume(callback,
                      queue=group,
                      no_ack=True)




print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()




