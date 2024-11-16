# phomemo_PM-241-BT
Repository containing a python script code capable to print a label on a PM-241-BT printer from phomemo.

# MacOS setup preparation
First go to Phomemo drivers website (https://eu.phomemo.com/pages/drivers) and download & install MacOS drivers (PM-241-BT series Driver setup package (mac)). Once printer´s driver is installed and printer is connected to PC over USB, use command `lpstat -p` in command line to check for available printers. At this phase, a printer with a name similar to `_PM_241_BT` should be found. 

If the label to print has `50mm x 25mm` size and the content to print is located in a file named `label.pdf`, the following command can be executed in the command line to print the label.

```
lp -d _PM_241_BT -o media=Custom.50x25mm label.pdf
```