from flask import Flask, request, jsonify
import joblib
from sklearn.ensemble import GradientBoostingRegressor

app = Flask(__name__)

# load model
model = joblib.load("model.pkl")
print ("Loaded model:", model)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    print ('request received:\n', request.args)
    result = {}
    prediction = -1
    
    try:
        bedrooms = int (request.args.get('Bedrooms'))
        bathrooms = float (request.args.get('Bathrooms'))
        sqft = int (request.args.get('SqFtTotLiving'))
        lot_size = int (request.args.get('SqFtLot'))
        land_val = int (request.args.get('LandVal'))

        columns = ["Bedrooms", "Bathrooms", "SqFtTotLiving", "SqFtLot", "LandVal"]
        data = [(bedrooms, bathrooms, sqft, lot_size, land_val)]
        #print ("Received data: ", data)
        
        prediction = model.predict(data)
        print ('predicted price ', prediction[0])
        result = {
            'prediction' :prediction[0],
        }


    except :
        prediction = -1.0
        
        result = {
            'prediction' : prediciton,
            'error' : 'some thing went wrong'
        }
    ## end try-except block
        
    return jsonify(result)

        


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run()  # default port 5000

