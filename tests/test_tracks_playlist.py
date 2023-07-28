from lib.tracks_playlist import * 
import pytest

def test_creating_instance_of_class_Tracks_Playlist():
    user1_playlist = TracksPlaylist()
    result = user1_playlist.tracks_listened_to
    assert result == []


def test_add_method_appends_to_tracks_listened_to():
    user1_playlist = TracksPlaylist()
    user1_playlist.add("Cruel Summer, Taylor Swift")
    result = user1_playlist.tracks_listened_to
    assert result == ["Cruel Summer, Taylor Swift"]


def test_add_method_returns_appropriate_string():
    user1_playlist = TracksPlaylist()
    result = user1_playlist.add("Cruel Summer, Taylor Swift")
    assert result == "The track 'Cruel Summer, Taylor Swift' has been added to your 'listened to' playlist."


def test_add_method_argument_is_string_data_type():
    user1_playlist = TracksPlaylist()
    with pytest.raises(Exception) as e:
        user1_playlist.add(100)
        user1_playlist.add(True)
        user1_playlist.add(6.7)
        user1_playlist.add([1, 2, 3])
        user1_playlist.add({'key':'value'})
    error_message = str(e.value)
    assert error_message == "track_name variable must be a string."


    
def test_see_playlist_method_returns_public_list():
    user1_playlist = TracksPlaylist()
    user1_playlist.add("Cruel Summer, Taylor Swift")
    user1_playlist.add("Hello, World")
    user1_playlist.add("September, EW&F")
    user1_playlist.add("Silk Chiffon, MUNA")
    result = user1_playlist.see_playlist()
    assert result == ["Cruel Summer, Taylor Swift", "Hello, World", "September, EW&F", "Silk Chiffon, MUNA"]


