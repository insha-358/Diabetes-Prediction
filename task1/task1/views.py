from django.shortcuts import render

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

def frontpage(request):

    return render(request, 'frontpage.html')

def predict(request):

    return render(request, 'predict.html')

def result(request):

    data = pd.read_csv(r"D:\python\task1\task1\diabetes.csv")

    x = data.drop("Outcome", axis=1)

    y = data['Outcome']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LogisticRegression()

    model.fit(x_train, y_train)

    value1 = float(request.GET['n1'])

    value2 = float(request.GET['n2'])

    value3 = float(request.GET['n3'])

    value4 = float(request.GET['n4'])

    value5 = float(request.GET['n5'])

    value6 = float(request.GET['n6'])

    value7 = float(request.GET['n7'])

    value8 = float(request.GET['n8'])

    pred = model.predict([[value1 , value2 , value3 , value4 , value5 , value6 , value7 , value8 ]])

    result1 =""

    if pred == [1]: result1 = "Positive"

    else : result1 = "Negative"

    return render(request, 'predict.html',{"result2":result1})
