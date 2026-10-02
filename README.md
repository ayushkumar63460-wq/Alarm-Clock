Python Alarm Clock

A simple command-line alarm clock developed in Python. The program allows the user to set an alarm for a specific time and plays an audio file when the specified time is reached.

Features

Set an alarm using the HH:MM:SS format.

Continuously displays the current system time.

Checks the alarm time every second.

Plays an MP3 audio file when the alarm time is reached.

Uses the Pygame library for audio playback.

Simple command-line interface.

Requirements

Before running the project, make sure you have:

Python 3.x

Pygame

An MP3 audio file

Installation
1. Install Python

Download and install Python 3.x if it is not already installed.

2. Install Pygame

Open a terminal or command prompt and run:

pip install pygame


Alternatively:

python -m pip install pygame

Project Structure

The project directory should contain the following files:

alarm-clock/
├── alarm.py
├── sound.mp3.mp3
└── README.md


The audio file should be placed in the same directory as the Python program.

Usage

Run the program using:

python alarm.py


The program will prompt you to enter the alarm time:

ENTER THE ALARM TIME (HH:MM:SS):


For example:

ENTER THE ALARM TIME (HH:MM:SS): 07:30:00


The program will then display the current time until the specified alarm time is reached.

Example:

Alarm set for 07:30:00.
07:29:57
07:29:58
07:29:59
07:30:00
WAKE UP!


Once the alarm time is reached, the specified audio file will play.

Audio File

The current program expects the audio file to be named:

sound.mp3.mp3


This filename is defined in the Python code:

alarm_sound = "sound.mp3.mp3"


If you want to use a different filename, update the variable accordingly. For example:

alarm_sound = "alarm.mp3"


Make sure the audio file is located in the same directory as alarm.py.

How It Works

The program follows these steps:

Prompts the user to enter an alarm time.

Retrieves the current system time.

Compares the current time with the specified alarm time.

Checks the time every second.

When the current time matches the alarm time, Pygame is initialized.

The alarm audio file is loaded and played.

The program waits until the audio finishes playing.

The program then terminates.

Libraries Used
time

The time module is used to pause execution for one second between each time check.

time.sleep(1)

datetime

The datetime module is used to retrieve and format the current system time.

datetime.datetime.now().strftime("%I:%M:%S")

pygame

The Pygame library is used to initialize the audio system and play the alarm sound.

pygame.mixer.init()
pygame.mixer.music.load(alarm_sound)
pygame.mixer.music.play()

Time Format

The program currently uses the 12-hour time format:

HH:MM:SS


For example:

07:30:00


The current implementation does not explicitly request AM or PM. For more flexible time handling, the program could be modified to support 24-hour time or an AM/PM input.

Future Improvements

Potential improvements include:

Add AM/PM support.

Add input validation.

Support 24-hour time format.

Allow users to select an audio file.

Add multiple alarms.

Add a snooze option.

Add a graphical user interface.

Add error handling for missing or invalid audio files.

Allow users to stop the alarm manually.

License

This project is intended for educational and personal use. You are free to modify and extend the project as needed.
