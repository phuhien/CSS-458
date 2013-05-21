import random

def displayTitle():
    
    print " inter  | arrival | service | TS begins | waiting | TS ends | Time in sys | Idle time"
    print ("----------------------------------------------------------------------------------------------------------") 
  
# generate random values 

def generateValue():
    return (random.randrange(1,101))

interArrival = [] # interarrival time
interArrival.append(0)
arrival = [] #arrival time
arrival.append(0)
service = [] # service time
service.append (25)
service_end = []
service_end.append(25)
service_begin = []
service_begin.append(0)
delay = [] # waiting time in the queue
delay.append(0)
sysTime = [] 
sysTime.append(25)         
idle = [] # idle time  
idle.append(0)



def interarrivalTime(number):
    #number = random.randrange(0,101)
    if (number >=0 and number <= 23):
        return 0
    elif (number >=24 and number <= 60):
        return 60
    elif (number >=61 and number <=88):
        return 2*60
    else:
        return 3*60

def generateIAT(step):
    for i in range(step):
        ranNum = random.randrange(0,101)
        result = interarrivalTime(ranNum)
        if(i>0):
            interArrival.append(result)

#generate the service time with standard deviation 8 mins, and mean 50 mins
def generateST(step):
    randomMeanST = random.randrange(0,11)

    for i in range(step):
        num = (random.randrange(25,75))
        if (randomMeanST != i):
            service.append(num)
        else:
            service.append(50)

def generateAT(num):
    for i in range(num):
        if (i>0):
            arrival.append(arrival[i-1] + interArrival[i])
            
                      
#simulation
def simulation(num):
    generateIAT(num)
    generateST(num)
    generateAT(num)
    
    #generate service_begin and serivce_end
    for i in range(num):
        if(i>0):
            if(arrival[i] >= service_end[i-1]):
                service_begin.append(arrival[i])
                service_end.append(service[i]+service_begin[i])
            else:
                service_begin.append(service_end[i-1])
                service_end.append(service[i]+service_begin[i])
                
    for i in range(num):
        if(i>0):
            
            if(arrival[i]<service_begin[i]):
                delay.append(service_begin[i] - arrival[i])
            else:
                delay.append(0)  
                
            sysTime.append(service[i] + delay[i])  
            idle.append(arrival[i] - service_end[i-1])
            
          
## result 
def displayTable( num):
    for i in range(num):
        print "  ",
        print str(interArrival[i]) + "\t", # print out interarrival time
        print "    "+str(arrival[i]) + "\t",  # print out arrival time
        print "     "+str(service[i])+ "\t",
        print "\t"+str(service_begin[i])+ "\t",
        print "     "+str(delay[i])+ "\t",  
        print "\t"+str(service_end[i])+ "\t",
        print "    "+str(sysTime[i])+ "\t",
        print "\t"+str(idle[i])+ "\t",
        print ""

delayAll = [] 
systemAll = []
maxAll = []
def allTrial(trial, num):
    
  for i in range (trial):
      
    print "Trial " + str(i+1)                
    print ("----------------------------------------------------------------------------------------------------------")  
    simulation(num)  
    displayTitle()
    displayTable(num)
    
    delayAll.append(sum(delay)/num)
    systemAll.append(sum(sysTime)/num)
    maxAll.append(max(sysTime))
  
    print "Average time in the queue: " + str(sum(delay)/num)
    print "Average processing time: " + str(sum(sysTime)/num)
    print "Maximum time in the system: "+ str(max(sysTime))
    print "\n"
 
  print ("----------------------------------------------------------------------------------------------------------")  
  print str(trial) + " trials result"
  print "Average time in the queue: "+ str(sum(delayAll)/trial)
  print "Average processing time: "+ str(sum(systemAll)/trial)
  print "Maximum time in the system: "+ str(max(maxAll))

  print ("----------------------------------------------------------------------------------------------------------")  


allTrial(1,10)   

