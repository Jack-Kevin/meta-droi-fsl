import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/pxk/info/<int:id>',methods=['GET'])
def get_info(id):
    if os.path.exists('/tmp/temp' + str(id)):
        with open('/tmp/temp' + str(id)) as files:
            data = json.load(files)
            info = {
                "id": id,
                "ip": data["ip"],
                "cpu_temp":data["cpu_temp"],
                "ap_temp": data["ap_temp"],
            }
    else:
        info = {
            "id":id,
            "ip": "not found",
            "cpu_temp":"not found",
            "ap_temp":"not found",
        }
    info_list = []
    info_list.append(info);

    return jsonify(data=info_list)

@app.route('/pxk/info/all',methods=['GET'])
def get_info_all():
    info_list = []
    for id in range(0,8):
        if os.path.exists('/tmp/temp' + str(id)) :
            with open('/tmp/temp' + str(id)) as files:
                data = json.load(files)
                info = {
                    "id": id,
                    "ip": data["ip"],
                    "cpu_temp":data["cpu_temp"],
                    "ap_temp": data["ap_temp"],
                }
        else:
            info = {
                "id": id,
                "ip": "not found",
                "cpu_temp":"not found",
                "ap_temp": "not found",
            }
        info_list.append(info)

    return jsonify(data=info_list)

@app.route('/pxk/setup_dhcp', methods=['POST'])
def setup_dhcp():
    #print request
    ip = request.form.get('ip')
    os.environ['ip'] = ip
    os.system('sh /etc/init.d/gen-dhcp.sh $ip &')
    return '2001'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True);
