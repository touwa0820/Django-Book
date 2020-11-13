from django.views import generic
from django.shortcuts import render    
import json
import csv
import requests

#初期設定
KEYID = 'da4e1585e099dac608d681acf6b4e042'
HIT_PER_PAGE = 100
PREF = "PREF41"
area_code = "AREA140"
areacode_l = "AREAL5152"
areacode_m = "AREAM5439"
areacode_s = "AREAS5437"
name = ""
name_kana = ""

PARAMS = {"keyid":KEYID,"hit_per_page":HIT_PER_PAGE,"pref":PREF,"area_code":area_code,"areacode_l":areacode_l,"areacode_m":areacode_m,"areacode_s":areacode_s,"name":name,"name_kana":name_kana}

def write_date_to_csv(parms):
    foodlist = ["名称","住所"]
    json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/",params=PARAMS).text
    respons = json.loads(json_res)
    if "error" in respons:
        return print("エラーが発生しました！")
    for foodlist in respons["food"]:
        foodlist_name = foodlist["name"]
        foodlist.append(foodlist_name)
    with open("food_list.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(foodlist)
    return print(foodlist)

write_date_to_csv(PARAMS)



# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"


class TableView(generic.TemplateView):
    template_name = "index2.html"

    def get(self,request,*args,**kwatgs):
        print(request)
        return render(request,"index2.html")