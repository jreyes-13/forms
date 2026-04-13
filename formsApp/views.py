from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template("index.html");
    return HttpResponse(template.render(context, request));


# def login(request):
#     email = request.POST["email"];
#     pwd = request.POST["password"];
#     # Need to add validation to each field
#     # Alternatively, we could let Django handle the validation for us
#     # To do so, we need to use forms.
#     if not email or "@" not in email:   
#         print("Invalid email")

#     Login.objects.create(email=email, password=pwd)
#     context = {} #{"email": email}
#     template = loader.get_template("index.html");
#     return HttpResponse(template.render(context, request));

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():            
            form.save()
            print("Login Info Saved")
        else:
            print("Invalid Form")
        context = {}
        template = loader.get_template("index.html");
        return HttpResponse(template.render(context, request));

#with authentication
# from django.contrib.auth import authenticate, login
# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST or None)
#         if form.is_valid():            
#             cd = form.cleaned_data
#             user = authenticate(
#                 request, 
#                 email = cd["email"],
#                 password = cd["password"]
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
            
#     else: 
#         context = {}
#         template = loader.get_template("index.html");
#         # return HttpResponse(template.render(context, request));
#         return render(request, 'index.html', {'form': form})

def loginDetails(request):
    details = Login.objects.all
    context = {"details": details}
    template = loader.get_template("login_details.html");
    return HttpResponse(template.render(context, request));