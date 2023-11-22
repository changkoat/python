import pytest
from television import Television

def test_power_on_off():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_unmute():
    tv = Television()
    tv.power()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up_wrap_around():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_CHANNEL + 1):
        tv.channel_up()
    assert str(tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0"

def test_volume_up_max_limit():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_VOLUME + 1):
        tv.volume_up()
    assert str(tv) == f"Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}"
