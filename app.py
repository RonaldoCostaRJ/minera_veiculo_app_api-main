#Última alteração: 06/07/2024 por: Ronaldo Ramos da Costa
#######################################################################
##### importações necessárias para o funcionamento da API #############

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Modelo_Automovel
from logger import logger
from schemas import *
from flask_cors import CORS
#from openai import OpenAI
import openai




#nome da API
info = Info(title=" Enriquecimento de Metadados com o uso de APIS do CEP e da OPENAI(ChatGPT) - Case para Veículos e Região Geográfica", version="1.0.0")
#chamada a OpenAPI
app = OpenAPI(__name__, info=info)
CORS(app)

# definição das tags que serão utilizadas
home_tag = Tag(name="Documentação", description="Documentação: Swagger")
automovel_tag = Tag(name="Modelo de Automóvel e Localização", description="Adição, visualização e remoção de um registro de busca por um automóvel na base")
##################################################################################################################################################################################################################################
#redirecionamento para Open API
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, swagger, apresentando a tela que contém a documentação da API.
    """
    return redirect('/openapi/swagger#')
##################################################################################################################
#inserção de um novo registro de busca por um modelo de automóvel no database a partir de um @post no endpoint relacionado.   
@app.post('/modeloauto', tags=[automovel_tag],
          responses={"200": Modelo_AutomovelViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_modelo_automovel(form: Modelo_AutomovelSchema):
    """Adiciona um novo Modelo à base de dados

    Retorna uma representação da busda por um modelo de automóvel associado.
    """
    modelo_automovel = Modelo_Automovel(
    
        regiao_busca_in = form.regiao_busca,
        categoria_modelo_in =form.categoria_modelo,
        tipo_modelo_in =form.tipo_modelo,
        tipo_cambio_modelo_in =form.tipo_cambio_modelo,
        marca_modelo_in =form.marca_modelo,
        nome_modelo_in = form.nome_modelo,        
        ano_desde_modelo_in = form.ano_desde_modelo,
        ai_caracteristicas_in = form.ai_caracteristicas, 
        ai_valor_medio_in = form.ai_valor_medio,
        ai_valor_seguro_in = form.ai_valor_seguro, 
        ai_info_regiao_in = form.ai_info_regiao 

        
      )
        
    logger.debug(f"Adicionando o nome do modelo de automóvel utilizado: '{modelo_automovel.nome_modelo}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando automóvel
        session.add(modelo_automovel)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionada uma nova busca por um modelo de nome: '{modelo_automovel.nome_modelo}'")
        return apresenta_modelo_automovel(modelo_automovel), 200

    except IntegrityError as e:
        # a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Já existe uma busca por este modelo de automóvel salva na base :/"
        logger.warning(f"Erro ao adicionar o modelo '{modelo_automovel.nome_modelo}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # tratamento para um erro fora do que foi previsto durante no desenvolvimento
        error_msg = "Não foi possível salvar a busca pelo modelo :/"
        logger.warning(f"Erro ao adicionar modelo: '{modelo_automovel.nome_modelo}', {error_msg}', {error_msg}")
        return {"mesage": error_msg}, 400
##################################################################################################################
##################################################################################################################
#inserção de um novo registro de busca por um modelo de automóvel no database a partir de um @post no endpoint relacionado.   
@app.put('/modeloauto', tags=[automovel_tag],
          responses={"200": Modelo_AutomovelViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def updt_modelo_automovel(form: Modelo_Automovel_AtualizaSchema):
    """Atualiza as informações de um modelo existente a partir do NOME de um nome de Modelo já existente.

    
    """
    modelo_automovel = Modelo_Automovel(
    
        regiao_busca_in = form.regiao_busca,
        categoria_modelo_in =form.categoria_modelo,
        tipo_modelo_in =form.tipo_modelo,
        tipo_cambio_modelo_in =form.tipo_cambio_modelo,
        marca_modelo_in =form.marca_modelo,
        nome_modelo_in = form.nome_modelo,        
        ano_desde_modelo_in = form.ano_desde_modelo,
        ai_caracteristicas_in = form.ai_caracteristicas, 
        ai_valor_medio_in = form.ai_valor_medio,
        ai_valor_seguro_in = form.ai_valor_seguro, 
        ai_info_regiao_in = form.ai_info_regiao 
    )
  
    try:
        # criando conexão com a base
        session = Session()
        modeloauto = session.query(Modelo_Automovel).all()
        for modelo in modeloauto:
            if modelo.nome_modelo == modelo_automovel.nome_modelo:
                modelo.marca_modelo =form.marca_modelo
                modelo.regiao_busca = modelo_automovel.regiao_busca
                modelo.categoria_modelo =modelo_automovel.categoria_modelo
                modelo.tipo_modelo =modelo_automovel.tipo_modelo
                modelo.tipo_cambio_modelo =modelo_automovel.tipo_cambio_modelo
                modelo.ano_desde_modelo = modelo_automovel.ano_desde_modelo
                modelo.ai_caracteristicas = form.ai_caracteristicas 
                modelo.ai_valor_medio = form.ai_valor_medio
                modelo.ai_valor_seguro = form.ai_valor_seguro 
                modelo.ai_info_regiao = form.ai_info_regiao

        session.commit()
       
        return apresenta_modelo_automovel(modelo_automovel), 200

    except IntegrityError as e:
        # a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Erro ao atualizar este automóvel  na base :/"
        logger.warning(f"Erro ao adicionar o modelo '{form.nome_modelo}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # tratamento para um erro fora do que foi previsto durante no desenvolvimento
     
        logger.warning(f"Erro ao atualizar modelo: '{form.nome_modelo}', {error_msg}', {error_msg}")
        return {"mesage": error_msg}, 400

##################################################################################################################
##################################################################################################################
#recuperação de uma lista com todos as buscas de automóveis no database a partir de um @get no endpoint relacionado.   

@app.get('/modeloautos', tags=[automovel_tag],
         responses={"200": ListagemModelo_AutomovelSchema, "404": ErrorSchema})
def get_modelos_automovel():
    """Faz a busca por todas as buscas pormodelos de automóveis cadastrados

    Retorna uma representação da listagem das buscas por modelos encontrados.
    """
    logger.debug(f"Coletando buscas por modelos de automóveis ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    modeloauto = session.query(Modelo_Automovel).all()

    if not modeloauto:
        # se não há modelos cadastrados
        return {"modeloauto": []}, 200
    else:
        logger.debug(f"%d automóveis econtrados" % len(modeloauto))
        # retorna a representação de modelo.
        print(modeloauto)
        return apresenta_modelos(modeloauto), 200

##################################################################################################################
#recuperação de um busca de automóveis no database a partir do nome de um modelo utilizando um @get no endpoint relacionado.   
@app.get('/modeloauto', tags=[automovel_tag],
         responses={"200": Modelo_AutomovelViewSchema, "404": ErrorSchema})
def get_modelo_automovel(query: Modelo_AutomovelBuscaSchema):
    """Retorna uma única  busca por um modelo de automóvel, a partir do nome do modelo

    Retorna uma representação de uma busca de modelo de automóvel.
    """
    modelo_automovel_modelo = query.nome_modelo
    logger.debug(f"Coletando dados sobre o modelo de automóvel #{modelo_automovel_modelo}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca    
    modeloauto = session.query(Modelo_Automovel).filter (Modelo_Automovel.nome_modelo == modelo_automovel_modelo).first()
    
    if not modeloauto:
        # se o modelo não foi encontrado
        error_msg = "Modelo de Automovel não encontrado na base :/"
        
        logger.warning(f"Erro ao buscar modelo de automóvel '{modelo_automovel_modelo}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Modelo de Automóvel econtrado: '{modelo_automovel_modelo}' ")
        # retorna a representação de modelo
        return apresenta_modelo_automovel(modeloauto), 200

##################################################################################################################
#Deleção de uma única busca por modelo de automóvel, a partir do nome de um modelo utilizando um @get no endpoint relacionado.   
@app.delete('/modeloauto', tags=[automovel_tag],
            responses={"200": Modelo_AutomovelDelSchema, "404": ErrorSchema})
def del_modelo_automovel(query: Modelo_AutomovelBuscaSchema):
    """Deleta um Automóvel a partir do nome do modelo informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    automovel_nome = unquote(unquote(query.nome_modelo))    
   
    print(automovel_nome)
    logger.debug(f"Deletando dados sobre o modelo de automóvel #{automovel_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Modelo_Automovel).filter( Modelo_Automovel.nome_modelo == automovel_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado modelo de automóvel: #{automovel_nome}")
        return {"mesage": "Modelo removido: " + automovel_nome}
    else:
        # se o modelo não foi encontrado
        error_msg = "Modelo de automóvel não encontrado na base :/"
        logger.warning(f"Erro ao deletar Modelo de automóvel #'{automovel_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
##################################################################################################################

