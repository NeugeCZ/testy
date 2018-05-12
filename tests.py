import pytest
from function import is_prime, print_next_prime, abc_random_string


class TestAbcRandomString:
    @pytest.fixture(params=[0, 1, 2, 4, 8, 16, 32, 64, 128])
    def length(self, request):
        return request.param

    def test_starts_with_abc(self, length):
        beginning = 'abc'
        assert abc_random_string(length)[:3] == beginning[:length]

    def test_string_length(self, length):
        assert len(abc_random_string(length)) == length

    def test_string_randomness(self, length):
        if length > 3:
            randomness_index = 0
            for i in range(10):
                if abc_random_string(length) == abc_random_string(length):
                    randomness_index += 1

            assert randomness_index < 4

    @pytest.fixture(params=['string', ['list'], ('tuple'), {'dict': 'withkey'}, 42.42])
    def structures(self, request):
        return request.param

    def test_wrong_structures_raises(self, structures):
        with pytest.raises(TypeError):
            assert abc_random_string(structures)

    def test_negative_length_raise(self):
        with pytest.raises(ValueError):
            assert abc_random_string(-42)

class TestIsPrime:
    @pytest.mark.parametrize("x,output", [
        (-6.66e2, False),
        (-2, False),
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (3.333, False),
        (11, True),
        (11.0000, True),
        (11.0001, False),
        (42, False),
        (4.2e1, False),
        (6481, True),
        (6483, False),
        (6.553e3, True),
        (16229, True),
        (100003, True),
        (2001037, True),
        (2001038, False)])

    def test_is_prime(self, x, output):
        assert is_prime(x) == output

    @pytest.fixture(params=['string', ['list'], ('tuple'), {'dict': 'withkey'}])
    def structures(self, request):
        return request.param

    def test_wrong_structures_raises(self, structures):
        with pytest.raises(TypeError):
            assert is_prime(structures)


class TestPrintNextPrime:
    @pytest.mark.parametrize("x, output", [
        (-100003331, 2),
        (-6.66e2, 2),
        (-42, 2),
        (-5.0, 2),
        (-3.3333, 2),
        (-2, 2),
        (0, 2),
        (1, 2),
        (2, 3),
        (3, 5),
        (5, 7),
        (7, 11),
        (8, 11),
        (10, 11),
        (1.011e1, 11),
        (6029.00042, 6037),
        (2002969, 2002993),
    ])

    def test_print_next_prime(self, x, output):
        assert print_next_prime(x) == output

    @pytest.fixture(params=['string', ['list'], ('tuple'), {'dict': 'withkey'}])
    def structures(self, request):
        return request.param

    def test_wrong_structures_raises(self, structures):
        with pytest.raises(TypeError):
            assert print_next_prime(structures)

