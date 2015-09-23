from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
 return "Hello World!"

@app.route("/milight/<zone>/on", methods=['PUT'])
def LEDon():
 os.system("~/milight_binaries/milight  {{zone}} on")
 return "Test succeeded"

@app.route("/milight/<zone>/off", methods=['PUT'])
def LEDoff():
 os.system("~/milight_binaries/milight {{zone}} off")
 return "Test succeeded"

@app.route("/milight/", methods=['PUT'])

@app.route("/milight/off", methods=['PUT'])

@app.route("/milight/off", methods=['PUT'])

@app.route("/milight/off", methods=['PUT'])





if __name__ == "__main__":

 app.run(host='0.0.0.0');