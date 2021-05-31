import asyncio
import time

#Coroutine Example
async def debugmsg(msg):
    print("Debug msg is {}".format(msg))
    msg = msg + ' domything'
    #time.sleep(0.2) #blocking call
    await asyncio.sleep(0.2)
    print("Debug msg is {}".format(msg))

async def senddebugmsgs():
    t1 = time.time()
    await debugmsg('i am log1')
    await debugmsg('i am log2')
    t2 = time.time()
    print(t2-t1)

#asyncio.run(senddebugmsgs(), debug=True)

################################################
#Task example
#################################################
