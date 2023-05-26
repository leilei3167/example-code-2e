import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # 有点类似于__str__,但是后者更偏向打印的美观输出
    # __repr__可用于交互式解释器的输出(默认的输出是类名+引用的地址)
    # 在没有提供__str__方法的情况下打印,实际调用的是__repr__
    # 提倡所有的类都提供__repr__
    def __repr__(self):
        return "from __repr__"

    def __str__(self):
        return "this is from __str__"
