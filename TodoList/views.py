from django.shortcuts import render

# Create your views here.
def render_todolist(req):
  return render(req, 'index.html')
