import svn.common_base
from typing import Any

class Admin(svn.common_base.CommonBase):
    def __init__(self, svnadmin_filepath: str = ..., env: Any = ..., *args: Any, **kwargs: Any) -> None: ...
    def create(self, path: Any, svnadmin_filepath: str = ...): ...
