from datetime import datetime
from pydantic import BaseModel
from typing import List
from model.cfc import Cfc

from schemas import CarroSchema, CarroViewSchema, InstrutorSchema , InstrutorListagemSchema
#
class CfcSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado"""
    #id: int = 50
    codigo: str = "ac1215"
    nome: str = "Auto Escola de Jacarepagua"
    cnpj: str = "70.982.550/0001-39"
    status: bool = True
    regiao:str = "Jacarepagua"

#estrutura get apenas por codigo    
class CfcBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no codigo da cfc. """
    codigo: str = "ac1215"
    
#estrutura getAll  
class ListaCfcsSchema(BaseModel):
    """ Define como a lista de cfc será retornada """
    cfcs:List[CfcSchema]

def apresenta_cfcs(cfcs:List[Cfc]):
    """ Retorna uma representação da cfc seguindo o schema definido em CfcViewSchema."""
    result = []
    for cfc in cfcs:
        result.append({
            "id": cfc.id,
            "codigo": cfc.codigo,
            "nome": cfc.nome,
            "cnpj": cfc.cnpj,
            "status": cfc.status,
            "regiao": cfc.regiao 
        })  
                                   
    return{"cfcs": result}

class CfcViewSchema(BaseModel):
    """ Define como uma cfc será retornada: cfc + instrutor + carro. """
    id: int = 1
    codigo:str = "ab0000"
    nome:str = "Auto Escola Sem Nome"
    cnpj:str = "43515658000149"
    status = True
    regiao = "Bairro"
    # ultima_atualizacao = datetime.now()
    instutores: List[InstrutorListagemSchema]
    carros:List[CarroViewSchema]
    
    
    
#esquema delete        
class CfcDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    codigo: str

#esquema apenas 1 cfc    
def apresenta_cfc(cfc: Cfc):
    """ Retorna uma representação da cfc seguindo o schema definido em CfcViewSchema. """
    return{
        "id":cfc.id,
        "codigo": cfc.codigo,
        "nome":cfc.nome,
        "cnpj":cfc.cnpj,
        "status":cfc.status,
        "regiao":cfc.regiao,
        "ultima_atualizacao": cfc.ultima_atualizacao,
        "instrutores": [{"id": i.id , "cpf":i.cpf , "nome":i.nome , "aula": i.aula
                         , "status":i.status , "ultima_atualizacao": i.ultima_atualizacao} for i in cfc.instrutores],
        "carros":[{"id":c.id , "renavan":c.renavan , "placa":c.placa , "marca":c.marca , "modelo":c.modelo,
                   "status":c.status , "ultima_atualizacao":c.ultima_atualizacao} for c in cfc.carros]        
    }

class CfcPutSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado"""
    id: int = 50
    
class CfcListagemSchema(BaseModel):
 """ Define como um novo produto a ser inserido deve ser representado"""
 id: int = 50
 codigo: str = "ac1215"
 nome: str = "Auto Escola de Jacarepagua"
 cnpj: str = "70.982.550/0001-39"
 status: bool = True
 regiao:str = "Jacarepagua"