# 2-Variable Plotter 

This partly exists to aid my learning of Python. As a result of this there are some comments that will not be useful to others. The matplotlib and numpy libraries are required.

Instructions:

1. Download the files and unzip them
2. Install [python3](https://www.python.org/downloads/)
3. Download the matplotlib and numpy libraries if do not already have them (use [pip](https://pip.pypa.io/en/stable/installing/) to do this)
4. Open the 'Main' directory and edit the 'settings.txt' file to your liking
5. Run the 'plot.py' script (typing 'python3 plot.py' into the terminal is the easiest way of doing this)
6. Proceed as instructed

What the script does:

The script will ask the user if they would like to input any data. The data will be input and saved to a 'data.csv' file in the 'Main' directory. This step can be repeated to the user's liking. When the user has finished inputtng the data, a scatter plot will be displayed. The style of the plot can be changed by editing the settings.txt file. A regression line (up to n^2) can also be shown. Since the data is stored in the 'data.csv' file the data can be amended over time.

Potential usefulness:

This can be used to gain insight to the relationship between two variables. Here is an example. The user may be a delivery driver who is payed per delivery, with the amount payed being some function of the total distance travelled. This user may want some insight to this function. With enough data points a relationship can be shown.
