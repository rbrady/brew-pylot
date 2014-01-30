#!/usr/bin/env python
# This is a sample service used for prototyping
# This file will be replaced in the near future
# Don't rely on this being here too long
from flask import request, Flask
from flask.ext.restful import abort, Resource, Api
import envoy
import os

app = Flask(__name__)
api = Api(app)
ROOT_DEVICE_DIR = '/sys/bus/w1/devices'

def get_thermometers():
	r = envoy.run('ls %s' % ROOT_DEVICE_DIR)
	therms = [therm for therm in r.std_out.split('\n') if len(therm) > 0]
	return therms

class Thermometer(Resource):
	def get(self, therm_id):
		format=request.args.get('format', 'raw')
		f=open(os.path.join(ROOT_DEVICE_DIR,therm_id,'w1_slave'), 'r')
		result=f.readlines()
		f.close()
		if "YES" in result[0]:
			#return {'raw': result[1].replace('\n', '').split('t=')[1]}
			raw=result[1].replace('\n', '').split('t=')[1]
			if 'f' in format:
				return {'farenheight': ((raw / 1000.0) * 1.8000) + 32.00}
			elif 'c' in format:
				return {'celsius': raw / 1000.00}
			else:
				return {'raw': raw}

	        else:
		    abort(500, "Thermometer not found")


class Thermometers(Resource):
    def get(self):
        return get_thermometers()

class Power120(Resource):
	def get(self):
		return {'TODO': 'Implement this for managing the pump(s)'}

class Power240(Resource):
	def get(self):
		return {'TODO': 'Implement this for managing the heating element(s)'}

api.add_resource(Thermometers, '/thermometers')
api.add_resource(Thermometer, '/thermometers/<string:therm_id>')
api.add_resource(Power120, '/powered')
api.add_resource(Power240, '/high-powered')

if __name__ == "__main__":
    app.run(debug=True)
