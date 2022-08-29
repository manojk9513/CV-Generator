from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io


# Create your views here.
def index(request):
    def __str__(self):
        return self.name

    if request.method =="POST":
        name=request.POST.get('name',"")
        email=request.POST.get('emailid',"")
        phno=request.POST.get('phnoid',"")
        summery=request.POST.get('textareaid',"")
        degree=request.POST.get('degreeid',"")
        school=request.POST.get('schoolid',"")
        university=request.POST.get('uniid',"")
        exprience=request.POST.get('expid',"")
        skills=request.POST.get('skillid',"")

        profile=Profile(name=name,email=email,phno=phno,summery=summery,degree=degree,school=school,university=university,exprience=exprience,skills=skills)
        profile.save()
    return render(request,'pdf/index.html',{})

def csv(request,id):
    user_profile=Profile.objects.get(pd=id)
    template=loader.get_template('pdf/cv_template.html')
    html=template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename='resume.pdf'
    return response