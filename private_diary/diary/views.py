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

    def get(self,request):
        Category = request.Get.get("1","何もありません")
        dic = {"cate":Category}
        return render(request,"index2.html",dic)
        
    def get(self, request):
        if "query_param" in request.GET:
            # query_paramが指定されている場合の処理
            param_value = request.GET.get("query_param")