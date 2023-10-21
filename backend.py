from flask import Flask, render_template, request, jsonify
from math import *
from flask_cors import CORS
import data_connect

# 使用Flask框架封装后端，与前端交互
app = Flask(__name__)
# 允许跨域请求
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('frontend.html')

# 接收前端待计算式，返回计算结果
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # 使用get_json来解析JSON数据
    expression = data['expression']
    try:
        # 进行符号替换，转化为eval函数可识别的式子
        expression_replace=expression.replace('^','**')
        expression_replace=expression_replace.replace('√','sqrt')
        expression_replace=expression_replace.replace('ln','log')
        expression_replace=expression_replace.replace('÷','/')
        expression_replace=expression_replace.replace('×','*')
        print(expression_replace)
        result = eval(expression_replace)
        formula=expression+'='+str(result)
        flag=data_connect.sql_action(2,formula)
        if flag==2:
            print(result)
            return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# 读数据库，返回给前端历史记录
@app.route('/history', methods=['POST'])
def history():
    data = request.get_json()  # 使用get_json来解析JSON数据
    try:
        flag=data_connect.sql_action(1)
        if flag:
            print(flag)
            return jsonify({'result': flag})
        else:
            return jsonify({'error': '无'})
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/dele', methods=['POST'])
def dele():
    data = request.get_json()  # 使用get_json来解析JSON数据
    expression = data['expression']
    try:
        flag=data_connect.sql_action(3,expression)
        if flag:
            print(flag)
            return jsonify({'result': flag})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=8000)



