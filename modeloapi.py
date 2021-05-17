from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/node")
def me_api():
    data = {
        "nodename": "bcopzbxsrv02",
        "hostname": "bcopzbxsrv02",
        "username": "ansible",
        "description": "Servidor zabbix 5.2",
        "tags": "PRODUCAO",
        "osFamily": "Red Hat",
        "osArch": "",
        "osName": "",
        "osVersion": "",
        "editUrl": "",
        "remoteUrl": ""
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
