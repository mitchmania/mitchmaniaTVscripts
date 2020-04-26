import stream
import threading
import rest_interface

def main():
    stream_thread = threading.Thread(target=stream.stream_main)
    stream_thread.start()
    rest_thread = threading.Thread(target=rest_interface.app.run)
    rest_thread.start()
    rest_thread.join()

if __name__ == "__main__":
    main()