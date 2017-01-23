class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError("only positive numbers available")
        super().append(x)

def test():
    pl = PositiveList([1, 2, 3, 4])
    assert len(pl) == 4

if __name__ == "__main__":
    test()