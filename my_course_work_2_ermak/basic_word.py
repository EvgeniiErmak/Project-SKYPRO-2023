from dataclasses import dataclass, field


@dataclass
class BasicWord:
    word: str
    subwords: list[str] = field(default_factory=list)

    @property
    def subwords_amount(self):
        return len(self.subwords)

    def is_correct(self, word: str) -> bool:
        return word in self.subwords

    def __repr__(self):
        return self.word.upper()

    __unicode__ = __str__ = __repr__
