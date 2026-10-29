"""Proposed educational break overlay. Does not classify or modify bias."""
class BreakOverlay:
    def __init__(self):
        self.consumed = set()

    def discover(self, close, high=None, low=None):
        if high is not None and close > high[1]:
            self.consumed.add(('H', high[0]))
        if low is not None and close < low[1]:
            self.consumed.add(('L', low[0]))

    def update(self, previous_close, close, bias, high=None, low=None, valid=True):
        if not valid:
            return 0
        if high is not None and ('H',high[0]) not in self.consumed and previous_close <= high[1] < close:
            self.consumed.add(('H',high[0]))
            return 1 if bias == 1 else 2 if bias == -1 else 3
        if low is not None and ('L',low[0]) not in self.consumed and close < low[1] <= previous_close:
            self.consumed.add(('L',low[0]))
            return -1 if bias == -1 else -2 if bias == 1 else -3
        return 0
