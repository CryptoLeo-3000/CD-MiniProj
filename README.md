# Compiler Design Mini Project

## Topic

Lyrics Displayer for Spotify

## By

Varun Khadayate

Simran Kumari

Kartik Padave

## About

The program is based on use of Regular Expression.

It Fetches the currently playing song from Spotify on Windows, Linux and macOS and displays the lyrics in the command-line, browser tab or in a desktop application (based on what the user selects).

## Requirements

Python 3

Python Library: swaglyrics (can be installed using command: pip install swaglyrics)

## How to use

1. Setup the program by running the command in CMD of you system. Command is: python setup.py

2. In command prompt run command 'swaglyrics' with an arguement as follow:

  Arguements          Actions

  -h, --help          show this help message and exit

  -t, --tab           Display lyrics in a browser tab.

  -c, --cli           Display lyrics in the command-line.

  -n, --no-issue      Disable issue-making on cli.

  -u, --update-check  Force check for updates.

<!--
## Usage

`usage: swaglyrics [-h] [-t] [-c] [-n]`

Either the tab or cli argument is required to output lyrics.

Arguments:

```
  -h, --help      show this help message and exit       
  -t, --tab       Display lyrics in a browser tab.      
  -c, --cli       Display lyrics in the command-line.   
  -n, --no-issue  Disable issue-making on cli.
```

You can quit by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd>.

Before using, you should check [USING.txt](swaglyrics/USING.txt) to comply with the Genius ToS. There's a copy
included inside the package as well.

Note: If you have trouble displaying Japanese/Chinese characters on the command-line, simply type `chcp 936` to change your code page. List of code pages can be found here: <https://en.wikipedia.org/wiki/Code_page>

## Community

- SwagLyrics participated in [Google Code-in 2019](https://g.co/gci) with CCExtractor Development.
- SwagLyrics participated in [Google Code-in 2018](https://g.co/gci) with CCExtractor Development.
- SwagLyrics participated in [Google Summer of Code 2019](https://g.co/gsoc) with CCExtractor Development.
The selected project can be found [here](https://summerofcode.withgoogle.com/projects/#5694893526089728).

## Changelog

- #### v1.2.0

  - Add Genius A/B support
  - Add support for Bollywood songs
  - Add update check only once per 24h
  - Add parameter to force update check

See [CHANGES.md](CHANGES.md) for prior release notes.

## Compiling SwagLyrics for Development

- Clone the repo by `git clone https://github.com/SwagLyrics/SwagLyrics-For-Spotify.git` or use ssh.
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.

## Improvements Planned

1. ~~Linux and macOS support **done**~~
2. ~~Better logging of unsupported songs, the isolated unsupported.txt is sub-optimal for multiple users since the
file will only update locally with songs which worked fine when it was just me but since I hope others use it too, I'll
try to add a better method with server support.~~
3. ~~Better tests to test all of the functionality. (cli.py fully tested!)~~ 100% code coverage
4. Perhaps a tiny app using Electron that could fit in your tray to be opened whenever you want lyrics for a song.
5. ~~Supporting more songs, currently the program sometimes fails at remixes since while the lyrics are same as
original,
 the artist is the remixer. **done**~~
6. Documenting all the files.

## SwagLyrics on Windows with Terminal

<p align="center">
  <img src="https://i.imgur.com/SRRbxbr.png" alt="SwagLyrics with Hyper">
</p>

## SwagLyrics on Windows with Firefox Side-View

<p align="center">
  <img src="https://i.imgur.com/TcSpbP9.png" alt="SwagLyrics with Side-View">
</p>

## Screencast - SwagLyrics on Linux

<p align="center">
  <a href="http://www.youtube.com/watch?v=-rxYcXAsO1U">
    <img src="https://i.imgur.com/v3iWyia.gif" alt="Watch the video">
  </a>
</p>

## Screencast - SwagLyrics on macOS

<p align="center">
  <a href="https://www.youtube.com/watch?v=XcobDTljMdM">
    <img src="https://i.imgur.com/7BVWB99.gif" alt="Watch the video">
  </a>
</p> -->
