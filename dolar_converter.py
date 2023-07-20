import requests
import json
import os
class Dolar_converter():
    
    def __init__(self,salary=0):
        self.dolar_today = {'pesos':salary}
        self.__set_quotes()
    
    def __new_quote(self,type_of_dolar):
        url = 'https://api.estadisticasbcra.com/'+type_of_dolar
        access_token = os.getenv("TOKEN")
        headers = {"Content-Type":"application/json", "Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.content
            res_dict = json.loads(content.decode('utf-8'))       
            self.dolar_today[type_of_dolar] = float((res_dict[-1]["v"])
  )

    def __set_quotes(self):
        self.__new_quote('usd')
        self.__new_quote('usd_of')
        self.__new_quote('usd_of_minorista')
    
    def calculate_usd_blue(self):
        return (self.dolar_today['usd_of'] + (self.dolar_today['usd_of']*0.35) + (self.dolar_today['usd_of']*0.30))

    def calculate(self):
        self.dolar_today['usd'] = round(float(self.dolar_today['pesos']) / self.dolar_today['usd'],2)
        self.dolar_today['usd_of'] = round(float(self.dolar_today['pesos']) / self.dolar_today['usd_of'],2)
        self.dolar_today['usd_of_minorista'] = round(float(self.dolar_today['pesos']) / self.dolar_today['usd_of_minorista'],2)        
        self.dolar_today['blue'] = round(float(self.dolar_today['pesos']) / self.calculate_usd_blue(),2)
        return self.dolar_today

    def show_quote(self):
        return self.dolar_today
    

