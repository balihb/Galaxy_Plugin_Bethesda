import abc
from typing import (
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Mapping,
    MutableMapping,
    Tuple,
    TypeVar,
    Union,
    overload,
)

class istr(str): ...

upstr = istr

_S = Union[str, istr]

_T = TypeVar("_T")

_T_co = TypeVar("_T_co", covariant=True)

_D = TypeVar("_D")

class MultiMapping(Mapping[_S, _T_co]):
    @overload
    @abc.abstractmethod
    def getall(self, key: _S) -> List[_T_co]: ...
    @overload
    @abc.abstractmethod
    def getall(self, key: _S, default: _D) -> Union[List[_T_co], _D]: ...
    @overload
    @abc.abstractmethod
    def getone(self, key: _S) -> _T_co: ...
    @overload
    @abc.abstractmethod
    def getone(self, key: _S, default: _D) -> Union[_T_co, _D]: ...

_Arg = Union[Mapping[_S, _T], Dict[_S, _T], MultiMapping[_T], Iterable[Tuple[_S, _T]]]

class MutableMultiMapping(MultiMapping[_T], MutableMapping[_S, _T], Generic[_T]):
    @abc.abstractmethod
    def add(self, key: _S, value: _T) -> None: ...
    @abc.abstractmethod
    def extend(self, arg: _Arg[_T] = ..., **kwargs: _T) -> None: ...
    @overload
    @abc.abstractmethod
    def popone(self, key: _S) -> _T: ...
    @overload
    @abc.abstractmethod
    def popone(self, key: _S, default: _D) -> Union[_T, _D]: ...
    @overload
    @abc.abstractmethod
    def popall(self, key: _S) -> List[_T]: ...
    @overload
    @abc.abstractmethod
    def popall(self, key: _S, default: _D) -> Union[List[_T], _D]: ...

class MultiDict(MutableMultiMapping[_T], Generic[_T]):
    def __init__(self, arg: _Arg[_T] = ..., **kwargs: _T) -> None: ...
    def copy(self) -> MultiDict[_T]: ...
    def __getitem__(self, k: _S) -> _T: ...
    def __setitem__(self, k: _S, v: _T) -> None: ...
    def __delitem__(self, v: _S) -> None: ...
    def __iter__(self) -> Iterator[_S]: ...
    def __len__(self) -> int: ...
    @overload
    def getall(self, key: _S) -> List[_T]: ...
    @overload
    def getall(self, key: _S, default: _D) -> Union[List[_T], _D]: ...
    @overload
    def getone(self, key: _S) -> _T: ...
    @overload
    def getone(self, key: _S, default: _D) -> Union[_T, _D]: ...
    def add(self, key: _S, value: _T) -> None: ...
    def extend(self, arg: _Arg[_T] = ..., **kwargs: _T) -> None: ...
    @overload
    def popone(self, key: _S) -> _T: ...
    @overload
    def popone(self, key: _S, default: _D) -> Union[_T, _D]: ...
    @overload
    def popall(self, key: _S) -> List[_T]: ...
    @overload
    def popall(self, key: _S, default: _D) -> Union[List[_T], _D]: ...

class CIMultiDict(MutableMultiMapping[_T], Generic[_T]):
    def __init__(self, arg: _Arg[_T] = ..., **kwargs: _T) -> None: ...
    def copy(self) -> MultiDict[_T]: ...
    def __getitem__(self, k: _S) -> _T: ...
    def __setitem__(self, k: _S, v: _T) -> None: ...
    def __delitem__(self, v: _S) -> None: ...
    def __iter__(self) -> Iterator[_S]: ...
    def __len__(self) -> int: ...
    @overload
    def getall(self, key: _S) -> List[_T]: ...
    @overload
    def getall(self, key: _S, default: _D) -> Union[List[_T], _D]: ...
    @overload
    def getone(self, key: _S) -> _T: ...
    @overload
    def getone(self, key: _S, default: _D) -> Union[_T, _D]: ...
    def add(self, key: _S, value: _T) -> None: ...
    def extend(self, arg: _Arg[_T] = ..., **kwargs: _T) -> None: ...
    @overload
    def popone(self, key: _S) -> _T: ...
    @overload
    def popone(self, key: _S, default: _D) -> Union[_T, _D]: ...
    @overload
    def popall(self, key: _S) -> List[_T]: ...
    @overload
    def popall(self, key: _S, default: _D) -> Union[List[_T], _D]: ...

class MultiDictProxy(MultiMapping[_T], Generic[_T]):
    def __init__(
        self, arg: Union[MultiMapping[_T], MutableMultiMapping[_T]]
    ) -> None: ...
    def copy(self) -> MultiDict[_T]: ...
    def __getitem__(self, k: _S) -> _T: ...
    def __iter__(self) -> Iterator[_S]: ...
    def __len__(self) -> int: ...
    @overload
    def getall(self, key: _S) -> List[_T]: ...
    @overload
    def getall(self, key: _S, default: _D) -> Union[List[_T], _D]: ...
    @overload
    def getone(self, key: _S) -> _T: ...
    @overload
    def getone(self, key: _S, default: _D) -> Union[_T, _D]: ...

class CIMultiDictProxy(MultiMapping[_T], Generic[_T]):
    def __init__(
        self, arg: Union[MultiMapping[_T], MutableMultiMapping[_T]]
    ) -> None: ...
    def __getitem__(self, k: _S) -> _T: ...
    def __iter__(self) -> Iterator[_S]: ...
    def __len__(self) -> int: ...
    @overload
    def getall(self, key: _S) -> List[_T]: ...
    @overload
    def getall(self, key: _S, default: _D) -> Union[List[_T], _D]: ...
    @overload
    def getone(self, key: _S) -> _T: ...
    @overload
    def getone(self, key: _S, default: _D) -> Union[_T, _D]: ...
    def copy(self) -> CIMultiDict[_T]: ...

def getversion(
    md: Union[MultiDict[_T], CIMultiDict[_T], MultiDictProxy[_T], CIMultiDictProxy[_T]]
) -> int: ...
