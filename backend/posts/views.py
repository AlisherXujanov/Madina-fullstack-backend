from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostForm

# CRUD -> Create Read Update Delete

# Create your views here.


def home(request):
    context = {
        "posts": Posts.objects.all(),
        "form": PostForm()
    }  # MUST be a dict
    return render(request, "home.html", context)


def post_details(request, pk: int):
    post = Posts.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "post_details.html", context)




def create_post(request):
    context = {
        "form": PostForm()
    }
    if request.method == "POST":
        # initialize the form with the data from the request
        form = PostForm(request.POST)
        if form.is_valid():  # if the form is valid
            form.save()  # save the form to the database
            # commit=False means that we will not save the form to the database yet.
            # This is useful if we want to add or change something before saving it.
            # call the same view function/page again
            return redirect("home")
        else:
            print('ERROR FORM INVALID')

    return render(request, "create_post.html", context)


def update_post(request, pk: int):
    post = Posts.objects.get(pk=pk)
    form = PostForm(instance=post)
    context = {
        "post": post,
        "form": form
    }
    if request.method == "POST":
        # initialize the form with the data from the request
        form = PostForm(request.POST, instance=post)
        if form.is_valid():  # if the form is valid
            form.save()  # save the form to the database
            # commit=False means that we will not save the form to the database yet.
            # This is useful if we want to add or change something before saving it.
            # call the same view function/page again
            return redirect("home")
        else:
            print('ERROR FORM INVALID')

    return render(request, "update_post.html", context)


def delete_post(request, pk: int):
    post = Posts.objects.get(pk=pk)
    post.delete()
    return redirect("home")


# 1. URL   ->  The users enters our URL into browser
# 2. URLS  ->  Our urls.py file recieves the request
#              and passes it to the function
# 3. VIEWS ->  The function recieves the request and answers
#              back with response (through the render(...) fn)
# 4. URLS  ->  urls.py gets the response back and sends it back
#              to the user who requested smth from our project
# ------------------------------------------------------------
# EX: Our site is called  https://www.express.com

# 1. User searches for our site and enters it
# 2. So, we get a request to show him our first page
# 3. The urls.py gets that request and passes it to the fn of views.py
# 4. That function works out the logic what we should show the user and sends it to the urls.py in response-form
# 5. The urls.py sends that response to the user back as HTML file
