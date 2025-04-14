#Última alteração: 06/07/2024 por: Ronaldo Ramos da Costa
#######################################################################
#importa os tipos de dados que serão utilizados
from sqlalchemy import Column, String, Integer, DateTime,Float

from datetime import datetime
from typing import Union

from  model import Base

##clase base que é utilizada para representar as informações de uma busca por um modelo de automóvel via webscrapping.
class Modelo_Automovel(Base):
    __tablename__ = 'modelo_automovel'    
    id_busca_modelo = Column("id_busca_modelo", Integer, primary_key=True)
    marca_modelo = Column(String(25))
    nome_modelo = Column(String(50), unique=True )     
    categoria_modelo = Column(String(30))
    tipo_modelo = Column(String(20))
    tipo_cambio_modelo = Column(String(15))
    ano_desde_modelo = Column( Integer)
    regiao_busca = Column(String(500))  
    data_insercao = Column(DateTime)
    ai_caracteristicas= Column(String(3000))
    ai_valor_medio= Column(String(500))
    ai_valor_seguro= Column(String(500))
    ai_info_regiao = Column(String(3000))


    ##################################################################################################################

    def __init__(self, marca_modelo_in:str, nome_modelo_in:str, categoria_modelo_in:str, tipo_modelo_in:str,tipo_cambio_modelo_in:str,
                ano_desde_modelo_in: int, regiao_busca_in:str,  ai_caracteristicas_in:str , ai_valor_medio_in:str, ai_valor_seguro_in: str, 
                ai_info_regiao_in: str,data_insercao_in:Union[DateTime, None] = None):
        """
        Cria um Modelo_Automovel

        Argumentos:            
            marca_modelo: nome da marca do modelo de automóvel a ser pesquisado. Exemplo: Fiat / VolksWagen / Renault / Chevrolet / Ford
            nome_modelo: nome do modelo de automóvel. Exemplo: Palio / Gol / Fusca / Pulse/ Uno / Corola
            categoria_modelo: Detalhe da categoria de Automóvel. Exemplo: Carros / Caminhões / Ônibus 
            tipo_modelo: Detalhe do tipo de Automóvel quanto ao porte e utilidade. Exemplo: Hatch / SUV / Sedã / Pick-up / Conversível / Caminhão Leve / Buggy / Van/Utilitário. 
            tipo_cambio_modelo: Detalhe do câmbio. Exemplo: Automático / Manual / Semi-Automático / Automatizado.
            ano_desde_modelo: Indica o ano inicial de fabricação que interessa na busca. Em conjunto com o ano_ate_modelo, forma um range do período de busca: Exemplo: 2019 --> (2019 a 2022)
            
            regial busca: região do Cep.
            data de inserção da busca. Define a data de inclusão da busca no sistema.
            
        """
        # Inicialização dos dados durante a instanciação da classe.
        self.marca_modelo = marca_modelo_in
        self.nome_modelo = nome_modelo_in        
        self.categoria_modelo = categoria_modelo_in
        self.tipo_modelo = tipo_modelo_in
        self.tipo_cambio_modelo = tipo_cambio_modelo_in
        self.ano_desde_modelo = ano_desde_modelo_in
        self.regiao_busca = regiao_busca_in
       #########   AI #############
        self.ai_caracteristicas = ai_caracteristicas_in
        self.ai_valor_medio = ai_valor_medio_in
        self.ai_valor_seguro = ai_valor_seguro_in
        self.ai_info_regiao = ai_info_regiao_in
       

       # Caso a data de inserção não seja informada, será registrado a data exata da inserção no banco.
        if data_insercao_in:
            self.data_insercao = data_insercao_in
        else: 
            self.data_insercao = datetime.now()
