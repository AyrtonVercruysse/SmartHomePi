from flask import Flask
import bottle
import os
app = Flask(__name__)

@app.route("/")
def hello():
 return "Hello World!"

@app.route("/milight/on/<zone>", methods=['PUT'])
def LEDon():
 os.system("~/milight_binaries/milight  {{zone}} on")
 return "Test succeeded"

@app.route("/milight/off/<zone>", methods=['PUT'])
def LEDoff():
 os.system("~/milight_binaries/milight {{zone}} off")
 return "Test succeeded"

if __name__ == "__main__":

 app.run(host='0.0.0.0');