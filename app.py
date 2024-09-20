from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.json
        print("Received data:", data)  # Log the received data
        if data:
            # Return the data back in the response
            return {"message": "Code executed with the following data", "data": data}, 200
        else:
            return {"message": "No JSON data received"}, 400
    return {"status": "success"}, 200

if __name__ == '__main__':
    app.run(debug=True)
