
import pandas as pd
import os
from pier import Pier

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = os.path.join(ROOT_DIR, "files") 

def bloquear_cartao_e_mudar_estagio(idcartao, pier):
    estagio_body ={
        "id": 4
    }

    url_bloquear = '/cartoes/'+ str(idcartao)+'/bloquear?id_status=2&observacao=status para nao embossing'
    url_estagio = '/cartoes/'+str(idcartao)+'/alterar-estagio'

    status_block, content_block = pier.post(url=url_bloquear, format_json=True)

    if status_block == 200:
        status_estagio, content_estagio = pier.post(url=url_estagio, json=estagio_body, format_json=True)



def carregar_cartoes():
    file_path = os.path.join(FILES, "base_cartao.xlsx")

    print(f"Arquivo: {file_path}")
    df = pd.read_excel(file_path, engine='openpyxl')
    df.dropna(subset=["ID_CONTA", "ID_CARTAO"], inplace=True)
    
    df = df.astype({'ID_CARTAO': 'int64', 'ID_CONTA': 'int64', 'ID_STATUS_CARTAO': 'int64'})

    return df

if __name__ == '__main__':
    pier = Pier()

    cartoes = carregar_cartoes()
    lista_cartoes = cartoes['ID_CARTAO'].to_list()
    i = 0
    for id_cartao in lista_cartoes:
        i = i + 1
        bloquear_cartao_e_mudar_estagio(id_cartao, pier)
        print(i)
