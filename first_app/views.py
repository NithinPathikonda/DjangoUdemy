from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord


def index(request):
    # my_dict={'insert_something':'My name is Nithin, I am full stack Developer @$@#! Not a full time tester $Y@#Y@'}

    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records': webpages_list}
    return render(request,'index.html', context=date_dict)

    


# Create your views here.


