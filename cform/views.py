from django.shortcuts import render
from . import models,forms
from django.shortcuts import redirect

def newform(request):
    if request.method == "POST":
        form = forms.credform(request.POST)
        if form.is_valid():
            cred = form.save(commit=False)
            cred.save()
            return render(request,"cform/newform.html",{'form':form})
    else:
        form=forms.credform()
        return render(request,"cform/newform.html",{'form':form})
