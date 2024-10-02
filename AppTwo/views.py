from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render_to_response

def help(request):
    m_dict={'data_filler':'Help page'}
    return render(request,'apptwo/help.html',context=m_dict)

# Create your views here.
