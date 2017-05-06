from gpiozero import CPUTemperature
from time import sleep, strftime,time
import csv
import matplotlib.pyplot as plt

cpu = CPUTemperature()
plt.ion()
x=[]
y=[]

def escrib_temp(temp):
    with open("cpu_temp.csv","a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))


def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()

while True:
    try:
        temp =cpu.temperature
        escrib_temp(temp)
        graph(temp)
        sleep(2)
    
    except KeyboardInterrupt:
        print("Stop")
