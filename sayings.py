from __future__ import annotations
from enum import IntEnum
from datetime import datetime
import xml.etree.ElementTree as ET

import requests

from text import TextDB


class TimeOfDay(IntEnum):
    MORNING = 1
    DAY     = 2
    EVENING = 3

def time_of_day() -> int:
    h = datetime.now().hour
    if h <= 10:
        return TimeOfDay.MORNING
    if h <= 18:
        return TimeOfDay.DAY
    return TimeOfDay.EVENING


class Sayings:
    corona_url = "https://services5.arcgis.com/Hx7l9qUpAnKPyvNz/arcgis/rest/services/stats_all_final/FeatureServer/"\
        "0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Date%20desc&resultOffset=0&resultRecordCount=1&resultType=standard&cacheHint=true"
    news_url = "https://jyllands-posten.dk/?service=rssfeed&mode=area&areaNames=level0,topflow"

    def __init__(self, textdb: TextDB):
        self.textdb = textdb

    def time_greeting(self, timebased=True) -> str:
        time = time_of_day()
        if not timebased:
            return self.textdb.get_text("hello")
        if time == TimeOfDay.MORNING:
            return self.textdb.get_text("goodmorning")
        if time == TimeOfDay.DAY:
            return self.textdb.get_text("goodday")
        return self.textdb.get_text("goodevening")

    def coronastatus(self) -> str:
        data = requests.get(
            self.corona_url
        ).json()["features"][0]["attributes"]
        infected, tested, total_admissions = data["Daily_Infected"], data["Tests_Diff"], data["Admissions"]
        return self.textdb.get_text("corona").format(infected=infected, tested=tested, total_admissions=total_admissions)

    def news(self, n_headlines: int=3) -> (str, str, str, str):
        page = requests.get(
            self.news_url
        ).text
        news = ET.fromstring(page)[0].findall("item")[0:n_headlines]
        return [
            self.textdb.get_text("news"),
            *(new[0].text for new in news)
        ]

if __name__ == '__main__':
    t = TextDB("da")
    s = Sayings(t)
    print(s.news())





