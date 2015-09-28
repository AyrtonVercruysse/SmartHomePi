from flask import Flask
import bottle
import os
app = Flask(__name__)

@app.route("/")
def hello():
 return "Hello World!"

@app.route("/milight/on/<zone>", methods=['PUT'])
def LEDon(zone):
 string = "~/milight_binaries/milight %s on" % zone
 os.system(string)
 return "Test succeeded"

@app.route("/milight/off/<zone>", methods=['PUT'])
def LEDoff(zone):
 string = "~/milight_binaries/milight %s off" %  zone
 os.system(string) 
 return "Test succeeded"

@app.route("/milight/white/<zone>", methods=['PUT'])
def LEDwhite(zone):
 string = "~/milight_binaries/milight %s white" %  zone
 os.system(string) 
 return "Test succeeded"

@app.route("/milight/disco/<zone>", methods=['PUT'])
def LEDdisco(zone):
 string = "~/milight_binaries/milight %s disco" %  zone
 os.system(string) 
 return "Test succeeded"

@app.route("/milight/disco/<zone>/<speed>", methods=['PUT'])
def LEDdiscospeed(zone, speed):
 string = "~/milight_binaries/milight %s disco %s" %  (zone, speed)
 os.system(string) 
 return "Test succeeded"

@app.route("/milight/brightness/<zone>/<value>", methods=['PUT'])
def LEDbrightness(zone, value):
 string = "~/milight_binaries/milight %s brightness %s" %  (zone, value)
 os.system(string) 
 return "Test succeeded"

@app.route("/milight/color/<zone>/<value>", methods=['PUT'])
def LEDcolor(zone, value):
 string = "~/milight_binaries/milight %s color %s" %  (zone, value)
 os.system(string) 
 return "Test succeeded"



if __name__ == "__main__":

 app.run(host='0.0.0.0');