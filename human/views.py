from django.shortcuts import render
from human.forms import HumanForm

def human_list(request):
    # st1 = {'name':'gio', 'lname':'Khomasuridze', 'age':18}
    # st2 = {'name': 'gia', 'lname': 'Khomasuridze', 'age': 65}
    # st3 = {'name': 'gogi', 'lname': 'cabadze', 'age': 100}
    # st4 = {'name': 'guga', 'lname': 'goguadze', 'age': 14}
    # st5 = {'name': 'gaga', 'lname': 'Khmiadashvili', 'age': 41}
    #
    # lst = [{'course_name':'back', 'students':[st1, st2, st3]},
    #        {'course_name':'front', 'students':[st4, st5]}]


    return render(request, 'human_list.html', {'form':HumanForm})
