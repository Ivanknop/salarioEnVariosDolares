import requests
import json
import os

class Dolar_converter():
    
    def __init__(self,salary=0):
        self.actual_quote = {'pesos':salary}
        self.__set_quotes()
    
    def __set_quotes(self):
        url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        try:
            response = requests.get(url)
            response.raise_for_status()
            quotes = response.json()
            self.__prepare_quotes(quotes)
        except requests.RequestException as e:
            print(f"Error al obtener las cotizaciones: {e}")

    def __prepare_quotes(self, quotes):
        excluded_currencies = ['Dolar', 'Argentina', 'Dolar Soja', 'Bitcoin']
        for quote in quotes:
            currency_name = quote['casa']['nombre']
            if currency_name not in excluded_currencies:
                self.actual_quote[currency_name] = quote['casa']['venta'].replace(',', '.')
       
    def calculate(self):
        pesos_amount = float(self.actual_quote['pesos'])
        for currency in self.actual_quote.keys():
            if currency != 'pesos':
                self.actual_quote[currency] = round(pesos_amount / float(self.actual_quote[currency]), 2)
        return self.actual_quote

    def show_quote(self):
        return self.actual_quote
    

