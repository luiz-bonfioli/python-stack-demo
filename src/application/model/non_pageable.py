import dataclasses
from typing import List, Generic, TypeVar

T = TypeVar('T')


@dataclasses.dataclass
class NonPageable(Generic[T]):
    content: List[T] = dataclasses.field(default_factory=list)

    def to_dict(self) -> dict:
        return dict(content=[r.to_dict() for r in self.content])
