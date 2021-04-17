import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
import time
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()




def priceDiscount(soup):
    price_discount = soup.find('span', {"class": "discountPrice"})
    if(price_discount is None):
        return ""

    return (price_discount.text.strip())


def priceNotDiscount(soup):
    price_not_discount = soup.find('span', {"class": "currencyPrice"})
    if(price_not_discount is None):
        return ""

    return (price_not_discount.text.strip())


def offerPercentage(soup):
    price_offer_percentage = soup.find('div', {"class": "detay-indirim"})
    if(price_offer_percentage is None):
        return ""
    return (price_offer_percentage.text.strip())


def productName(soup):
    #multiple return statements
    product_name = soup.find('h1', {"class": "product-name"})
    if(product_name is None):
        return ""

    brand = product_name.find('span', {"class": "fbold"})
    if(brand is None):
        return ""
    brand.extract()

    return (product_name.text.strip())


def productCode(soup):
    product_code = soup.find('div', {"class": "product-feature-content"})
    if(product_code is None):
        return ""
    product_code_unwanted = product_code.find_all(['div','b'])
    for tag in product_code_unwanted:
        tag.extract()

    return (product_code.text.strip())


def productAvailability(soup):
    size_variant_active = 0
    size_variant_passive = 0
    product_availability = 0
    variants = soup.find_all('div', class_="new-size-variant")
    for tag in variants:
        size_variant_passive = len(tag.find_all('a', {"class": "passive"}))
        size_variant_active = len(tag.find_all('a')) - size_variant_passive
        product_availability = (size_variant_active /
                                len(tag.find_all('a'))) * 100

    if size_variant_active == 0 and size_variant_passive == 0:
        return ""
    else:
        return ('{0:.0f}%'.format(product_availability))


if __name__ == '__main__':


    
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = os.environ["KEY_PATH"]

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SPREADSHEET_ID = '1a1da53hBBBRMzjqWhxSETPW821DdYhmUGVmg0KfEGBw'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    df = pd.read_excel(os.environ["DF_PATH"]) 

    for index, row in df.iterrows():
        url = 'https://www.markastok.com{}'.format(row['/'])
        page = requests.get(url)
        print(row['/'])

        soup = BeautifulSoup(page.text, 'html.parser')

        value_range_body = {
            "majorDimension": "COLUMNS",
            "values": [
                [
                    url
                ],
                [
                    productCode(soup)
                ],
                [
                    productAvailability(soup)
                ],
                [
                    priceDiscount(soup)
                ],
                [
                    priceNotDiscount(soup)
                ],
                [
                    productName(soup)
                ],
                [
                    offerPercentage(soup)
                ]
            ]
        }

        if value_range_body['values'][1] != ['']:
            sheet.values().append(spreadsheetId=SPREADSHEET_ID, range='urunler!A2', valueInputOption="RAW",  body=value_range_body).execute()

