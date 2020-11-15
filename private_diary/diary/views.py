from django.views import generic
from django.shortcuts import render    
import json
import csv
import requests

        #初期設定

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"


class TableView(generic.TemplateView):
    template_name = "index2.html"

    def get(self,request,*args,**kwatgs,):
        KEYID = "da4e1585e099dac608d681acf6b4e042"
        HIT_PER_PAGE = 100
        PREF = "PREF41"
        areacode_l = "AREAL5152"
        areacode_m = "AREAM5439"
        areacode_s = "AREAS5437"
        name = ""
        name_kana = ""
        PARAMS = {
            "keyid": KEYID,
            # "hit_per_page": HIT_PER_PAGE,
            "pref": PREF,
            "areacode_l": areacode_l,
            # "areacode_m": areacode_m,
            # "areacode_s": areacode_s,
            # "name": name,
            # "name_kana": name_kana
        }
        json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
        response = json.loads(json_res)

        if "error" in response:
            return print("エラーが発生しました！")
        
        def category(self,request):
            if "category" in request.Get:
                param_value = request.Get("category")
            print(param_value)
        # print(response)
        return render(request,"index2.html")