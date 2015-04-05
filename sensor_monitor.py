import json, datetime, requests, ast, fnmatch
import os, serial, time
#endpoints
#.../tempsensor				get/post
#.../tempsensor/(serial#)	get/put/delete
#.../temperature/(serial#)	get/post
base_url = "http://192.168.1.122:8000/api/"
headers = {'content-type': 'application/json'}
ser = serial.Serial('/dev/ttyAmA0',9600, timeout=0, writeTimeout=0)

def addsensortodb(sensor):
	url = base_url+"sensors"
	payload = {}
	payload['serial'] = sensor
	return requests.post(url, data=json.dumps(payload), headers = headers)

def addtemptodb(serial, temp):
    #only add data to database if the sensor we got data from is associated with a room
    
    #check if sensor is in a room
    url = base_url+"sensors/"+serial
    r = requests.get(url)
    tmp = json.dumps(r.json())


    url = base_url+"temperature/"+serial
    payload = {'serial':serial, 'temperature':round(temp,3), 'timestamp':str(datetime.datetime.now())}
    r = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}


#get current devices in database
r = requests.get(base_url+"sensors")
temp = json.dumps(r.json())
dict_list = ast.literal_eval(temp)
dbsensors = []
for dict in dict_list:
    dbsensors.append(dict['serial'])
print("Sensors in database: ",dbsensors)


#xbee read push loop
while True:
    #wait until full packet(dont know why 21 bytes)
    if ser.inWaiting() >= 21:
        #ord() converts a char byte into int()
        firstbyte = ord(ser.read(1))
        #value packets start with 0x7e
        if firstbyte == 0x7e:
            lengthhi = ser.read(1)
            lengthlo = ser.read(1)
            frametype = ser.read(1)
            sourcemac = ser.read(8)
            serialnum = ""
            for i in sourcemac:
                serialnum += hex(ord(i))[2:]

            if serialnum not in dbsensors:
                addsensortodb(serialnum)
                print("added %s to databse" %serialnum)

            sourceethi = ser.read(1)
            sourcenetlo = ser.read(1)a
            junk = ser.read(5)
            volthi = ord(ser.read(1))
            voltlo = ord(ser.read(1))
            volt = voltlo+(volthi(*256)
            tempc = ((volt/1023.*1.2 -.5)*100)
            tempf = tempc*(9/5.)+32
            addtemptodb(serialnum, tempf)

