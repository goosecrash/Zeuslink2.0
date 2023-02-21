from flask import Flask, render_template

app = Flask(__name__)

# define your routes here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/total_supply')
def total_supply():
    return str(1000000)

if __name__ == '__main__':
    app.run(debug=True, port=5000) # run on port 5000 for HTML requests
    app.run(debug=True, port=8080) # run on port 8080 for total supply requests
