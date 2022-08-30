
from flask import Flask,request, render_template
from function import car_price

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def  predict():

    data = request.form

    km_driven = int(data['km_driven'])
    mileage = float(data['mileage'])
    engine = float(data['engine'])
    max_power =float(data['max_power'])
    seats = int(data['seats'])
    brand_name = data['brand_name']
    seller = data['seller']
    fuel = data['fuel']
    transmission =data['transmission']

    

    price = car_price(km_driven,mileage,engine,max_power,seats,brand_name,seller,fuel,transmission)
    predicted_price = price.predict_price()
    print(predicted_price)

    return render_template('index.html',final_price=predicted_price)


if __name__ == "__main__":
    app.run(debug=True)