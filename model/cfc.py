from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base , Instrutor , Carro


class Cfc(Base):
    __tablename__ = 'cfc'
    
    id = Column(Integer, primary_key=True, unique=True)
    codigo = Column(String(20), unique=True)
    nome = Column(String(100))
    cnpj = Column(String(20))
    status = Column(Boolean)
    cep = Column(String(10))
    logradouro = Column(String(100))
    complemento = Column(String(100))
    bairro = Column(String(50))
    localidade = Column(String(50))
    uf = Column(String(2))
    ibge = Column(String(10))
    gia = Column(String(10))
    ddd = Column(String(3))
    siafi = Column(String(10))
    ultima_atualizacao = Column(DateTime,default=datetime.now())   
    instrutores = relationship("Instrutor")
    carros = relationship("Carro")
    
    
    def __init__(self, codigo: str, nome: str, cnpj: str, status: Boolean, cep: str,
                 logradouro: str, complemento: str, bairro: str, localidade: str, uf: str, ibge: str,
                 gia: str, ddd: str, siafi: str, ultima_atualizacao: Union[DateTime, None] = None):
        """
        Cria uma Cfc

        Arguments:
            codigo: código único da autoescola
            nome: nome da autoescola
            cnpj: CNPJ da autoescola
            status: se a autoescola está ativa
            cep: CEP da autoescola
            logradouro: logradouro do endereço
            complemento: complemento do endereço
            bairro: bairro do endereço
            localidade: cidade do endereço
            uf: unidade federativa do endereço
            ibge: código IBGE do município
            gia: código GIA do município
            ddd: código DDD do telefone
            siafi: código SIAFI do município
            ultima_atualizacao: data de quando o CFC teve a última atualização
        """       
        self.codigo = codigo
        self.nome = nome
        self.cnpj = cnpj
        self.status = status
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi
        if ultima_atualizacao:
            self.ultima_atualizacao = ultima_atualizacao
          
    def adiciona_instrutor(self, instrutor:Instrutor):
       """ Adiciona um novo instrutor na cfc """
       self.instrutores.append(instrutor)
                 
    def adiciona_carro(self, carro:Carro):
       """ Adiciona um novo carro na cfc """
       self.carros.append(carro)                 
