from flask import Flask,json,jsonify,make_response,request
from random import randint





class Record:
    records=[]

    def   add_record(self,record):#record is the new redflag being created.
        """creating fields that will be returned automatically"""
        record['record_no']= int(len(self.records) + 1 )
        record['record_type']= 'Redflag_record'
        return  record


    def    get_all_orders(self):
        return (self.records),200

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    data=request.json
    records1={'record_title':data.get('record_title'),'record_type':data.get('record_type'),'record_geoloc':data.get('record_geoloc'),'record_no':data.get('record_no')}
    records.append(records1)
    return jsonify({'records':records}),201
"""


"""
if len(records)==0:
        record_no=1
        records={'record_title':request.json['record_title'],'record_type':request.json['record_type'],'record_geoloc':request.json['record_geoloc'],'record_no':record_no}

    if len(records)==0:
        record_no=1

    else:
        item=records[len(records)-1]
        t=int(item(['record_no']))
        new_record=t+1
        records={'record_title':request.json.get['record_title'],'record_type':request.json.get['record_type'],'record_geoloc':request.json['record_geoloc'],'record_no':new_record}
"""