#import from Model class

from django.db import models

class Post(models.Model):

 #Create a title property

    title = models.CharField(max_length=64)

#Create a date property

    date = models.DateTimeField()   

#Create a body of content property

    body = models.TextField()

# This method is just like toString() function in .NET. Whenever Python needs to show a

#string representation of an object, it calls __str__

    def __str__(self):
        return "%s " % (self.title)