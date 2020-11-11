from django.views import generic
from django.shortcuts import render
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"


class TableView(generic.TemplateView):
    template_name = "index2.html"

    def get(self,request,*args,**kwatgs):
        print(request)
        return render(request,"index2.html")
