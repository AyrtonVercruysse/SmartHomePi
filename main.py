from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
 return "Hello World!"

@app.route("/milight/on", methods=['PUT'])
def test():
 os.system("~/milight_binaries/milight on")
 return "Test succeeded"

@app.route("/milight/off", methods=['PUT'])
def test():
 os.system("~/milight_binaries/milight off")
 return "Test succeeded"




if __name__ == "__main__":

 app.run(host='0.0.0.0');