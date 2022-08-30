from distutils.command.config import config
import pickle
from unittest import result
import numpy as np
import json
import config

class car_price():

    def __init__(self,km_driven,mileage,engine,max_power,seats,brand_name,seller,fuel,transmission):
        """ init function for accepting the User Input """
        self.km_driven = km_driven
        self.mileage = mileage
        self.engine = engine
        self.max_power = max_power
        self.seats = seats
        self.brand_name = brand_name
        self.seller = seller
        self.fuel = fuel
        self.transmission = transmission
        


    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as file:
            self.model = pickle.load(file)

        with open(config.COLUMN_LIST__PATH,'r') as file:
            self.columns_dict = json.load(file)


    def predict_price(self):
        self.load_model()

        array = np.zeros(len(self.columns_dict['columns']))

        array[0] = self.km_driven
        array[1] = self.mileage
        array[2] = self.engine
        array[3] = self.max_power
        array[4] = self.seats

        brand_value = 'brand_name_' + self.brand_name
        brand_index = self.columns_dict['columns'].index(brand_value)
        array[brand_index] = 1

        seller_value = 'seller_type_' + self.seller
        seller_type_index = self.columns_dict['columns'].index(seller_value)
        array[seller_type_index]=1

        fuel_value = 'fuel_type_' + self.fuel 
        fuel_type_index = self.columns_dict['columns'].index(fuel_value)
        array[fuel_type_index] = 1

        transmission_value = 'transmission_type_' + self.transmission 
        transmission_index = self.columns_dict['columns'].index(transmission_value)
        array[transmission_index] = 1

        # print(array)

        result = self.model.predict([array])
        # print(result)

        return result[0]




if __name__ == '__main__':
    km_driven = 120000.0
    mileage = 19.7
    engine = 796.0
    max_power =46.3
    seats = 5.0
    brand_name = 'Maruti'
    model = 'Alto'
    seller = 'Dealer'
    fuel = 'Petrol'
    transmission = 'Manual' 
    year= 2015


    car_price_obj = car_price(km_driven,mileage,engine,max_power,seats,brand_name,seller,fuel,transmission,year)

    car_price_obj.predict_price()

