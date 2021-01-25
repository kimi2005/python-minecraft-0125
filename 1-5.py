# 1-5
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

i=0
while True:
    i=i+1
    mc.postToChat("第"+str(i)+"次")
    time.sleep(3)
                 