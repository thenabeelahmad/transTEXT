from django.shortcuts import render, redirect
from googletrans import Translator

tr = Translator()

def index(request):
    if request.method == 'POST':
        txt = request.POST.get('originaltext')
        ot = tr.detect(txt).lang
        lang = request.POST.get('lang')
        trans = tr.translate(txt,dest=lang,src=ot)
        translatedtext = trans.text
        return render(request,'home.html',{"trans":translatedtext})        
    return render(request,'index.html')


