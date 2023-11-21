import pickle

def prediction(cylinders, displacement, horsepower, weight, acceleration, model_year, origin):
    x = [[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]]
    model = pickle.load(open('RandomForestRegressor_best_model.sav', 'rb'))
    predictions = model.predict(x)
    return predictions


def load_model():
    model = pickle.load(open('/home/zeyd/Desktop/end to end /LR/LR/RandomForestRegressor_best_model.sav', 'rb'))
    return model