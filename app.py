from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from sqlalchemy.exc import IntegrityError

from model import Session, Roupa
from schemas.roupa import RoupaSchema, RoupaGetSchema, ListaRoupasSchema, RoupaDelSchema, RoupaEditSchema, apresenta_roupa, apresenta_roupas
from schemas.error import ErrorSchema
from flask_cors import CORS

info = Info(title="Babyzar API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definir tags
home_tag = Tag(name="Documentação", description="Direciona para Swagger")
roupa_tag = Tag(name="Roupa", description="Inserção, consulta e deleção de roupas da base")

# define tela de início
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para openapi, para documentação como Swagger.
    """
    return redirect('/openapi')

# adicionar uma nova roupa
@app.post("/roupa", tags=[roupa_tag],
          responses={"200": RoupaSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_roupa(form: RoupaSchema):
    """
    Adiciona uma nova roupa à base de dados.
    """
    roupa = Roupa(
        nome = form.nome,
        categoria = form.categoria,
        tamanho = form.tamanho,
        valor_de_compra = form.valor_de_compra,
        valor_de_venda = form.valor_de_venda
    )
    try:
        session = Session()
        session.add(roupa)
        session.commit()
        return apresenta_roupa(roupa), 200
    
    except Exception as exc:
        msg_erro = "Erro ao adicionar este item!"
        return({"message": msg_erro}, 400)
    
@app.get("/roupa", tags=[roupa_tag],
          responses={"200": RoupaSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_roupa(query: RoupaGetSchema):
    """
    Busca uma roupa a partir de um id fornecido
    """
    roupa_id = query.id
    session = Session()
    roupa = session.query(Roupa).filter(Roupa.id == roupa_id).first()
    
    if not roupa:
        return {"message": "Item não encontrado"}, 400
    else:
        return apresenta_roupa(roupa), 200
    
# consulta de todas as roupas no banco de dados
@app.get("/roupas", tags=[roupa_tag],
          responses={"200": ListaRoupasSchema, "400": ErrorSchema})
def get_roupas():
    """
    Busca todas as roupas presentes no banco de dados
    """
    session = Session()
    roupas = session.query(Roupa).all()
    
    if not roupas:
        return {"roupas": []}, 200
    else:
        return apresenta_roupas(roupas), 200

# apaga uma roupa do banco de dados
@app.delete("/roupa", tags=[roupa_tag],
            responses={"200": RoupaDelSchema, "404": ErrorSchema})
def delete_roupa(query: RoupaGetSchema):
    """
    Apaga uma roupa do banco de dados, após ser vendida
    """
    roupa_id = query.id
    session = Session()
    count = session.query(Roupa).filter(Roupa.id == roupa_id).delete()
    session.commit()
    
    if count:
        return {"message": f"Roupa {roupa_id} deletada com sucesso!"}
    else:
        return {"message": "Erro ao deletar a roupa!"}, 404

#atualiza preco de uma roupa
@app.put("/roupa", tags=[roupa_tag],
         responses={"200": RoupaSchema, "409": ErrorSchema, "400": ErrorSchema})
def atualiza_roupa(form: RoupaEditSchema):
    """
    Atualiza o preço de uma roupa no banco de dados, pelo id
    """
    roupa_id = form.id
    session = Session()
    roupa = session.query(Roupa).filter(Roupa.id == roupa_id).first()
    
    #valida se roupa foi encontrada
    if not roupa:
        return {"message": f"Roupa não foi encontrada no sistema"}, 400
    
    if roupa:
        roupa.valor_de_venda = form.valor_de_venda
        try:
            session.commit()
            return {"message": f" Preço de roupa {roupa_id} atualizado com sucesso!"}
        except Exception as e:
            return {"message": "Erro ao atualizar o preço. Favor entrar em contato com suporte"}, 404