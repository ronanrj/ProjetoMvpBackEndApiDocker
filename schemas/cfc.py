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
    cep:str = "20780-200"

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
            "cep": cfc.cep 
        })  
                                   
    return{"cfcs": result}

class CfcViewSchema(BaseModel):
    """ Define como uma cfc será retornada: cfc + instrutor + carro. """
    id: int = 1
    codigo:str = "ab0000"
    nome:str = "Auto Escola Sem Nome"
    cnpj:str = "43515658000149"
    status = True
    cep = "20780-200"
    # ultima_atualizacao = datetime.now()
    instutores: List[InstrutorListagemSchema]
    carros:List[CarroViewSchema]
    
    
class CfcViewSchemaGet(BaseModel):
    """ Define como uma cfc será retornada: cfc + instrutor + carro. """
    id: int = 1
    codigo: str = "ab0000"
    nome: str = "Auto Escola Sem Nome"
    cnpj: str = "43515658000149"
    status: bool = True
    regiao: str = "Bairro"
    cep: str = "20780-200"
    logradouro: str = "Praça da Sé"
    complemento: str = "lado ímpar"
    bairro: str = "Sé"
    localidade: str = "São Paulo"
    uf: str = "SP"
    ibge: str = "3550308"
    gia: str = "1004"
    ddd: str = "11"
    siafi: str = "7107"
    ultima_atualizacao: datetime = datetime.now()
    instrutores: List[InstrutorListagemSchema]
    carros: List[CarroViewSchema]   
    
    
    
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
        "id": cfc.id,
        "codigo": cfc.codigo,
        "nome": cfc.nome,
        "cnpj": cfc.cnpj,
        "status": cfc.status,
        "cep": cfc.cep,
        "logradouro": cfc.logradouro,
        "complemento": cfc.complemento,
        "bairro": cfc.bairro,
        "localidade": cfc.localidade,
        "uf": cfc.uf,
        "ibge": cfc.ibge,
        "gia": cfc.gia,
        "ddd": cfc.ddd,
        "siafi": cfc.siafi,
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
 cep:str = "20780-200"