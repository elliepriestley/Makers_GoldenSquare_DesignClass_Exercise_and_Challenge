class TracksPlaylist():
    def __init__(self):
        self.tracks_listened_to = []

    def add(self, track_name):
        if type(track_name) == str:
            self.tracks_listened_to.append(track_name)
            return f"The track '{track_name}' has been added to your 'listened to' playlist."
        else:
            raise Exception("track_name variable must be a string.")

    def see_playlist(self):
        return self.tracks_listened_to
