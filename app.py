from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Safe Flask App</title>
</head>
<body>
    <h2>Welcome</h2>
    <form method="get" action="/greet">
        <label>Name:</label>
        <input type="text" name="name" required>
        <input type="submit" value="Greet">
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(TEMPLATE)

@app.route('/greet')
def greet():
    name = request.args.get("name", "guest")
    safe_name = ''.join(c for c in name if c.isalnum() or c.isspace())
    return f"<h3>Hello, {safe_name}!</h3>"

if __name__ == '__main__':
    app.run(debug=False)  # ✅ safe now!
