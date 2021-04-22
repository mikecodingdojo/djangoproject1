from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def add_user(request):
    if request.method == "POST":

        #Request.POST['pass vars from html']
        #We need a dict to store values from request.POST 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        comment = request.POST['comment']

        # request.session['first_name'] = first_name
        # request.session['last_name'] = last_name
        # request.session['comment'] = comment
        context = {
            "first_name": first_name, 
            "last_name": last_name,
            "comment" : comment

        }

        request.session['forminfo'] = context
    return redirect('/success')

def results(request):
    return render(request, 'show.html')
    
    