from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """ Define como a mensagem de erro será apresentada 
    """
    msg: str