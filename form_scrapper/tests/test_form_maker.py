from core.form_maker import check_type
from tests.test_data import TEST_TYPES


def test_check_type():
    for data, result in TEST_TYPES.items():
        assert check_type(data) == result, f'Return not {result}'
