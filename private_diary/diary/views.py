from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get(self,request,*args,**kwatgs):
        return render(request,"index.html")