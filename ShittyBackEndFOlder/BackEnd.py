from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('FrontEnd/SearchQueryThing.html')

@app.route('/api/SearchQuery', methods=['POST'])
def SearchQueryHa():
    # FIX 1: Add parentheses to execute the function
    recievedJson = request.get_json() 

    # FIX 2: Change 'UserInput' to 'ResultOfSearch' to match the JS payload
    userSearch = recievedJson.get('ResultOfSearch', '')
    
    print("--- TERMINAL PRINT ---")
    print(userSearch)
    print("----------------------")
    
    return jsonify({
        "status": "success",
        "reply": "sigmaballs"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
