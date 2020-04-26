import os


class Playlist():
    def __init__(self):
        self.pl = []
        self.index = -1

    def add_path_to_playlist(self, vid_path):
        for root, _, files in os.walk(os.path.abspath(vid_path)):
            for filename in files:
                if filename.endswith(".mp4"):
                    abs_path = os.path.join(root, filename)
                    self.pl.append(abs_path)

    def get_next_vid(self):
        self.index += 1
        return self.pl[self.index]