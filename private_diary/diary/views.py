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
            elif param_value == "洋食":
                category_l = "RSFST13000"
                PARAMS = {
                    "keyid": KEYID,
                    "pref": PREF,
                    "areacode_l": areacode_l,
                    "category_l": category_l,
                }
                json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
                response = json.loads(json_res)
            elif param_value == "中華":
                category_l = "RSFST14000"
                PARAMS = {
                    "keyid": KEYID,
                    "pref": PREF,
                    "areacode_l": areacode_l,
                    "category_l": category_l,
                }
                json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
                response = json.loads(json_res)
            elif param_value == "喫茶店・カフェ":
                category_l = "RSFST18000"
                PARAMS = {
                    "keyid": KEYID,
                    "pref": PREF,
                    "areacode_l": areacode_l,
                    "category_l": category_l,
                }
                json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
                response = json.loads(json_res)
            elif param_value == "ファミレス":
                category_l = "RSFST20000"
                PARAMS = {
                    "keyid": KEYID,
                    "pref": PREF,
                    "areacode_l": areacode_l,
                    "category_l": category_l,
                }
                json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
                response = json.loads(json_res)
                
            elif param_value == "居酒屋":
                category_l = "RSFST09000"
                PARAMS = {
                    "keyid": KEYID,
                    "pref": PREF,
                    "areacode_l": areacode_l,
                    "category_l": category_l,
                }
                json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
                response = json.loads(json_res)
        if "namae" in request.GET:
            
            PARAMS = {
                    "keyid": KEYID,
                    "pref": PREF,
                    "areacode_l": areacode_l,
                    
                }
            json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
            response = json.loads(json_res)
        store_list = [] 
        for i in response['rest'] :
            store_list.append({
                "name":i["name"],
                "address":i["address"],
                "tel":i["tel"],
                "url":i["url"],
            })
        print(type(response))
        return render(request,"index2.html",{"store_list":store_list})