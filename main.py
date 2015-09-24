from flask import Flask
import bottle
import os
app = Flask(__name__)

@app.route("/")
def hello():
 return "Hello World!"

@app.route("/milight/on/<zone>", methods=['PUT'])
def LEDon(zone):
 os.system("~/milight_binaries/milight  0 on")
 return "Test succeeded"

@app.route("/milight/off/<zone>", methods=['PUT'])
def LEDoff(zone):
 os.system("~/milight_binaries/milight " {{zone}} " off")
 return "Test succeeded"

if __name__ == "__main__":

 app.run(host='0.0.0.0');