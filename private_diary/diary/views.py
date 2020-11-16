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
        PREF = "PREF41"
        areacode_l = "AREAL5152"
        PARAMS = {
            "keyid": KEYID,
            "pref": PREF,
            "areacode_l": areacode_l,
        }
        json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
        response = json.loads(json_res)
        if "error" in response:
            return print("エラーが発生しました！")
        if "category" in request.GET:
            param_value = request.GET.get("category")
            if param_value == "和食":
                category_l = "RSFST01000"
                PARAMS = {
                    "keyid": KEYID,
                    "pref": PREF,
                    "areacode_l": areacode_l,
                    "category_l": category_l,
                }
                json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
                response = json.loads(json_res)
                count = len(response['rest'])
                for count in range(count):
                    print(response['rest'][count]['name'])
                
            elif param_value == "洋食":
                print("洋食")
            elif param_value == "中華":
                print("中華")
            elif param_value == "喫茶店・カフェ":
                print("喫茶店・カフェ")
            elif param_value == "ファミレス":
                print("ファミレス")
            elif param_value == "居酒屋":
                print("居酒屋")
            
        return render(request,"index2.html")