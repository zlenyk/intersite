from django.db import models
from datetime import datetime

class Tag(models.Model):
    name = models.CharField(max_length=50)
   
    @staticmethod
    def getTagByName(_name):
        return Tag.objects.get(name=_name)

    @staticmethod
    def addTag(_name):
        Tag(name=_name).save()
        return getTagByName(_name)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    login = models.CharField(max_length=20)
    content = models.TextField()
    interviewId = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    @staticmethod
    def addComment(_login,_content,_interviewId):
        Comment(login=_login,content=_content,interviewId=_interviewId).save()

        return Comment.objects.get(login=_login,content=_content,interviewId=_interviewId)


class Interview(models.Model):
    person = models.ForeignKey("people.Person")
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category)
    comments = models.ManyToManyField(Comment, blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def addComment(self,login,content,interviewId):
        self.comments.add(Comment.addComment(login,content,interviewId))
    
    def addTag(self,name):
        self.tags.add(Tag.addTag(name))

    @staticmethod
    def createInterview(_person,_title,_content):
        newInterview = Interview(
            person = _person,
            title = _title,
            content = _content
        )
        newInterview.save();

    @staticmethod
    def getAllInterviews(orderBy='-pub_date'):
        return Interview.objects.order_by(orderBy)

    @staticmethod
    def getInterviewById(_id):
        return Interview.objects.get(id=_id)

    def __unicode__(self):
        return self.title


