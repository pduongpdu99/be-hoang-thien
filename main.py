from flask import *
from flask_cors import CORS

import pandas as pd
import numpy as np
import json

app = Flask(__name__, static_folder="static")
app.config['JSON_AS_ASCII'] = False
CORS(app)



@app.route('/test', methods = ['POST'])
def index():
    # return "hello world"
    data = json.loads(request.data)
    fullname = data['fullname']
    sdt = data['number']
    email = data['email']
    df1 = pd.read_excel('static/test.xlsx', index_col=0)
    t = df1.to_numpy()[:, :].tolist()
    t.append([fullname, sdt, email])
    print(np.array(t, dtype=object))
    df1 = pd.DataFrame(data=np.array(t, dtype=object), dtype=object, columns=['FULLNAME', 'SDT','EMAIL'])
    df1.reset_index(drop=True, inplace=True)
    df1.to_excel('static/test.xlsx')
    return json.dumps(t)


@app.route('/data', methods=['GET'])
def get_data():
    df1 = pd.read_excel('static/test.xlsx', index_col=0)
    t = df1.to_numpy()[:, :].tolist()
    return json.dumps(t)
