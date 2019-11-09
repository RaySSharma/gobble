from gobble.gobble import gobble
import pytest

def test_gobbler_good_input():
    gobble(1)

def test_gobbler_bad_input():
    with pytest.raises(SystemExit):
        gobble('bad')
        gobble(1.1)

def test_gobbler_random():
    gobble()