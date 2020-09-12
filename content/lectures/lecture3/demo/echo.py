# load Flask 
import flask
from googletrans import Translator

app = flask.Flask(__name__)


# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    # get the request parameters
    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, echo the msg parameter 
    if (params != None):
        translator = Translator()
        msg = params.get('msg')
        result = translator.translate(text=msg, src='en', dest='fr')
        data["response"] = msg
        data['translated'] = result.text
        data['language'] = result.dest
        data["success"] = True
        data['host_ip'] = flask.request.host
        data['remote_ip'] = flask.request.remote_addr

    # return a response in json format 
    return flask.jsonify(data)

# start the flask app, allow remote connections
app.run(debug=True, host="0.0.0.0")