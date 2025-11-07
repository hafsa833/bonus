from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the vulnerable app!"

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get("name")
    return f"Hello {name}"

@app.route('/exec', methods=['POST'])
def exec_cmd():
    import os
    cmd = request.form.get("cmd")
    return os.popen(cmd).read()

if __name__ == '__main__':
    app.run(debug=True)
"# trigger" 
