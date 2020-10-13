#######################################
#  ATTENTION: Do not touch this file  #
#######################################
import json
from flask import Flask, request
from gevent.pywsgi import WSGIServer
from gevent import monkey
from Src.Controllers.consciousnessController import ConsciousnessController

app = Flask(__name__)
app.register_blueprint(ConsciousnessController)

serverPort=3000
hostname='0.0.0.0'

def main():
    http = WSGIServer((hostname, serverPort), app.wsgi_app )

    print("Server started %s" % (str(http.address)))

    # Serve your application
    http.serve_forever()

if __name__ == "__main__":
    main()

