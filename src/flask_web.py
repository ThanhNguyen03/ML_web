from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the KMeans model once when the server starts
model = joblib.load('kmeans_modellll.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    income = data['income']
    spending = data['spending']

    # Reshape the input data and create a DataFrame with column names
    input_data = np.array([[income, spending]])
    input_df = pd.DataFrame(input_data, columns=['Annual Income', 'Spending Score'])

    # Make a prediction
    prediction = model.predict(input_df)

    if prediction[0] == 0:
        result="Khách hàng có thu nhập trung bình hàng năm và chi tiêu hàng năm trung bình"
    elif prediction[0]==1:
        result="Khách hàng có thu nhập hàng năm cao nhưng chi tiêu hàng năm thấp"
    elif prediction[0]==2:
        result="Khách hàng có thu nhập hàng năm thấp và chi tiêu hàng năm thấp"
    elif prediction[0]==3:
        result="Khách hàng có thu nhập hàng năm thấp nhưng chi tiêu hàng năm cao"
    elif prediction[0]==4:
        result="Khách hàng có thu nhập hàng năm cao và chi tiêu hàng năm cao"

    # Return the result as JSON
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
