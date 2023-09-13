from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    user_words: set[str] = field(default_factory=set)

    @property
    def words_count(self) -> int:
        return len(self.user_words)

    def is_used(self, word: str) -> bool:
        return word in self.user_words

    def add(self, word: str) -> None:
        self.user_words.add(word)

    def __repr__(self):
        return self.name

    __unicode__ = __str__ = __repr__