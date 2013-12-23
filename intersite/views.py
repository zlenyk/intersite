from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from interviews.models import Interview
from people.models import Person
def index(request):
    inter_list = Interview.getAllInterviews()
    return render(request, 'content.html',{'list':inter_list})

def people_list(request):
    people_list = Person. getAllPeople()
    return render(request, 'people/people_list.html',{'list':people_list})
    
