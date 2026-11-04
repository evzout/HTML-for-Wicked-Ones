from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('SearchQueryThing.html')

@app.route('/api/message', methods=['GET'])
def getMessage():
    data = {'Message': "kill yourself"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=6767)
