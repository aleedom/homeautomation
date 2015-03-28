import json, datetime, requests, ast, fnmatch
import os, time
from w1_therm import w1_therm
#endpoints
#.../tempsensor				get/post
#.../tempsensor/(serial#)	get/put/delete
#.../temperature/(serial#)	get/post
base_url = "http://192.168.1.131:9000/api/"
device_dir = '/sys/bus/w1/devices/'
headers = {'content-type': 'application/json'}
def addtodb(sensor):
	url = base_url+"tempsensor"
	payload = {}
	payload['serial'] = sensor
	return requests.post(url, data=json.dumps(payload), headers = headers)

def updatedbstatus(sensor, status):
	url = base_url+"tempsensor/"+sensor
	payload = {'serial':sensor,'active':status}
	return requests.put(url, data=json.dumps(payload), headers = headers)
#get attatched sensors
atsensors = []
for filename in os.listdir("/sys/bus/w1/devices"):
	if fnmatch.fnmatch(filename, '28-*'):
		atsensors.append(filename)
print("active sensors: ",atsensors)

#get current devices in database
r = requests.get(base_url+"tempsensor")
temp = json.dumps(r.json())
temp = temp.replace('true','True')
temp = temp.replace('false','False')
dict_list = ast.literal_eval(temp)
dbsensors = {}

#transform database data into proper form of {"serial":"status"}
for dict in dict_list:
	dbsensors[dict['serial']] = dict['active']
print("List of sensors in database: ", dbsensors)
changelist = {}
for sensor in atsensors:
	if sensor in dbsensors: 
		if dbsensors[sensor] == False:
			updatedbstatus(sensor,True)
			changelist[sensor] = "update status from False to True"
	elif sensor not in dbsensors:
		addtodb(sensor)
		changelist[sensor] = "add to database"

for sensor in dbsensors:
	if dbsensors[sensor] == True:
		if sensor not in atsensors:
			updatedbstatus(sensor,False)
			changelist[sensor] = "update status from True to False"
print("List of changes: ",changelist)


#read temperature sensors 
for sensor in atsensors:
	sobj = w1_therm(sensor)
	temp = sobj.get_temp_f()[0]
	url = base_url+"temperature/"+sensor
	payload = {'serial':sensor, 'temperature':round(temp,3), 'timestamp':str(datetime.datetime.now())} 
	r = requests.post(url, data=json.dumps(payload), headers=headers)

#new temperature 
#url = "http://192.168.1.14:9000/api/temperature/28-0215684fd5ff"
#payload = {'serial': '28-0214684fd5ff', 'temperature': 123.456, 'timestamp': str(datetime.datetime.now())}
#headers = {'content-type': 'application/json'}
#print(payload)
#r = requests.post(url, data=json.dumps(payload), headers=headers)
#print(r.response)

#r = requests.delete(url+"/28-0214684fd5ff")
#print(r.status_code)
