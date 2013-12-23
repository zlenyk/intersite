from people.models import Person
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def show_person(request,id):
    person = Person.getPersonById(id)
    return render(request,'people/person.html',{'person':person})
