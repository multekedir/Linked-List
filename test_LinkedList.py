import pytest

from main import LinkedList


@pytest.fixture
def create_linked_list():
    l_l = LinkedList()
    for i in range(10):
        l_l.append(i)
    return l_l


def test_append(create_linked_list):
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == create_linked_list.to_list()


def test_str(create_linked_list):
    assert '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' == str(create_linked_list)


def test_len(create_linked_list):
    assert 10 == len(create_linked_list)


def test_index(create_linked_list):
    assert create_linked_list.get(0) == 0


def test_over_index(create_linked_list):
    assert create_linked_list.get(10) is None


def test_remove(create_linked_list):
    create_linked_list.remove(5)
    assert 9 == len(create_linked_list)
    assert create_linked_list.get(5) == 6
