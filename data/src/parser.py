import os
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


class FestivalParser:

    @staticmethod
    def parse_festivals() -> pd.DataFrame:
        data = []
        for html_path in tqdm(os.listdir('htmls')):
            data.append(FestivalParser.parse_html(html_path))
        festivals = pd.DataFrame(data)
        festivals = festivals[festivals["lineup"].notna()]
        festivals["artist_count"] = festivals["lineup"].str.len()
        festivals["country"] = festivals["location"].str.split(",").str[-1].str.strip()
        return festivals.query("artist_count > 7")

    @staticmethod
    def parse_html(html_path: str) -> dict:
        with open(os.path.join('htmls', html_path), 'r', encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            return {
                "name": FestivalParser.parse_festival_name(soup),
                "date": FestivalParser.parse_festival_date(soup),
                "location": FestivalParser.parse_festival_location(soup),
                "lineup": FestivalParser.parse_festival_lineup(soup)
            }

    @staticmethod
    def parse_festival_name(soup) -> str:
        element = soup.select_one(
            '#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterunsplash > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div > h1')
        if element is None:
            element = soup.select_one(
                "#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterlight > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div.mb-2 > h1 > strong")
        festival_name = element.text.replace("Festival 2023", "")
        return festival_name.strip()

    @staticmethod
    def parse_festival_date(soup):
        element = soup.select_one(
            "#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterunsplash > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div > div > span")
        if element is None:
            element = soup.select_one(
                "#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterlight > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div.mb-2 > div > span")
        festival_date = element.text
        return festival_date.split(",")[0].strip()

    @staticmethod
    def parse_festival_location(soup):
        element = soup.select_one(
            "#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterunsplash > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div > div > span > span")
        if element is None:
            element = soup.select_one(
                "#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterlight > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div.mb-2 > div > span")
        festival_city = element.text
        country_element = soup.select_one(
            "#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterunsplash > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div > div > span > a")
        if country_element is None:
            country_element = soup.select_one(
                "#content > div.maxcontainer.mx-auto.bg-white.mt-4.mt-sm-0.mb-4.mb-sm-0 > div.position-relative.d-md-flex.bg-img-hero.height-futdfilterlight > div > div > div.row.align-items-center.position-absolute.bottom-0.mr-1 > div > div > div.mb-2 > div > span > a")
        festival_country = country_element.get("href")
        return f"{festival_city.strip()}, {festival_country.split('/')[-1].strip().title()}"

    @staticmethod
    def parse_festival_lineup(soup):
        element = soup.select_one(
            "#lineup > div > div:nth-child(3) > div > div")
        if element is None:
            return None
        bodies = element.find_all(class_="card-body")
        if len(bodies) == 0:
            return None
        artists = set()
        for body in bodies:
            artists = artists.union(set(a.text.lower().strip()
                                    for a in body.find_all("span")))
        for artist in artists:
            if "&" in artist:
                artists = artists.union(set(a.strip()
                                        for a in artist.split("&")))
            if " b2b " in artist:
                artists = artists.union(set(a.strip()
                                        for a in artist.split(" b2b ")))
        return list(a for a in artists if a != "")
