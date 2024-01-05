
from flask import Flask
import math
import time
app = Flask(__name__)
@app.route('/')
def hello_world():
    start = time.time()
    for i in range(1000):
        for x in range(2,10):
            for y in range(1,10):
                print(x, '*', y, '=', x * y)
                if(y == 9):
                    print('----------')
    end = time.time()
    print(f"{end - start:.5f} sec")
    return '이상준'
if __name__ == '__main__':
    app.run(host='0.0.0.0')
