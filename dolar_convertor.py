import requests
import json

class Dolar_convertor():
    
    def __init__(self,salary=0):
        self.dolar_today = {'pesos':salary}
        self.__add_quotes()
    
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
        self.dolar_today['dolarblue'] = float(self.dolar_today['pesos']) / self.dolar_today['dolarblue']
        self.dolar_today['dolaroficial'] = float(self.dolar_today['pesos']) / self.dolar_today['dolaroficial']
        self.dolar_today['dolarturista'] = float(self.dolar_today['pesos']) / self.dolar_today['dolarturista']
        self.dolar_today['contadoliqui'] = float(self.dolar_today['pesos']) / self.dolar_today['contadoliqui']
        self.dolar_today['dolarbolsa'] = float(self.dolar_today['pesos']) / self.dolar_today['dolarbolsa']
        self.dolar_today['mayorista'] = float(self.dolar_today['pesos']) / self.dolar_today['mayorista']
        return self.dolar_today

    def show_quote(self):
        return self.dolar_today
    

