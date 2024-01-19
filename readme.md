# grouchforUTK

## About

A registration aid for students at UTK based JIceberg's grouch for Georgia Tech. I just swapped out the url for one that works with UTK's system.

I also "added" (more like forced in) support for a discord webhook to send you notifications that way, if that is something you are interested in.

## Installation

To use this project, you need Python 3.8+ installed as well as pip on your device.

* Clone the repo: git clone `https://github.com/karatedg/grouchforutk.git`

* Open the root of the project and open a CLI (command line interface) like powershell

* Install the necessary requirements `pip install -r requirements-<os>.txt` (note that mac users need to use requirements-unix.txt)

That should be it.

## Usage

### Tracker

The simplest usage is to simply run `python src/tracker.py [SEASON] CRN-1 CRN-2 ...` in the CLI.
For the season, use 'spring', 'fall', or 'summer'. An example call is below
```sh
user@computer:~$ python tracker.py fall 82693 89515 ...
```

If you know what you're doing more than I did when changing this then you can
use the tools in the library to configure your own notifications and reminders. JIceberg
made some `notifier` and `courses` handlers for easy use. If you want to remove the prebuilt discord webhook. That is currently
hiding in the send function of notifier.

An example of a custom program would be
```python
from courses import Course, WaitlistNotifier

myCourse = Course(crn, 'fall')
notif = WaitlistNotifier(myCourse)

notif.run()
```
To run it, just do `python path/to/file.py`.

### Info

From the CLI, run `python info.py [SEASON] CRN-1 CRN-2 ...` and a notification will be sent
containing information for the class. This does not loop, unlike the tracker.
