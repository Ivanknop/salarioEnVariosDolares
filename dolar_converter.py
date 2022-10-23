import requests
import json

class Dolar_converter():
    
    def __init__(self,salary=0):
        self.dolar_today = {'pesos':salary}
        self.__set_quotes()
    
    def __new_quote(self,type_of_dolar):
        url = 'https://api-dolar-argentina.herokuapp.com/api/'+type_of_dolar
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content
            res_dict = json.loads(content.decode('utf-8'))
            self.dolar_today[type_of_dolar] = float(res_dict['venta'])

    def __set_quotes(self):
        self.__new_quote('dolarblue')
        self.__new_quote('dolaroficial')
        self.__new_quote('dolarbolsa')
        self.__new_quote('dolarturista')
        self.__new_quote('mayorista')
        self.__new_quote('contadoliqui')
    
    def calculate(self):
        self.dolar_today['dolarblue'] = round(float(self.dolar_today['pesos']) / self.dolar_today['dolarblue'],2)
        self.dolar_today['dolaroficial'] = round(float(self.dolar_today['pesos']) / self.dolar_today['dolaroficial'],2)
        self.dolar_today['dolarturista'] = round(float(self.dolar_today['pesos']) / self.dolar_today['dolarturista'],2)
        self.dolar_today['contadoliqui'] = round(float(self.dolar_today['pesos']) / self.dolar_today['contadoliqui'],2)
        self.dolar_today['dolarbolsa'] = round(float(self.dolar_today['pesos']) / self.dolar_today['dolarbolsa'],2)
        self.dolar_today['mayorista'] = round(float(self.dolar_today['pesos']) / self.dolar_today['mayorista'],2)
        return self.dolar_today

    def show_quote(self):
        return self.dolar_today
    

