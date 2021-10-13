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

``` text
  Arguements          Actions

  -h, --help          show this help message and exit

  -t, --tab           Display lyrics in a browser tab.

  -c, --cli           Display lyrics in the command-line.

  -n, --no-issue      Disable issue-making on cli.

  -u, --update-check  Force check for updates.
```
