from flask import Flask, render_template

app = Flask(__name__)

total_supply = 1000

@app.route("/")
def home():
    return render_template('index.html', total_supply=total_supply)

if __name__ == "__main__":
    app.run()
