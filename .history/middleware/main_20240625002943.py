

from typing import Any


class customeMiddleware:
    def __init__(self,get_responce) -> None:
        
        self.get_responce=get_responce
    def __call__(self,request  ) -> Any:
        print("before")
        responce=self.get_responce()