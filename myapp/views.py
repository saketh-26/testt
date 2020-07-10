from django.shortcuts import render
from myapp.models import TitanicPrediction
from django import forms
from myapp.day3gnw import home
#import numpy as np
# Create your views here.

class TitanicForm(forms.ModelForm):
	class Meta:
		model = TitanicPrediction
		fields = '__all__'

'''def home(Age,SibSp,Parch,Fare,Gender,Pclass,Place):

  p = []
  p +=[Age,SibSp,Parch,Fare]
  if Gender.casefold() == "m":
    p+=[1]
  else:
    p+=[0]
  if Pclass == 2:
    p+=[1,0]
  elif Pclass == 3:
    p+=[0,1]
  else:
    p+=[0,0]
  if Place.casefold() == "queenstown":
    p+=[1,0]
  elif Place.casefold() == "southampton":
    p+=[0,1]
  else:
    p+=[0,0]
  arr = np.array([p])
  predict = survivalpredict(arr)
  if predict == [1]:
    result = {'result':'Survived'}
  else:
    result = {'result':'Not Survived'}
  return result'''

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TitanicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            # ...
            age = form.cleaned_data['age']
            sibsp = form.cleaned_data['sibsp']
            parch = form.cleaned_data['parch']
            fare = form.cleaned_data['fare']
            gender = form.cleaned_data['gender']
            pclass = form.cleaned_data['pclass']
            place = form.cleaned_data['place']
            # redirect to a new URL:
            result = home(age,sibsp,parch,fare,gender,pclass,place)

            return render(request, 'index.html', {'form': form,'result':result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TitanicForm()

    return render(request, 'index.html', {'form': form})
