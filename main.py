import playlist
import stream
import sys
import threading
import rest_interface


def main():
    my_pl = playlist.Playlist()
    my_pl.add_path_to_playlist(sys.argv[1])

    stream_thread = threading.Thread(target=stream.stream_main, args=(my_pl,))
    stream_thread.start()
    # rest_thread = threading.Thread(target=rest_interface.app.run)
    # rest_thread.start()
    
    stream_thread.join()

if __name__ == "__main__":
    main()