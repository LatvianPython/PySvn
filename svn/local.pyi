import svn.common
from collections import namedtuple
from typing import Any, Optional

_STATUS_ENTRY = namedtuple('_STATUS_ENTRY', ['name', 'type_raw_name', 'type', 'revision'])

class LocalClient(svn.common.CommonClient):
    def __init__(self, path_: Any, *args: Any, **kwargs: Any) -> None: ...
    def add(self, rel_path: Any, do_include_parents: bool = ...) -> None: ...
    def commit(self, message: Any, rel_filepaths: Any = ...) -> None: ...
    def update(self, rel_filepaths: Any = ..., revision: Optional[Any] = ...) -> None: ...
    def cleanup(self) -> None: ...
    def status(self, rel_path: Optional[Any] = ...) -> None: ...
    def remove(self, rel_path: Any, do_keep_local: bool = ..., do_force: bool = ...) -> None: ...
