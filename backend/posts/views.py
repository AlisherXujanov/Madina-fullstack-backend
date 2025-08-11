from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "This is title", 
        "text": "What a beautiful day it is!"
    } # MUST be a dict
    return render(request, "home.html", context)

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
