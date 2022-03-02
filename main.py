from distutils.command.config import config
import json, requests
from dotenv import dotenv_values
from db import Db

class Fuel(Db):
    
    def __init__(self):

        config = dotenv_values('.env')
        apiKey = config['API_KEY']
        selffirebaseAuth = config['FIREBASE_AUTH']

        stationId = 'fe50b4a5-84c9-4812-a0b7-4b29f589e1e2'

        url = f'https://creativecommons.tankerkoenig.de/json/detail.php?id={stationId}&apikey={apiKey}'      

        self.data = self.getStationDetails(url)

    def getStationDetails(self, url):

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)

        return data

    def getDieselPrice(self) -> float:

        price = self.data['station']['diesel']

        return price

    def getE10Price(self) -> float:

        price = self.data['station']['e10']

        return price

    def getE5Price(self) -> float:

        price = self.data['station']['e5']

        return price

    def intoDb(self):

        diesel = self.getDieselPrice()
        e10 = self.getE10Price()
        e5 = self.getE5Price()

        self.insert(diesel, e10, e5)

fuel = Fuel()

fuel.intoDb()