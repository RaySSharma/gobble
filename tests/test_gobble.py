from gobble import gobble

def test_gobbler_good_input():
    gobble(1)

def test_gobbler_bad_input():
    gobble('bad')
    gobble(1.1)

def test_gobbler_random():
    gobble()