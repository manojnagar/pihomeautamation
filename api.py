from flask import Flask,request
from read import readPort, readPorts, setPortOutput
from flask_restful import  reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# Define port in PI board
PORTS = [18, 19]
StatusList = [0, 1]

def abort_if_port_doesnt_exist(port_id):
    if port_id not in PORTS:
        abort(404, message="Port {} dosn't exist ".format(port_id))

def abort_if_invalid_status(status):
    if status not in StatusList:
        abort(404, message="Status {} dosn't exist ".format(status))

parser = reqparse.RequestParser()

class Home(Resource):
    def get(self):
        return {'message': 'Welcome to Home Automation'}

class GPIO(Resource):
    def get(self, port_id):
        abort_if_port_doesnt_exist(port_id)
        return readPort(port_id), 200
    
    def put(self, port_id):
        abort_if_port_doesnt_exist(port_id)
        data = request.get_json()
        status = data["status"]
        abort_if_invalid_status(status)
        setPortOutput(port_id, status)
        return readPort(port_id), 201

class GPIOList(Resource):
    def get(self):
        return readPorts(PORTS), 200
    
    def post(self):
        data = request.get_json()
        port_id = data["port"]
        status = data["status"]
        abort_if_port_doesnt_exist(port_id)
        abort_if_invalid_status(status)
        setPortOutput(port_id, status)
        return readPort(port_id), 201

api.add_resource(GPIOList,  '/gpio')        
api.add_resource(GPIO,  '/gpio/<int:port_id>')    
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
