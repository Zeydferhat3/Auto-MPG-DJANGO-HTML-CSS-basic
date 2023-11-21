from django.shortcuts import render
from . import ml

def home(request):
    return render(request,"index.html")
import joblib  # Corrected import statement

def results(request):
    cylinders = float(request.GET.get('cylinders'))
    displacement = float(request.GET.get('displacement'))
    horsepower = float(request.GET.get('horsepower'))
    weight = float(request.GET.get('weight'))
    acceleration = float(request.GET.get('acceleration'))
    model_year = float(request.GET.get('model_year'))
    origin = float(request.GET.get('origin'))

    model = joblib.load('RandomForestRegressor_best_model.sav')
    predictions = model.predict([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]])


    return render(request, 'results.html', {'predictions': predictions})