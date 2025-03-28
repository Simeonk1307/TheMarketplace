## define pydantic models for requests here

from pydantic import BaseModel


class Response(BaseModel):
    '''
        This response must be used by all other responses
        i.e. All response must contain these fields
    '''
    status: int
    success: bool
    message: str