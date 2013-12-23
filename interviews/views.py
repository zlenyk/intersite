from interviews.models import Interview
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def show_interview(request,id):
    interview = Interview.getInterviewById(id)
    return render(request,'interviews/interview.html',{'interview':interview})

def add_comment(request):
    id = request.POST.get('id')
    login = request.POST.get('login')
    content = request.POST.get('content')

    interview = Interview.getInterviewById(id)
    interview.addComment(login,content,id)
    
    return render(request,'interviews/interview.html',{'interview':interview})
    
