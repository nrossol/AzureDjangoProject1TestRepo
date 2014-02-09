# Create your views here.
from django.shortcuts import render_to_response
from myblog.models import Post

#Creating a view for the home page
def home(request):
   posts = Post.objects.all()
   #Renders a given template with a given context dictionary and returns an
   #HttpResponse object with that rendered text.
   return render_to_response('home.html', {'posts': posts} )