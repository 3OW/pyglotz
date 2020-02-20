from pyglotz.glotz import *
from time import time

import pytest

GLOTZ_API_KEY = '9DAF49C96CBF8DAC'


def test_get_show():
    g = Glotz(GLOTZ_API_KEY)
    result = g.get_show(tvdb_id='121361', language='de')
    assert isinstance(result, Show)

    with pytest.raises(MissingParameters):
        g.get_show(tvdb_id='', language='de')
    with pytest.raises(IDNotFound):
        g.get_show(tvdb_id='0', language='de')
    with pytest.raises(IDNotFound):
        g.get_show(tvdb_id='1', language='de')


def test_get_show_list():
    g = Glotz(GLOTZ_API_KEY)
    show_list = g.get_show_list('dexter', 'de')
    assert isinstance(show_list, list)
    assert isinstance(show_list[0], Show)

    with pytest.raises(ShowNotFound):
        g.get_show_list('uuuuuuuuuuuuu', 'de')


def test_show_search():
    g = Glotz(GLOTZ_API_KEY)
    show = g.show_search('dexter', 'de')
    assert isinstance(show, list)
    assert isinstance(show[0], Show)

    with pytest.raises(ShowNotFound):
        g.show_search('uuuuuuuuuuuuu', 'de')


def test_episode_by_id():
    g = Glotz(GLOTZ_API_KEY)
    episode = g.episode_by_id(3254641, 'de')
    assert isinstance(episode, Episode)

    with pytest.raises(EpisodeNotFound):
        g.episode_by_id(0, 'de')


def test_lookup_tvdb():
    g = Glotz(GLOTZ_API_KEY)
    result = g.lookup_tvdb(121361, 'de')
    assert isinstance(result, Show)

    with pytest.raises(IDNotFound):
        g.lookup_tvdb(0, 'de')
    with pytest.raises(IDNotFound):
        g.lookup_tvdb(1, 'de')


def test_get_show_aliases():
    g = Glotz(GLOTZ_API_KEY)
    aliases = g.get_show_aliases(0)
    assert isinstance(aliases, list)
    aliases = g.get_show_aliases(1)
    assert aliases == '[]'


def test_get_actors_list():
    g = Glotz(GLOTZ_API_KEY)
    actors = g.get_actors_list(121361)
    assert isinstance(actors, list)
    assert isinstance(actors[0], Actor)

    with pytest.raises(ActorNotFound):
        g.get_actors_list(0)


def test_get_banners():
    g = Glotz(GLOTZ_API_KEY)
    banners = g.get_banners(121361)
    assert isinstance(banners, list)
    assert isinstance(banners[0], Banner)

    with pytest.raises(BannersNotFound):
        g.get_banners(0)


def test_get_show_updates():
    g = Glotz(GLOTZ_API_KEY)
    updates = g.get_show_updates(int(time()) - 604800)
    assert isinstance(updates, list)

# TODO: add further tests
