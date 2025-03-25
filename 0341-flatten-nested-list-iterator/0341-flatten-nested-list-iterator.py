class NestedIterator:
    def __init__(self, nestedList):
        def flatten(nested):
            for item in nested:
                if item.isInteger():
                    yield item.getInteger()
                else:
                    yield from flatten(item.getList())
        self.generator = flatten(nestedList)
        self.next_val = None
        self._advance()
    
    def _advance(self):
        try:
            self.next_val = next(self.generator)
        except StopIteration:
            self.next_val = None
    
    def next(self):
        if self.next_val is None:
            return None
        result = self.next_val
        self._advance()
        return result
    
    def hasNext(self):
        return self.next_val is not None