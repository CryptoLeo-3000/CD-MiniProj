import argparse
import os
import sys
import time
import tkinter
import requests
from SwSpotify import spotify, SpotifyNotRunning
from swaglyrics import unsupported_txt, SameSongPlaying, __version__ as version, backend_url, api_timeout
from swaglyrics.cli import lyrics, clear
from swaglyrics.tab import app


def unsupported_precheck(force: bool = False) -> None:
    """
    Checks if new version available and updates unsupported.txt from server.
    Runs only if 24h have elapsed since previous run or if forced via the -u flag.
    """
    if not force:
        # check 24h has elapsed since last update check
        with open(unsupported_txt, 'r', encoding='utf-8') as f:
            try:
                last_updated = float(f.readline())
                if time.time() - last_updated < 86400:  # 86400 seconds in a day
                    return None
            except ValueError:  # would occur if first line string, on initial versions of unsupported.txt
                pass
            except PermissionError as e:
                print("You should install SwagLyrics as --user or use sudo to access unsupported.txt.", e)
                sys.exit(1)
    try:
        v = requests.get(f'{backend_url}/version')
        ver = v.text
        if ver > version:
            print("New version of SwagLyrics available: v{ver}\nPlease update :)".format(ver=ver))
            print("To update, execute pip install -U swaglyrics")
    except requests.exceptions.RequestException:
        pass
    print('Updating unsupported.txt from server.')
    with open(unsupported_txt, 'w', encoding='utf-8') as f:
        try:
            unsupported_songs = requests.get(f'{backend_url}/song_lyrics_unsupported', timeout=api_timeout)
            last_updated = time.time()
            f.write(f'{last_updated}\n')
            f.write(unsupported_songs.text)
            print("Updated unsupported.txt successfully.")
        except requests.exceptions.RequestException as e:
            print("Could not update unsupported.txt successfully.", e)
        except PermissionError as e:
            print("You should install SwagLyrics as --user or use sudo to access unsupported.txt.", e)
            sys.exit(1)

def show_cli(make_issue: bool = False) -> None:

    try:
        song_lyrics = tkinter.Tk()
        song_lyrics.title("CD Mini Proj")

        song, artist = spotify.current()  # get currently playing song, artist
        words = tkinter.Message(song_lyrics, text=lyrics(song, artist, make_issue))
        words.pack()

        song_lyrics.after(30000, song_lyrics.destroy)
        tkinter.mainloop()

    except SpotifyNotRunning as e:
        song_lyrics = tkinter.Tk()
        song_lyrics.title("CD Mini Proj")

        words = tkinter.Message(song_lyrics, text=e)
        words.pack()

        song_lyrics.after(30000, song_lyrics.destroy)
        song_lyrics.mainloop()
        song, artist = None, None
    
    while True:
        # refresh every 5s to check whether song changed
        # if changed, display the new lyrics
        try:
            try:
                if spotify.current() == (song, artist):
                    raise SameSongPlaying
                else:
                    song_lyrics = tkinter.Tk()
                    song_lyrics.title("CD Mini Proj")

                    song, artist = spotify.current()  # get currently playing song, artist
                    words = tkinter.Message(song_lyrics, text=lyrics(song, artist, make_issue))
                    words.pack()

                    song_lyrics.after(30000, song_lyrics.destroy)
                    tkinter.mainloop()
            except (SpotifyNotRunning, SameSongPlaying):
                time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()

show_cli(True)