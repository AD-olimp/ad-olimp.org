from typing import TypeVar, Protocol


D = TypeVar('D')
C = TypeVar('C')

class BaseMapper(Protocol):    
    def to_domain(item: C) -> D:
        ... 

    def to_controller(item: D) -> C:
        ...
        
