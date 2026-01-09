from immune_gems.media import apply_exchange_bounds

class DummyRxn:
    def __init__(self):
        self.lower_bound = 0.0

class DummyModel:
    def __init__(self):
        self.reactions = {"EX_o2[e]": DummyRxn()}
    def copy(self):
        return self

def test_apply_exchange_bounds():
    m = DummyModel()
    apply_exchange_bounds(m, {"EX_o2[e]": -1})
    assert m.reactions["EX_o2[e]"].lower_bound == -1.0
