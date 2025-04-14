#Última alteração: 06/07/2024 por: Ronaldo Ramos da Costa
#######################################################################
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from model.modelo_automovel import Modelo_Automovel

#######################################################################
#####     Definição dos schemas utilizados na API    ##################
#######################################################################
class Modelo_ChatGPT_ResponseSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a pesquisa de uma busca, feita com base no nome do Modelo do automóvel.
    """
    request : str = "Msg de Solicitação à API da OpenAI "
    resposta  : str = "Msg de Retorno"



class Modelo_AutomovelSchema(BaseModel):
    """ Define como um novo modelo de automóvel a ser inserido, deve ser representado.
    """
    
    regiao_busca : str = "RJ, Zona Sul"
    categoria_modelo : str = "Carros"
    marca_modelo : str = "Fiat"
    tipo_modelo : str = "Hatch"
    tipo_cambio_modelo : str = "Automático"
    nome_modelo  : str = "Pulse"
    ano_desde_modelo : int = 2020
    ai_caracteristicas : str = " Informações da AI sobre o veículo" 
    ai_valor_medio : str = " Informações da AI sobre o valor médio na região"
    ai_valor_seguro : str = "Informações da AI sobre o valor aunal do seguro para uma região"
    ai_info_regiao : str = "Informações da AI sobre características da região do Automóvel identificadas pelo CEP."
        

class Modelo_Automovel_AtualizaSchema(BaseModel):
    """ Define como um modelo existente de automóvel a ser atualizado pelo NOME, deve ser representado.
    """
    
    nome_modelo  : str = "Pulse"
    regiao_busca : str = "RJ, Zona Sul"
    categoria_modelo : str = "Carros"
    marca_modelo : str = "Fiat"
    tipo_modelo : str = "Hatch"
    tipo_cambio_modelo : str = "Automático"    
    ano_desde_modelo : int = 2020
    ai_caracteristicas : str = " Informações da AI sobre o veículo" 
    ai_valor_medio : str = " Informações da AI sobre o valor médio na região"
    ai_valor_seguro : str = "Informações da AI sobre o valor aunal do seguro para uma região"
    ai_info_regiao : str = "Informações da AI sobre características da região do Automóvel identificadas pelo CEP."
        


class Modelo_AutomovelBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a pesquisa de uma busca, feita com base no nome do Modelo do automóvel.
    """
    nome_modelo  : str = "Pulse"
  

class ListagemModelo_AutomovelSchema(BaseModel):
    """ Define como uma listagem de buscas por modelos cadastradas, será retornada.
    """
    modelos_auto:List[Modelo_AutomovelSchema]


def apresenta_modelos(modelos_auto: List[Modelo_Automovel]):
    """ Retorna uma representação de uma busca por modelo, seguindo o schema definido em
        Modelo_AutomovelViewSchema.
    """
    result = []
    for modelo in modelos_auto:
        result.append({
            "marca_modelo" : modelo.marca_modelo,
            "nome_modelo": modelo.nome_modelo,           
            "categoria_modelo": modelo.categoria_modelo,
            "tipo_modelo": modelo.tipo_modelo,
            "tipo_cambio_modelo": modelo.tipo_cambio_modelo,
            "ano_desde_modelo": modelo.ano_desde_modelo,
            "regiao_busca": modelo.regiao_busca,             
            "data_insercao": modelo.data_insercao,
            "ai_caracteristicas" : modelo.ai_caracteristicas,
            "ai_valor_medio" : modelo.ai_valor_medio,
            "ai_valor_seguro" : modelo.ai_valor_seguro,
            "ai_info_regiao" : modelo.ai_info_regiao
       })

    return {"modelos_auto": result}


class Modelo_AutomovelViewSchema(BaseModel):
    """ Define como uma 'busca por modelo', será retornada: modelo_auto
    """
    id_busca_modelo : int = 1
    regiao_busca : str = "RJ, Zona sul"
    categoria_modelo : str = "Carros"
    marca_modelo : str = "Fiat"
    tipo_modelo : str = "Hatch"
    tipo_cambio_modelo : str = "Automático"
    nome_modelo  : str = "Pulse"
    ano_desde_modelo : int = 2020
    ai_caracteristicas : str = " Informações da AI sobre o veículo" 
    ai_valor_medio : str = " Informações da AI sobre o valor médio na região"
    ai_valor_seguro : str = "Informações da AI sobre o valor aunal do seguro para uma região"
    ai_info_regiao : str = "Informações da AI sobre características da região do Automóvel identificadas pelo CEP."
          

class Modelo_AutomovelDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome_modelo: str
    

def apresenta_modelo_automovel(modelo_auto: Modelo_Automovel):
    """ Retorna uma representação do registro de uma busca por modelo de automóvel, seguindo o schema definido em
        Modelo_AutomovelViewSchema.
    """
    return {
        "marca_modelo": modelo_auto.marca_modelo,
        "id_busca_modelo": modelo_auto.id_busca_modelo,
        "nome_modelo": modelo_auto.nome_modelo,       
        "categoria_modelo": modelo_auto.categoria_modelo,
        "tipo_modelo": modelo_auto.tipo_modelo,
        "tipo_cambio_modelo": modelo_auto.tipo_cambio_modelo,
        "ano_desde_modelo": modelo_auto.ano_desde_modelo,    
        "regiao_busca": modelo_auto.regiao_busca, 
        "data_insercao": modelo_auto.data_insercao,
        "ai_caracteristicas" : modelo_auto.ai_caracteristicas,
        "ai_valor_medio" : modelo_auto.ai_valor_medio,
        "ai_valor_seguro" : modelo_auto.ai_valor_seguro,
        "ai_info_regiao" : modelo_auto.ai_info_regiao
        }