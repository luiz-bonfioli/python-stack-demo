import dataclasses
from typing import List, Optional, Generic, TypeVar

T = TypeVar('T')


@dataclasses.dataclass
class Pageable(Generic[T]):
    content: List[T] = dataclasses.field(default_factory=list)
    cursor: Optional[str] = dataclasses.field(default=None)

    def to_dict(self):
        return {'content': [value.to_dict() for value in self.content], 'cursor': self.cursor}
