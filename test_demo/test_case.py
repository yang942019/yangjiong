import os

import pytest


@pytest.mark.webui
def test_01():
    print('webui')


def test_02():
    print('02')


def test_03():
    print('03')


@pytest.mark.interface
def test_04():
    print('interface')


if __name__ == '__main__':
    # pytest.main(['--alluredir', './temp'])
    os.system('allure generate ./temp -o ./report --clean')
