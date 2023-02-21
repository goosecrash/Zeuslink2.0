from flask import Flask, request

app = Flask(__name__)

# Define the total_supply variable here
total_supply = 1000000

@app.route('/total_supply', methods=['GET'])
def get_total_supply():
    global total_supply
    return str(total_supply)

@app.route('/mine', methods=['POST'])
def mine():
    global total_supply
    mined_coins = int(request.form['coins'])
    total_supply += mined_coins
    return "Mined {} coins. Total supply is now {}.".format(mined_coins, total_supply)

if __name__ == '__main__':
    app.run()
