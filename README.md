# 2-Variable Plotter 

This repository exists purely to aid my learning of Python. As a result of this there are many comments that are probably not useful to others. The matplotlib and numpy libraries are required.

Usage instructions:

1. Download the files
2. Install python3
3. Download the matplotlib and numpy libraries as required
4. Open the 'Main' directory and edit 'settings.txt' to your liking
5. Run the 'plotter.py' script 
6. Proceed as instructed

What the script does:

The script will ask the user if any data pairs would like to be input (x and y). If yes, the data will be input and saved to a 'data.csv' file in the same directory as the .py file (the x_y_plotter directory). This step can be repeated to the user's liking. When the user has finished inputtng the data, a scatter plot will be displayed. The style of the plot can change to the user's liking, this can be done by editing the settings.txt file. A regression line (up to n^2) can also be shown. Since the data is stored in the 'data.csv' file the scatter plot can be amended over time.

Potential usefulness:

This can be used to gain insight to the relationship between two variables. Here is an example. The user may be a delivery driver who is payed per delivery, with the amount payed being some function of the total distance travelled. This person may wonder how their pay varies with distance. By inputting many past distance+pay pairs into the .csv file, the scatter plot displayed will provide insight.
