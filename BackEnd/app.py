from flask import Flask
from flask_cors import CORS
from flask.globals import request
#from Position_DAO import Position_DAO
from instances import position_handler
app = Flask(__name__)
CORS(app)
#Positions initialization
position_handler.new_position(1,-1,"free","off","off")
position_handler.new_position(2,-1,"free","off","off")
position_handler.new_position(3,-1,"free","off","off")
position_handler.new_position(4,-1,"free","off","off")
position_handler.new_position(5,-1,"free","off","off")
position_handler.new_position(6,-1,"free","off","off")
position_handler.new_position(7,-1,"free","off","off")
position_handler.new_position(8,-1,"free","off","off")
position_handler.new_position(9,-1,"free","off","off")
position_handler.new_position(10,-1,"free","off","off")
position_handler.new_position(11,-1,"free","off","off")
position_handler.new_position(12,-1,"free","off","off")
position_handler.new_position(13,-1,"free","off","off")
position_handler.new_position(14,-1,"free","off","off")
position_handler.new_position(15,-1,"free","off","off")
position_handler.new_position(16,-1,"free","off","off")
position_handler.new_position(17,-1,"free","off","off")
position_handler.new_position(18,-1,"free","off","off")
position_handler.new_position(19,-1,"free","off","off")
position_handler.new_position(20,-1,"free","off","off")
position_handler.new_position(21,-1,"free","off","off")
position_handler.new_position(22,-1,"free","off","off")
position_handler.new_position(23,-1,"free","off","off")
position_handler.new_position(24,-1,"free","off","off")
position_handler.new_position(25,-1,"free","off","off")
position_handler.new_position(26,-1,"free","off","off")
position_handler.new_position(27,-1,"free","off","off")
position_handler.new_position(28,-1,"free","off","off")
position_handler.new_position(29,-1,"free","off","off")
position_handler.new_position(30,-1,"free","off","off")
position_handler.new_position(31,-1,"free","off","off")
position_handler.new_position(32,-1,"free","off","off")


@app.route("/")
def index():
    return "<h1>Ruta Principal 14k</h1>"


@app.route('/set-reserved/<id>',methods=['POST'])
def reserved(id):
    response={}
    user=request.json['user']
    position_handler.set_parking_reserved(int(id.split("=")[1]),int(user))
    return response

@app.route('/set-occupied/<id>',methods=['POST'])
def occupied(id):
    response={}
    user=request.json['user']
    position_handler.set_parking_occupied(int(id.split("=")[1]),int(user))
    return response

@app.route('/decline-reserved/<id>',methods=['POST'])
def decline(id):
    response={}
    user=request.json['user']
    position_handler.set_parking_free_by_reserved(id,int(user))
    return response

@app.route('/accept-reserved/<id>',methods=['POST'])
def accept(id):
    response={}
    user=request.json['user']
    position_handler.set_parking_occupied_by_reserved(id,int(user))
    return response
        

@app.route('/get-level-01',methods=['GET'])
def level_one():
    return "{"+position_handler.return_level_one().replace("[","{").replace("]","}").replace("{","").replace("}","")+"}"

@app.route('/get-level-02',methods=['GET'])
def level_two():
    return "{"+position_handler.return_level_two().replace("[","{").replace("]","}").replace("{","").replace("}","")+"}"

@app.route('/analytics',methods=['GET'])
def analytics():
    return position_handler.return_parking_stats()

@app.route('/refresh',methods=['GET'])
def refresh():
    return position_handler.return_parking_stats()

@app.route('/alarm-stats/<user>',methods=['GET'])
def alarm(user):
    return position_handler.return_alarm_analytics(int(user))

@app.route('/alarm-off',methods=['POST'])
def off():
    response={}
    user=request.json['user']
    position_handler.turn_off_the_alarm(int(user))
    return response

@app.route('/alarm-on',methods=['POST'])
def on():
    response={}
    user=request.json['user']
    position_handler.turn_on_the_alarm(int(user))
    return response

@app.route('/change-parking-proteus',methods=['POST'])
def change_parking_in_proteus():
    response={}
    id=request.json['id']
    position_handler.verify_parking_change_in_proteus(int(id))
    return response

@app.route('/get-all-reserved',methods=['GET'])
def get_reserveds():
    return position_handler.return_all_reserveds()



if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True, host='0.0.0.0')