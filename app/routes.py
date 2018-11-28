from flask import Flask,json,jsonify,request,make_response #MethodView,view_functions
from .model import Record
from app import creat_app

record_object=Record() #create a record object.


""" we name the app,(create an instance of flask)"""

app=creat_app()


@app.route('/')
def home():
    return 'You are welcome'

""" route for getting a record"""

@app.route('/api/v1/records', methods=['POST'])
def post_record():
    if request.method=='POST':
        
        result = request.data
        data=json.loads(result)
        record={
            'record_title':data['record_title'],
            'record_geolocation':data['record_geolocation']
            }


        if record['record_title']== '' or record['record_geolocation']=='':
            return ('fill in these fields'),400 #bad request
        
        else:

            new_record=record_object.add_record(record)
            return jsonify({'message':'record created successfully','record':new_record}),201


@app.route('/api/v1/records', methods=['GET'])
def return_all_orders():
    # if record_object.records==[]:
    #     return jsonify({'message':'This list is empty'}),204#no item found
    # else:
    list_of_orders=record_object.get_all_orders()
    return jsonify({'records':list_of_orders}),200