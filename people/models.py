from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name + " " + self.surname

    @staticmethod
    def getAllPeople(orderBy='surname'):
        return Person.objects.order_by(orderBy)

    @staticmethod
    def getPersonById(_id):
        return Person.objects.get(id=_id)
