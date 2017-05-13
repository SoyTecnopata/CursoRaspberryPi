from gpiozero import CPUTemperature
from time import sleep, strftime,time
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import serial

arduino=serial.Serial('/dev/ttyACM0',9600)

cpu = CPUTemperature()
plt.ion()

x=[]
y=[]
z=[]
w=[]
a=[]

num1=0
num2=0
num3=0

def escrib_temp(data1,data2,data3,data4):
    with open("imprimir4Datos.csv","a") as log:
        log.write("{0},{1},{2},{3},{4}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(data1),str(data2),str(data3),str(data4)))

def graph(data1,data2,data3,data4):
    y.append(data1)
    z.append(data2)
    w.append(data3)
    a.append(data4)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.scatter(x,z)
    plt.scatter(x,w)
    plt.scatter(x,a)
    plt.plot(x,y)
    plt.plot(x,z)
    plt.plot(x,w)
    plt.plot(x,a)
    plt.draw()

def datos_Arduino():
    global num1
    global num2
    global num3
    linea=str(arduino.readline())
    print(linea)
    dividir=linea.split(",")
    #print("dividir")
    for i in range(len(dividir)):
            print(i,dividir[i])
            
    if(len(dividir)>4):
        num1=int(dividir[1])
        num2=int(dividir[2])
        num3=int(dividir[3])
    print(num1)
    print(num2)
    print(num3)

try:
    while 1:
        temp =cpu.temperature
        datos_Arduino()
        
        print(temp)
        print(num1)
        print(num2)
        print(num3)
        escrib_temp(temp,num1,num2,num3)
        graph(temp,num1,num2,num3)
        
        sleep(2)
    
except KeyboardInterrupt:
    plt.savefig('grafica4datos.jpg')
    plt.close()
    print("Stop")
