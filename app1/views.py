from django.shortcuts import render
from app1.models import Profile
# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        profile.save()
    return render(request,"home.html")

def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    return render(request,"resume.html",{'user_profile':user_profile})

