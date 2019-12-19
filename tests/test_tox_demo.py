#!/usr/bin/env python

"""Tests for `tox_demo` package."""

import pytest


from tox_demo import tox_demo


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_bubble():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    tox_demo.bubbleSort(alist)
    # assert alist == [54, 26, 93, 17, 77, 31, 44, 55, 20]
