from constants import PORT
from flask import Flask, request, make_response , render_template
import json 
import os 
from flask_cors import cross_origin
# from SolarSystemAPI import *
from SolarSystemDataBase import SolarSystemRepository
import logger_config
from logger_config import *
from termcolor import colored
from backend_process import processRequest

#---Configuring log filename---
log_file=os.path.splitext(os.path.basename(__file__))[0]+".log"
log = logger_config.configure_logger('default', ""+DIR+""+LOG_DIR+"/"+log_file+"")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/webhook', methods=['POST','GET'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    # print("request: ", req)
    # print(json.dumps(req,indent=3))

    res = processRequest(req)
    log.info(colored("Bot replied: "+str(res), 'green'))
    res = json.dumps(res,indent=4)
    r = make_response(res)
    # print(r.text)
    r.headers['Content-Type'] = 'application/json'
    # print("returning response:---",r)
    return r


if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    # print("Starting app on port %d"% port)
    app.run(threaded=True,port=port, host="0.0.0.0", debug=True)
    # app.run(threaded=True)