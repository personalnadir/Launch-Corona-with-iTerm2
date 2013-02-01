# Instructions

## Requirements
These scripts require [Alfred with the Powerpack installed](http://www.alfredapp.com/powerpack/). Without the Powerpack you won't be able to run any extensions.

These scripts assume [Corona](http://www.coronalabs.com/) has been installed in __/Applications/CoronaSDK__ and that there's a Corona Terminal executable. They also assume that [iTerm 2](http://www.iterm2.com/#/section/home) has been installed.

The Python script has only been tested against version 2.7.3.

## How to install
Open Alfred's preference pane and add a new Shell Script. Name it as you please - I tend to use __Launch Corona with iTerm 2__. You might want to put the [GitHub address](https://github.com/personalnadir/Launch-Corona-with-iTerm2) in as the web address, in case you want to check for updates. 

Click create.

Now you will see the configuration pane for the extension. Give it a sensible title (again I use __Launch Corona with iTerm 2__) and description (__Launches project in Corona__).

Next you'll need to specify the keyword or command you want to use to run this script from Alfred. I use __corona__, but go with what ever is memorable for you, I would stick to a single word though.

In the command box enter the following:  
`python -u corona_launch.py __path_to_search__ {query}`

Replace __path_to_search__ with the folder where you want the script to look for your projects. On my mac that's a directory called Programming in my home directory, so I pass in /Users/username/Programming. The more specific the directory, the faster the script will run.

On the Parameter dropdown select "Required Parameter".

If you have [Growl](http://growl.info/) installed you can get messages from the script to appear as notifications. To do that click on the Advanced Tab over the command field and check "Display script output in Growl". 

Next you'll need to manually copy the Python and AppleScript scripts into the directory Alfred has created for this extension. That will be in the __Alfred/extensions/scripts/__ directory, which will either live in your Dropbox folder if you have syncing enabled, or (I think) __~/Library/Application Support/__

## How to run it
With everthing set up simply type `corona __project_name__` in Alfred, if everything works the scripts will start iTerm 2 and launch Corona Terminal with the project you requested.

## How it works
Basically the python script searches for a folder with the name you passed as the argument to Alfred. It will restrict its search to the directory you specified in the command box in the configuration pane for the script. If it finds a directory with a matching name (case insensitive), then searches all subdirectories of that folder for a main.lua file. If it finds that, it passes that to the applescript which tells Corona Terminal to open it!

Complicated, but worth it!

## Limitations
In my experience, Corona Terminal won't accept file paths with spaces in them. So trying to launch a main.lua file in "Raging Birds" directory won't work unfortunately.
