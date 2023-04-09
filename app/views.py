from django.shortcuts import render
from app.models import *
# Create your views here.
from django.db.models.functions import Length
from django.db.models import Q
def display_topic(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.filter(topic_name='Cricket')
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)
def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.filter(topic_name='Tennis')
    LOW=Webpage.objects.exclude(name='Sania')
    LOW=Webpage.objects.filter(name__startswith='S')
    LOW=Webpage.objects.filter(name__endswith='A')
    LOW=Webpage.objects.filter(name__contains='n')
    LOW=Webpage.objects.filter(name__in=('Hima','Yuvaraj'))
    LOW=Webpage.objects.filter(topic_name__in=('Tennis','Football'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(name='Yuvaraj') & Q(topic_name='Cricket'))
    LOW=Webpage.objects.filter(Q(topic_name='Football'))

    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)
def Access_records(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-11-11')
    LOA=AccessRecord.objects.filter(date__gte='2023-4-6')
    LOA=AccessRecord.objects.filter(date__lt='2023-4-11')
    LOA=AccessRecord.objects.filter(date__lte='2023-4-11')
    LOA=AccessRecord.objects.filter(date__month='4')
    LOA=AccessRecord.objects.filter(date__year='2022')
    LOA=AccessRecord.objects.filter(date__day='11')
    LOA=AccessRecord.objects.filter(date__year__gt='2022')
    LOA=AccessRecord.objects.filter(date__month__gt='4')
    LOA=AccessRecord.objects.filter(date__day__gte='6')

    d={'records':LOA}
    return render(request,'Access_records.html',context=d)

