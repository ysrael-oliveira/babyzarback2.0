from sqlalchemy import Column, String, Integer, Float

from model import Base

class Roupa(Base):
    __tablename__ = 'roupa'
    
    id = Column("id",Integer, primary_key = True, autoincrement = True)
    nome = Column("nome",String(100))
    categoria = Column("categoria",String(30))
    tamanho = Column("tam", String(10))
    valor_de_compra = Column("valor_compra", Float)
    valor_de_venda = Column("valor_venda", Float)
    
    def __init__(self, nome: str, categoria: str, tamanho: str, valor_de_compra: float, valor_de_venda: float):
        """
        Adiciona uma roupa ao banco de dados
        
        Argumentos:
            nome: breve descrição da roupa
            categoria: tipo da roupa: pijama, casa, sair
            tamanho: tamanho da roupa: 0-3m, 3-6m, 6-9m, 9-12m, 1y, 2y, ...
            valor_de_compra: valor em que a roupa foi comprada
            valor_de_venda: valor no qual a roupa possa ser vendida
        """
        self.nome = nome
        self.categoria = categoria
        self.tamanho = tamanho
        self.valor_de_compra = valor_de_compra
        self.valor_de_venda = valor_de_venda
    