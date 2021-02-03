import paho.mqtt.client as mqtt
message = ''
def on_connect(client, userdata, flags, rc):
    connstatus = str(rc)
    print("Connected with result code "+str(rc))
    client.subscribe("Node_Data")

def on_message(client, userdata, msg):
    message1 = msg.payload.decode()
    global message
    message = message1
    #f = open('test.txt','w')
    #print(message1)
    #f.write(message1)
    #f.close()
    
client = mqtt.Client()
#f = open('test.txt','w')
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()
