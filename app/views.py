from django.shortcuts import render
from app.models import *
# Create your views here.
from django.db.models.functions import Length
def display_topic(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.filter(topic_name='Cricket')
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)
def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)
def Access_records(request):
    LOA=AccessRecord.objects.all()
    d={'records':LOA}
    return render(request,'Access_records.html',context=d)

