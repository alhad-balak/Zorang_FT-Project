import requests,math


def dis(a,b):
    x1,y1 = a[0],a[1]
    x2,y2 = b[0], b[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#Retrieve data from given url
res = requests.get("https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json")
res = res.json() #Convert it into json

order = []
for i in res:
    order.append([i["latitude"],i["longitude"],i["_id"]])

#Stored the location of store
storex = 28.9428
storey=77.2276

#Applying Binary Search with implementation on minimum of maximum distance covered by delivery agents. variable 'mid refers as maximum distance can be travlled by all delivery agents.
l = 0
r = 10**10
agentdeliveries = []
while(l<=r):
    mid = (l+r)/2
    temporder = [[] for i in range(10)]
    def check(mid):
        tot = 0
        temp = []
        for i in order:
            temp.append(i)
        totdist = 0
        a, b = storex, storey
        while(tot<10 and len(temp)>0):
            dist = []
            index = 0
            for i,j,k in temp:
                dist.append([dis([i,j],[a,b]),i,j,k,index])
                index+=1
            dist.sort()
            totdist+=dist[0][0]
            finaldist = dis([storex,storey],[dist[0][1],dist[0][2]])
            if totdist+finaldist<=mid:
                a,b = dist[0][1],dist[0][2]
                temporder[tot].append(dist[0][3])
                temp.pop(dist[0][4])
            else:
                tot+=1
                totdist = 0
                a,b = storex,storey
        if len(temp)==0:
            return temporder
        else:
            return False
    if check(mid): #If delivery possible then it'll copy order of deliveries in array 'agentdeliveries'
        agentdeliveries = temporder.copy()
        r = mid-1
    else:
        l = mid+1

remaining = 0
for i in agentdeliveries:
    if len(i)==0:
        remaining+=1
l = []
for i in range(len(agentdeliveries)):
    if remaining==0:
        break
    while(len(agentdeliveries[i])>1 and remaining>0):
        l.append(agentdeliveries[i].pop())
        remaining-=1
for i in range(len(agentdeliveries)):
    if agentdeliveries[i]==[]:
        agentdeliveries[i].append(l.pop()) #Ensuring that every agents deliver at least one parcel.

print(agentdeliveries) #Printing the Order of deliveries

