#!/usr/bin/env python
from flask import Flask
from flask.ext.restful import abort, Resource, Api
import envoy

app = Flask(__name__)
api = Api(app)
ROOT_DEVICE_DIR = '/sys/bus/w1/devices'

def get_thermometers():
	r = envoy.run('ls %s' % ROOT_DEVICE_DIR)
	therms = [therm for therm in r.std_out.split('\n') if len(therm) > 0]
	return therms

class Thermometer(Resource):
	def get(self, therm_id):
		f=open(os.path.join(ROOT_DEVICE_DIR,therm_id), 'r')
		result=f.readlines()
		f.close()
		if "YES" in result[0]:
			return {'raw': result[1].replace('\n', '').split('t=')[1]}
	        else:
		    abort(500, "Thermometer not found")


class Thermometers(Resource):
    def get(self):
        return get_thermometers()

api.add_resource(Thermometers, '/thermometers')
api.add_resource(Thermometer, '/thermometers/<string:therm_id>')

if __name__ == "__main__":
    app.run(debug=True)
