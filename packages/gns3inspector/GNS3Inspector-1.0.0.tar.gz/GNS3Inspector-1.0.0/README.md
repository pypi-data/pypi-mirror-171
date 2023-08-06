# GNS3Inspector

## Overview
A simple python-package to help get an overview of what is configured in a network-project that was created using GNS3. It also allows to configure several routers at the same time.

**NOTE**: This tool doesn't verify any of the inputs you give to it. You should know what you're doing. Preferably you should run the commands on one router to see if they work. If they work as intended, you can use `gns3inspector` for an easier way to deploy the same configuration to other routers.

*This tool was written to make your life a little easier using GNS3. It doesn't aim to be perfect or solve all the problems GNS3 has. I just wrote it quickly to help my group solve a university assignment easier. Feedback is still welcome, just hmu here on GitHub.*

## Installation
Simply run `pip install gns3inspector` to install the package. By adding `.local/bin` to your `PATH` variable, you can use the command `gns3inspector` from any directory.

`gns3inspector` uses the readline-library, to make it work make sure `ncurses-dev` is installed via `apt`.

## Usage
Navigate to your GNS3 project directory (where the `*.gns3`-file is located), and open a terminal there. Then run `gns3inspector` to start the tool. If you opened a valid GNS3-project-directory, you will now see a terminal input `>>> ` indicating that you can now run `gns3inspector` commands to see your project.

## gns3inspector commands
The letter in parantesis can be used as a shortcut to run the commands, e.g. `help` will open the help-text, but `h` will also do that.
- **(h)elp**: Shows a list of the available commands
- **(l)ist**: Shows all the routers in the current project. It generates abbreviations and id's for each router, which can be used to not have to write out the full router name each time.
- **(s)elect**: select the following device(s) as shown in (l)ist. E.g. TeleStar_R1 or TS_R1 or 3. The id's can also be selected as ranges, e.g. 3-5 or 4-9. 
To select all devices leave the parameter empty, defaults to all devices.
- **(c)config**: shows all commands in the configuration starting with the provided prefix, e.g. "interface f/." If no parameter is provided, all the startup configuration is shown. 
- **(e)dit**: Like c, but now the selected configuration can be edited in a file called tmp_gns3.txt in the current working directory. **Make sure that all the devices whose configuration you would like to edit are turned off in GNS3 before using this command!**
- **(r)eload**: reloads all the router's startup config files from disk
- **exit**: or quit, ends the shell 

