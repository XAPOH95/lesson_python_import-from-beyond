from src import NWO

def test_can_init_NWO():
    nwo = NWO(3.233_321, 32.333_444)
    print(nwo)
    print(nwo.calc_rate())