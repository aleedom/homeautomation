import serial, time

ser = serial.Serial('/dev/ttyAMA0',9600, timeout=0, writeTimeout=0)
while True:
    #print("inwaiting: ", ser.inWaiting())
    if ser.inWaiting() >= 21:
        first = ord(ser.read(1))
        if first == 0x7e:
#            print("found packet start")
            lengthhi = ser.read(1)
            lengthlo = ser.read(1)
            frametype = ser.read(1)
            sourcemac = ser.read(8)
            mac = ""
            for i in sourcemac:
                mac += hex(ord(i))[2:]
            sourcenethi = ser.read(1)
            sourcenetlo = ser.read(1)
            junk = ser.read(5)
            volthi = ord(ser.read(1))
            voltlo = ord(ser.read(1))
            volt = voltlo+(volthi*256)
            tempc = ((volt/1023.*1.2 -.5)*100)
            tempf = round(tempc*(9/5.)+32,2)
            print("Temp: %.2f from: %s" %(tempf,mac))
    time.sleep(1)
