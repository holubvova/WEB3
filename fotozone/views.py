from django.shortcuts import render
from .forms import Forgot_password, Sign_in, Register , Edit
from django.http import HttpResponseRedirect, HttpResponse
from .models import User


AAA = []


def sign(request):
    error = ""
    if request.method == 'POST':

        form = Sign_in(request.POST)

        if form.is_valid():

            Email = form.cleaned_data["Email_sign"]
            Password = form.cleaned_data["Password"]
            a = list(User.objects.filter(user_email=Email))
            if len(a) == 1:
                tmp = User.objects.get(user_email=Email)
                if tmp.user_password == Password:
                    AAA.append(Email)
                    return HttpResponseRedirect('/fotozone_y/')
                else:
                    error= "Passwords do not match"
            elif len(a) > 1 :

                error="Account was exist"
                return HttpResponseRedirect('/',{'form':form, 'error': error})
            else:
                return HttpResponseRedirect('/',{'form':form, 'error': error})
    else:
        form = Sign_in()
    return render(request,'Title/sign_in_title.html',{'form':form, 'error': error} )

def about_n(request):
    return render(request,'Title/about_site_no.html')

def fotozone_n(request):
    AAA.clear()
    return render(request, 'Title/fotozone_no.html')

def about_y(request):
    return render(request,'Title/about_site.html')

def fotozone_y(request):
    return render(request, 'Title/fotozone_yes.html')

def profile(request):
    fields = User.objects.get(user_email=AAA[0])

    return render(request, 'Title/profile.html',{'fields': fields})

def edit(request):
    error = ""
    if request.method == 'POST':

        form = Edit(request.POST)

        if form.is_valid():
            Email = form.cleaned_data["Email"]
            Name = form.cleaned_data["Name"]
            SurName = form.cleaned_data["SurName"]
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']
            booking = form.cleaned_data['birthday']
            number = form.cleaned_data['Number']
            tmp = User.objects.get(user_email=AAA[0])
            tmp.user_email = Email
            tmp.user_name = Name
            tmp.user_surname = SurName
            tmp.user_gender = gender
            tmp.user_birthday = birthday
            tmp.user_booking = booking
            tmp.user_tell = number
            AAA[0] = Email
            tmp.save()
            return HttpResponseRedirect('/profile/')

    else:
        form = Edit()
    return render(request, 'Title/edit.html', {'form': form})

def register(request):

    error = ""
    if request.method == 'POST':

        form = Register(request.POST)

        if form.is_valid():
            Email = form.cleaned_data["Email"]
            Name = form.cleaned_data["Name"]
            Password = form.cleaned_data["Password"]
            R_Password = form.cleaned_data["R_Password"]
            gender=form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']
            if Password == R_Password:
                a = list(User.objects.filter(user_email=Email))
                if len(a) == 0:
                        usr = User(user_name=Name, user_email = Email, user_password =Password, user_gender=gender,user_birthday=birthday,user_tell=380000000000,user_surname="",user_booking="2000-01-01")
                        usr.save()
                        return HttpResponseRedirect('/')
                else:
                    return render(request, 'Title/registered.html',{'form': form, 'error' : error})


            else:
                return HttpResponse("passwords do not match")

    else:
        form = Register()
    return render(request, 'Title/registered.html',{'form': form,'error':error})


def forgot_password(request):

    if request.method == 'POST':

        form = Forgot_password(request.POST)

        if form.is_valid():
            Email = form.cleaned_data["Email"]
            a = User.objects.filter(user_email=Email)
            if len(a) == 1:
                New_pass=form.cleaned_data["New_password"]
                R_New_pass = form.cleaned_data["R_New_password"]
                if New_pass == R_New_pass:
                    tmp = User.objects.get(user_email=Email)
                    tmp.user_password = New_pass
                    tmp.save()
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("passwords do not match")

    else:
        form = Forgot_password()

    return render(request, 'Title/Forgot_passord.html', {'form':form})
