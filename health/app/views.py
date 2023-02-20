from urllib import request
from django.shortcuts import render
import json

# Create your views here.

def index(request):
#request.GET gets all the parameter entered in the form.

    if request.method == 'GET':

        #All the form parameters will be saved in this list.

        lst_1 = []                           

        #Getting the relevant data from eavh form field.
        NPI = request.GET.get('NIP')                
        firstname = request.GET.get('firstname')
        middlename = request.GET.get('middlename')
        lastname = request.GET.get('lastname')
        states = request.GET.get('state')
        speciality1 = request.GET.get('speciality1')
        speciality2 = request.GET.get('speciality2')
        speciality3 = request.GET.get('speciality3')
        speciality4 = request.GET.get('speciality4')
        search = request.GET.get('search')
        lst_1.extend((NPI,firstname,middlename,lastname,states,speciality1,speciality2,speciality3,speciality4))
    while("" in lst_1):
        lst_1.remove("")

    #List of states defined which is used by states dropdown in the frontend.

    state_lst = ['Miami','New York','California','Alabama','Chicago','Texas','Ohio','Georgia','Alaska','Washington','Virginia','Colorado','Illinois','New Jersey','North Calorina','Michigan','Oregon','Indiana','Utah','Montana']
    lst = []

# [[],[],[]]
    #Reading the json file

    f = open('db.json')
    data =json.load(f)

    #iterating through each record(dictionary) in the json.

    main = data['records']

    #iterating each dictionary and getting the values through keys.

    for vals in main:
        inni_lst=[]
        for k in vals.keys():
            inni_lst.append(vals[k])
        lst.append(inni_lst)

    #django render function which takes the file name that uses the particular function and the parameters
    #which we want to display on the frontend

    return render(request, 'index.html', {'lst_1':lst_1,'NPI':NPI,'firstname':firstname,'middlename':middlename,'lastname':lastname,'states':states, 'state_lst':state_lst, 'speciality1':speciality1,'speciality2':speciality2,'speciality3':speciality3,'speciality4':speciality4, 'lst':lst,'search':search})
    

