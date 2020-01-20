from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request  ,'index.html')
def analize(request):
    invoice = request.POST.get('voice')
    param = {'invoice': invoice}
    return render(request,'analize.html',param)    
def reco(request):
    return render(request  ,'voicereco.html')