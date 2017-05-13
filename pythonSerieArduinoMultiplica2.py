import serial
import time

arduino=serial.Serial('/dev/ttyACM0',9600)
try:
    num1=str(input("Escribe el primer numero para que arduino multiplique "))
    num2=str(input("Ahora otro numero "))
    
    print("Enviar numeros")
    print(num1)
    print(num2)
    arduino.write('N')
    arduino.write(num1)
    arduino.write(',')
    arduino.write(num2)
    time.sleep(0.5)
    linea=int(arduino.readline())
    print("la multiplicacion: ",num1, " x ",num2, " = ",linea);
    time.sleep(2)
except KeyboardInterrupt:
    arduino.close()
