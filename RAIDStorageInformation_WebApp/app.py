"""
Author: Philip Narteh
Operating Systems Mini Project 4
"""


from flask import Flask, request, jsonify
# from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return """
    <center>
    <h1>Operating Systems Mini Project 4</h1>
    <h2>Philip Narteh - 29832022<h2>
    <br>
    <hr>
    <br>
    <h2><strong>To Test the Permissions API, do the following 👇:</strong></h2>
    <h3><p>Put <em>'/permissions?code=num'</em> after the current host(homepage) URL in your browser and change 
    <em>'num'</em> to your desired permissions code</p></h3>
    <br>
    <h2><strong>To Test the Parity API, do the following 👇:</strong></h2>
    <h3><p>Put <em>'/parity?b1=n1&b2=n2&b3=n3&b4=n4'</em> after the current host(homepage) URL in your browser and 
    change <em>'n1', 'n2', 'n3' and 'n4'</em> to your desired 2-bit RAID block numbers</p></h3>
    </center>
    """


@app.route("/permissions/", methods=["GET"])
def permissions():
    code = request.args.get('code')
    final_permissions = {"owner": decode_permissions(bin(int(code[0]))[2:]),
                         "group": decode_permissions(bin(int(code[1]))[2:]),
                         "other": decode_permissions(bin(int(code[2]))[2:])
                         }

    return jsonify(final_permissions)


def decode_permissions(num):
    if num in ('0', '1'):
        num = '00' + num
    elif num in ('10', '11'):
        num = '0' + num

    perm_list = []
    if num[0] == '1':
        perm_list.append("read")
    if num[1] == '1':
        perm_list.append("write")
    if num[2] == '1':
        perm_list.append("execute")
    return perm_list


@app.route('/parity/', methods=["GET"])
def parity():
    b1 = request.args.get('b1')
    b2 = request.args.get('b2')
    b3 = request.args.get('b3')
    b4 = request.args.get('b4')
    MSBs = b1[0] + b2[0] + b3[0] + b4[0]
    LSBs = b1[1] + b2[1] + b3[1] + b4[1]
    MSBs_1_count = MSBs.count('1')
    LSBs_1_count = LSBs.count('1')

    if MSBs_1_count % 2 == 0:
        MSB_parity = '0'
    else:
        MSB_parity = '1'

    if LSBs_1_count % 2 == 0:
        LSB_parity = '0'
    else:
        LSB_parity = '1'

    return MSB_parity + LSB_parity


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)