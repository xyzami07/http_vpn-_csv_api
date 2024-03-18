from flask import Flask
import pandas as pd


app = Flask(__name__)

df = pd.read_csv('http://www.vpngate.net/api/iphone/', skiprows=1)

df.rename(columns={"#HostName": "HostName"}, inplace=True)
data_dict = df.to_dict()


@app.route("/")
def api():
    return data_dict
