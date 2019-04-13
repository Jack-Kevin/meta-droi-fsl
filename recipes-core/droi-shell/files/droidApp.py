import os
from flask import Flask, jsonify, request
import json
import numpy as np
import re


VOL_RAW = '/sys/bus/iio/devices/iio:device0/in_voltage8_raw'
VOL_SCALE = '/sys/bus/iio/devices/iio:device0/in_voltage_scale'

resistance_array = np.array([1787.9797,1679.6017,1578.5061,1484.1584,1396.0662,1313.7754
,1236.8685,1164.9598,1097.6941,1034.7432,975.8038,920.5962,868.8615,820.3603
,774.871,732.1889,692.1238,654.4999,619.154,585.9346,554.7016,525.3245,497.6821,471.6621
,447.1599,424.0781,402.3264,381.8204,362.4818,344.2375,327.0195,310.764,295.4121
,280.9084,267.2014,254.2428,241.9877,230.394,219.4224,209.0361,199.2007,189.8841
,181.0559,172.6881,164.754,157.229,150.0898,143.3144,136.8825,130.7749,124.9734
,119.4612,114.2223,109.2417,104.5053,100,95.7132,91.6333,87.7492,84.0505,80.5274,77.1707
,73.9717,70.9222,68.0144,65.2411,62.5954,60.0707,57.661,55.3604,53.1635,51.0651
,49.0602,47.1443,45.313,43.5621,41.8878,40.2862,38.7539,37.2876,35.8842,34.5405
,33.2538,32.0214,30.8408,29.7096,28.6253,27.586,26.5895,25.6338,24.7171,23.8376,22.9937
,22.1836,21.4061,20.6594,19.9424,19.2537,18.592,17.9562,17.3452,16.7578,16.193
,15.6499,15.1276,14.6251,14.1417,13.6764,13.2286,12.7976,12.3825,11.9828,11.5978
,11.227,10.8697,10.5254,10.1935,9.8736,9.5652,9.2678,8.9809,8.7042,8.4373
,8.1797,7.9312,7.6912,7.4596,7.236,7.0201,6.8115,6.6101,6.4155,6.2274,6.0457,5.8701
,5.7003,5.5362,5.3775,5.224,5.0755,4.9319,4.793,4.6586,4.5285,4.4026,4.2807,4.1627
,4.0484,3.9378,3.8306,3.7268,3.6263,3.5289,3.4345,3.343,3.2543,3.1683,3.085
,3.0042,2.9258,2.8498,2.7761,2.7045,2.6352,2.5678,2.5025,2.4391,2.3775,2.3178
,2.2598,2.2034,2.1487,2.0956,2.044,1.9939,1.9452,1.8978,1.8518,1.8071,1.7637,1.7215,1.6804,1.6405
])

temp_array = np.array([
-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,
-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,
59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,
78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,
97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,
112,113,114,115,116,117,118,119,120,121,122,123,124,125,
126,127,128,129,130,131,132,133,134,135,136,137,138,139,
140,141,142,143,144,145,146,147,148,149,150,151,152,153,
154,155,156,157,158,159,160,161,162,163,164,165,166,167,
168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,
183,184,185,186,187,188,189,190,191,192,193,194,195,196,
197,198,199,200,
])

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx #array[idx]

def isvalidmac(mac):
    if re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", mac):
        return True
    return False

app = Flask(__name__)

@app.route('/pxk/info/<int:id>',methods=['GET'])
def get_info(id):
    if os.path.exists('/tmp/temp' + str(id)):
        with open('/tmp/temp' + str(id)) as files:
            data = json.load(files)
            info = {
                "id": id,
                "ip": data["ip"],
                "mac": data["mac"],
                "cpu_temp":data["cpu_temp"],
                "ap_temp": data["ap_temp"],
            }
    else:
        info = {
            "id":id,
            "ip": "not found",
            "mac": "not found",
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
                    "mac": data["mac"],
                    "cpu_temp":data["cpu_temp"],
                    "ap_temp": data["ap_temp"],
                }
        else:
            info = {
                "id": id,
                "ip": "not found",
                "mac": "not found",
                "cpu_temp":"not found",
                "ap_temp": "not found",
            }
        info_list.append(info)

    try:
        with open(VOL_RAW) as vol_raw:
            vol = vol_raw.readline().strip('\n')
        with open(VOL_SCALE) as vol_scale:
            scale = vol_scale.readline().strip('\n')
        fvol = float(vol) * float(scale)
        fresistance = (fvol * 390)/(1800 - fvol)
        adc_temp = temp_array[find_nearest(resistance_array, fresistance)]
        adc_info = {
            "adc": adc_temp
        }
    except Exception as e:
        adc_info = {
            "adc": 0
        }
    info_list.append(adc_info)
    return jsonify(data=info_list)

@app.route('/pxk/checkall',methods=['GET'])
def get_check_all():
    info_list = []
    for id in range(0,8):
        if os.path.exists('/tmp/temp' + str(id)) :
            with open('/tmp/temp' + str(id)) as files:
                data = json.load(files)
                info = {
                    "id": id,
                    "check": "Pass",
                }
        else:
            info = {
                "id": id,
                "ip": "Fail",
            }
        info_list.append(info)

    return jsonify(data=info_list)


@app.route('/pxk/check/<int:id>',methods=['GET'])
def get_check(id):
    if os.path.exists('/tmp/temp' + str(id)):
        with open('/tmp/temp' + str(id)) as files:
            data = json.load(files)
            info = {
                "id": id,
                "check": "Pass",
            }
    else:
        info = {
            "id":id,
            "check": "Fail",
        }
    info_list = []
    info_list.append(info);

    return jsonify(data=info_list)

@app.route('/pxk/setup_dhcp', methods=['POST'])
def setup_dhcp():
    #print request
    ip = request.form.get('ip')
    mac = request.form.get('mac')
    os.environ['ip'] = ip
    os.environ['mac'] = mac
    os.system('sh /etc/init.d/gen-dhcp.sh $ip &')
    if isvalidmac(mac):
        os.system('sh /etc/init.d/gen-mac-append.sh $ip $mac &')
    return '2001'

@app.route('/pxk/post_mac', methods=['POST'])
def post_mac():
    #print request
    mac = request.form.get('mac')
    id = request.form.get('id')
    try:
        with open('/tmp/mac' + id, 'w') as file:
            file.write(mac)
    except Exception as e:
        return '2000'
    return '2001'

@app.route('/pxk/post_mcu_mac', methods=['POST'])
def post_mcu_mac():
    mac = request.form.get('mac')
    try:
        split = mac.split(':')
        mac0 = split[2] + split[3] + split[4] + split[5]
        mac1 = split[0] + split[1]
        os.environ['mac0'] = mac0
        os.environ['mac1'] = mac1
        os.system('echo -n 0x$mac0 > /sys/fsl_otp/HW_OCOTP_MAC0')
        os.system('echo -n 0x$mac1 > /sys/fsl_otp/HW_OCOTP_MAC1')
    except Exception as e:
        return '2000'
    return '2001'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True);
