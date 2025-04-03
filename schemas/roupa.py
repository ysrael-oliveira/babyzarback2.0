from pydantic import BaseModel
from typing import Optional, List
from model.roupa import Roupa

class RoupaSchema(BaseModel):
    """ Define como uma nova roupa deve ser representada 
    """
    nome: str = "Conjunto Body"
    categoria: str = "Casa"
    tamanho: str = "0-3m"
    valor_de_compra: float = 150
    valor_de_venda: Optional[float] = 100
    
class RoupaGetSchema(BaseModel):
    """ Define como buscar a roupa, pelo id"""
    id: int = 1

class ListaRoupasSchema(BaseModel):
    """ Define como a lista de roupas deve ser retornada
    """
    roupas: List[RoupaSchema]
    
class RoupaDelSchema(BaseModel):
    """ Define o modelo de resposta caso a roupa seja deletada com sucesso
    """
    message: str
    
class RoupaEditSchema(BaseModel):
    """ Define como atualizar o preço de uma roupa, pelo id
    """
    id: int = 1
    valor_de_venda: Optional[float] = 80
    
def apresenta_roupa(roupa: Roupa):
    """ Retorna a representação da roupa """
    return {
        "id": roupa.id,
        "nome": roupa.nome,
        "categoria": roupa.categoria,
        "tamanho": roupa.tamanho,
        "valor_de_compra": roupa.valor_de_compra,
        "valor_de_venda": roupa.valor_de_venda
    }
    
def apresenta_roupas(roupas: List[Roupa]):
    lista = []
    for roupa in roupas:
        lista.append({
            "id": roupa.id,
            "nome": roupa.nome,
            "categoria": roupa.categoria,
            "tamanho": roupa.tamanho,
            "valor_de_compra": roupa.valor_de_compra,
            "valor_de_venda": roupa.valor_de_venda
        })
    return {"roupas": lista}
