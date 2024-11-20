from typing import Optional
from fastapi import HTTPException, Header, status

ATLYS_TOKEN = "atlys-token"

class Authenticator: 
    def authenticate(x_token: Optional[str] = Header(None)):
        if x_token != ATLYS_TOKEN:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return x_token