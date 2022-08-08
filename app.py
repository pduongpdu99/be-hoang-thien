from flask import *
from flask_cors import CORS

import pandas as pd
import numpy as np
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/test', methods = ['POST'])
def index():
    data = json.loads(request.data)
    fullname = data['fullname']
    sdt = data['number']
    email = data['email']
    df1 = pd.read_excel('test.xlsx')
    t = df1.to_numpy()[:, 1:].tolist()
    t.append([fullname, sdt, email])
    df1 = pd.DataFrame(data=np.array(t), columns=['FULLNAME', 'SDT','EMAIL'])
    df1.to_excel('test.xlsx')
    return json.dumps(t)