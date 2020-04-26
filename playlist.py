import os
import sqlite3
import pdb

class Playlist():
    def __init__(self):
        self.index = -1
        self.db_uri = "file:test_db.sqlite"

        with sqlite3.connect(self.db_uri, uri=True) as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS pl")
            cur.execute("CREATE TABLE pl(idx integer, abs_path text)")
            conn.commit()

    def add_path_to_playlist(self, vid_path):
        i = 0

        with sqlite3.connect(self.db_uri, uri=True) as conn:
            cur = conn.cursor()
            for root, _, files in os.walk(os.path.abspath(vid_path)):
                for filename in files:
                    if filename.endswith(".mp4"):
                        abs_path = os.path.join(root, filename)
                        cur.execute("INSERT INTO pl VALUES (?,?)",(i,abs_path))
                        i += 1
            conn.commit()

    def get_next_vid(self):
        with sqlite3.connect(self.db_uri, uri=True) as conn:
            cur = conn.cursor()

            max_index = cur.execute("SELECT MAX(idx) FROM pl").fetchone()
            max_index = int(max_index[0])

            if self.index >= max_index:
                self.index = 0
            else:
                self.index += 1

            cur.execute("SELECT * FROM pl WHERE idx = ?",(self.index,))
            ans = cur.fetchone()

            return ans[1]