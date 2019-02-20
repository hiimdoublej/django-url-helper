from . import utils

from urllib.parse import SplitResult


def test_add_param():
    url = '/search'
    modified = utils.add_param(url, 'q', 'somekeyword')
    assert '/search?q=somekeyword' == modified
    modified = utils.add_param(modified, 'l', 'somelocation')
    assert '/search?q=somekeyword&l=somelocation' == modified
    modified = utils.add_param(modified, 'l', 'someotherlocation')
    assert '/search?q=somekeyword&l=somelocation&l=someotherlocation' == modified


def test_toggle_param():
    url = '/search?wn=0'
    modified = utils.toggle_param(url, 'wn', '0')
    assert '/search' == modified
    modified = utils.toggle_param(modified, 'gg', '30')
    assert '/search?gg=30' == modified


def test_reset_param():
    url = '/search?wa=1%2C9'
    modified = utils.reset_param(url, 'wa', '0')
    assert '/search?wa=0' == modified


def test_remove_param():
    url = '/search?wa=1&wa=9&wa=8'
    modified = utils.remove_param(url, 'wa', '9')
    assert '/search?wa=1&wa=8' == modified
    url = '/search?wa=1&wa=9'
    modified = utils.remove_param(url, 'wa', '1')
    assert '/search?wa=9' == modified
    modified = utils.remove_param(modified, 'wa', '9')
    assert '/search' == modified


def test_purge_param():
    url = '/search?q=LiHaoLover&l=TaiChung'
    modified = utils.purge_param(url, 'q')
    assert '/search?l=TaiChung' == modified
    modified = utils.purge_param(modified, 'l')
    assert '/search' == modified


def test_parse_url():
    url = 'https://wajob.cc/search?q=OneNightFourTimes&l=TaiChung'
    o, q = utils.parse_url(url)
    expected = SplitResult(
        scheme='https',
        netloc='wajob.cc',
        path='/search',
        query='q=OneNightFourTimes&l=TaiChung',
        fragment=''
    )
    assert expected == o
    assert {'q': ['OneNightFourTimes'], 'l': ['TaiChung']} == q


def test_reconstruct_url():
    o = SplitResult(
        scheme='https',
        netloc='wajob.cc',
        path='/search',
        query='q=OneNightFourTimes&l=TaiChung',
        fragment=''
    )
    q = {'q': ['OneNightFourTimes'], 'l': ['TaiChung']}
    url = utils.reconstruct_url(o, q)
    assert url == 'https://wajob.cc/search?q=OneNightFourTimes&l=TaiChung'


def test_is_int():
    assert utils.is_int('notInt') is False
    assert utils.is_int('1') is True
