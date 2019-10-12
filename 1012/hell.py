from flask import Flask

app = Flask(__name__)

@app.route("/")  #路由
def index():  ## 视图
    return  "hello world"

if __name__ == '__main__':
    app.run()   ##项目启动