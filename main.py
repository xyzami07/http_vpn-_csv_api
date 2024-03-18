from flask import Flask, render_template
import pandas as pd

df = pd.read_csv('http://www.vpngate.net/api/iphone/', skiprows=1)

df.rename(columns={"#HostName": "HostName"}, inplace=True)
data_dict = df.to_dict()


app = Flask("website")


@app.route("/")
def api():
    return data_dict


if __name__ == '__main__':
    app.run(debug=True)

