#############################################################################################################
#import
from statistics import mode #used for calculating mode
import csv #importing module allowing me to manipulate csv files easier
import matplotlib.pyplot as plt #from the matplotlib library import the pyplot module, refer to this as 'plt'
import numpy as np #numpy is used for the handling of arrays

#############################################################################################################
#importing setttings from settings.txt and setting variables to these settings for later use. handling errors

f = open('settings.txt','r') #opening the settings file
lines = f.readlines() #defining lines to be a list of all lines. these can be indexed 
try:
    prompt_user_to_edit_settings = str((lines[19].split())[2])
    if prompt_user_to_edit_settings not in ('y','Y','n','N'):
        print("""The 'prompt_user_to_edit_settings' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
        prompt_user_to_edit_settings = str('y')
except:
    print("""The 'prompt_user_to_edit_settings' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
    prompt_user_to_edit_settings = str('y')

try:
    prompt_user_to_input_data = str((lines[20].split())[2])
    if prompt_user_to_input_data not in ('y','Y','n','N'):
        print("""The 'prompt_user_to_input_data' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
    """)
        prompt_user_to_input_data = str('y')      
except:
    print("""The 'prompt_user_to_input_data' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
    prompt_user_to_input_data = str('y')
try:
    x_name = str((lines[21].split())[2]) #defining x_name to be the 3rd word on the 18th line. python counts from 0
except:
    print("""The 'x_name' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (x) will be used
""")
    x_name = str('x')
try:
    y_name = str((lines[22].split())[2])
except:
    print("""The 'y_name' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
    y_name = str('y')
try:
    grid_true = str((lines[23].split())[2])
    if grid_true not in ('y','Y','n','N'):
        print("""The 'grid_true' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (n) will be used
""")
        grid_true = str('n')
except:
    print("""The 'grid_true' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (n) will be used
""")
    grid_true = str('n')
try:
    force_axes_start_0_true = str((lines[24].split())[2])
    if force_axes_start_0_true not in ('y','Y','n','N'):
        print("""The force_axes_start_0_true'' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
    """)
        force_axes_start_0_true = str('y')  
except:
    print("""The 'force_axes_start_0_true' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
    force_axes_start_0_true = str('y')
try:
    dark_mode_true = str((lines[25].split())[2])
    if dark_mode_true not in ('y','Y','n','N'):
        print("""The 'dark_mode_true' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
        dark_mode_true = str('y')
except:
    print("""The 'dark_mode_true' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
    dark_mode_true = str('y')
try:
    marker_size = float((lines[26].split())[2])
except:
    print("""The 'marker_size' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (30) will be used
""")
    marker_size = float(30)
try:
    marker_color = str((lines[27].split())[2])
except:
    print("""The 'marker_color' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (w) will be used
""")
    marker_color = str('w')
try:
    marker_style = str((lines[28].split())[2])
except:
    print("""The 'marker_style' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (x) will be used
""")
    marker_style = str('x')
try:
    show_regression_line_degree1 = str((lines[29].split())[2])
    if show_regression_line_degree1 not in ('y','Y','n','N'):
        print("""The 'show_regression_line_degree1' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
        show_regression_line_degree1 = str('y')
except:
    print("""The 'show_regression_line_degree1' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
    show_regression_line_degree1 = str('y')

try:
    regression_line_degree1_color = str((lines[30].split())[2])
except:
    print("""The 'regression_line_degree1_color' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (g) will be used
""")
    regression_line_degree1_color = str('g')
try:
    regression_line_degree1_style = str((lines[31].split())[2])
    if regression_line_degree1_style not in ('-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'):
        print("""The 'regression_line_degree1_style' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (-) will be used
""")
        regression_line_degree1_style = '-'
except:
    print("""The 'regression_line_degree1_style' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (-) will be used
""")
    regression_line_degree1_style = '-'
try:
    show_regression_line_degree2 = str((lines[32].split())[2])
    if show_regression_line_degree2 not in ('y','Y','n','N'):
        print("""The 'show_regression_line_degree2' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (n) will be used
""")
        show_regression_line_degree2 = str('n')
        
except:
    print("""The 'show_regression_line_degree2' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (n) will be used
""")
    show_regression_line_degree2 = str('n')
try:
    regression_line_degree2_color = str((lines[33].split())[2])
except:
    print("""The 'regression_line_degree2_color' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (c) will be used
""")
    regression_line_degree2_color = str('c')
try:
    regression_line_degree2_style = str((lines[34].split())[2])
    if regression_line_degree2_style not in ('-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'):
        print("""The 'regression_line_degree2_style' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (-) will be used
""")
        regression_line_degree2_style = '-'
except:
    print("""The 'regression_line_degree2_style' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (-) will be used
""")
    regression_line_degree2_style = '-'
try:
    regression_line_extension_multiplier = float((lines[35].split())[2])
except:
    print("""The 'regression_line_extension_multiplier' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (0.05) will be used
""")
    regression_line_extension_multiplier = float(0.05)
try:
    show_extra_details = str((lines[36].split())[2])
    if show_extra_details not in ('y','Y','n','N'):
        print("""The 'show_extra_details' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
        show_extra_details = str('y')
except:
    print("""The 'show_extra_details' parameter has been changed incorrectly in the settings.txt file. <--- READ
The default value (y) will be used
""")
    show_extra_details = str('y')

f.close()

#############################################################################################################
#initial inputs

def firstquestion(): #function that asks user what to do
    
    answer = input("Do you want to input another " + x_name + "/" + y_name + " pair? (Y/N): ")
    
    if answer in ('Y','y','Yes','yes',''): #finding answer
        try:
            x = float(input("Input " + x_name + " (x-axis): ")) #input x
            y = float(input("Input " + y_name + " (y-axis): ")) #input y
            file = open('data.csv','a') #locate data.csv
            writer = csv.writer(file) #parse data.csv
            writer.writerow([x,y]) #add a row for the data the user just input
            file.close()
            return True #does not break loop
        except:
            print("Please enter a real number")
            return True
    elif answer in ('N','n','No','no'): #finding answer
        try: #the code in the try block checks over data.csv. it must pass these checks for the code to continue
            file = open('data.csv','r') #the data.csv file must exist in the same directory
            reader = csv.reader(file)
            for row in reader:
                temp = float(row[0]) #the data type must be float
                temp = float(row[1])
            file.close()
            temp = ''
            return False #fails checks
        except:
            print("""
The 'data.csv' file is either missing or corrupted. It should be in the same directory as 'plot.py'.
If it is missing simply use this program to enter data to generate it.
If it is corrupted either edit it directly or delete it and then use this program to enter data.
""")
            return True #if no data.csv file is found the loop is not broken
            
            
                
    else:
        print("Please enter a valid answer")
        return True #user is prompted to answer a valid answer. loop not broken

if prompt_user_to_edit_settings in ('n','N'):
    pass
else:
    print("""Editing the 'settings.txt' file would be worthwhile - you can remove this message by doing so.
""")

if prompt_user_to_input_data in ('n','N'):
    pass
else:
    repeat = True #defining repeat
    while repeat == True:
        repeat = firstquestion() #repeat is defined as what is returned from the function

#############################################################################################################
#generating lists for x and y

file = open('data.csv','r') #referencing the csv file
reader = csv.reader(file) #parsing the csv file. There is no need for the csv file to be sorted hence I do not bother doing this

x_list = [] #defining empty x list
y_list = [] #defining empty y list

for row in reader:  #iterates through each row
    x_list.append(float(row[0])) #adding the first piece of data in the row to the x list 
    y_list.append(float(row[1])) #adding the second piece of data in the row to the y list
file.close()

#############################################################################################################
#extra details

x_array = np.array(x_list) #converting lists to numpy arrays. this is so I can use the numpy methods
y_array = np.array(y_list)

x_std = str(np.std(x_array)) #standard deviation
x_range = str((np.amax(x_array))-(np.amin(x_array))) #range 
x_list_length = len(x_list)
x_mean = str(((sum(x_list))/x_list_length)) #mean
x_list_sorted = sorted(x_list)
if x_list_length % 2 == 0: 
    x_median_lower = x_list_sorted[int((x_list_length/2)-1)]
    x_median_higher = x_list_sorted[int((x_list_length/2))]
    x_median = str(((x_median_lower)+(x_median_higher))*0.5)
else:
    x_median = str(x_list_sorted[x_list_length//2]) #median
x_mode = str(mode(x_array)) #mode

y_std = str(np.std(y_array)) #standard deviation
y_range = str(((np.amax(y_array))-(np.amin(y_array)))) #range 
y_list_length = len(y_list)
y_mean = str((sum(y_list))/y_list_length) #mean
y_list_sorted = sorted(y_list)
if y_list_length % 2 == 0: 
    y_median_lower = y_list_sorted[int((y_list_length/2)-1)]
    y_median_higher = y_list_sorted[int((y_list_length/2))]
    y_median = str(((y_median_lower)+(y_median_higher))*0.5)
else:
    y_median = str(y_list_sorted[y_list_length//2]) #median
y_mode = str(mode(y_array)) #mode

if show_extra_details in ('n','N'):
    pass
else:
    print("""
##################################################
""")
    print(x_name + " data: " + str(x_list))
    print(x_name + " standard deviation: " + x_std)
    print(x_name + " range: " + x_range)
    print(x_name + " mean: " + x_mean)
    print(x_name + " median: " + x_median)
    print(x_name + " mode: " + x_mode)
    print('')
    print(y_name + " data: " + str(y_list))
    print(y_name + " standard deviation: " + y_std)
    print(y_name + " range: " + y_range)
    print(y_name + " mean: " + y_mean)
    print(y_name + " median: " + y_median)
    print(y_name + " mode: " + y_mode)

#############################################################################################################
#plotting regression line depending on settings.txt

regression_overhang = float(((np.amax(x_array))-(np.amin(x_array)))*(regression_line_extension_multiplier))
step = ((np.amax(x_array))-(np.amin(x_array)))*(1/1000)
t = np.arange((np.amin(x_array))- regression_overhang,(np.amax(x_array))+regression_overhang,step)
                    #defining array 't' which represents all the x values that will have the polynomial function applied to it.
                    #The step correlates the 'resolution' of the regression line. Change 'step' to a constant like 10 to see this in action
if show_regression_line_degree1 in ('n','N'):
    pass
else:
    if dark_mode_true in ('n','N'):
        pass
    else: #this is the default incase n is not pressed
        plt.style.use('dark_background') #change style to dark_background
    b,c = np.polyfit(x_array,y_array,1) #definining the coefficents of the linear polynomial
    b = round(b,3) #round to 3dp
    c = round(c,3)
    func_name = ('y = '+str(b)+"x + "+str(c))
    plt.plot(t, b*(t) + c, label=func_name, color = regression_line_degree1_color, linestyle = regression_line_degree1_style) #plotting this polynomial using the values from t
    plt.legend(loc='best') #location of label

if show_regression_line_degree2 in ('y','Y'):
    if dark_mode_true in ('n','N'):
        pass
    else:
        plt.style.use('dark_background') #change style to dark_background
    a,b,c = np.polyfit(x_array,y_array,2) #definining the coefficents of the quadratic polynomial
    a = round(a,3)
    b = round(b,3) #round to 3dp
    c = round(c,3)
    func_name = ('y = '+str(a)+'x^2 + '+str(b)+"x + "+str(c)) #definining label name
    plt.plot(t, a*(t**2) + b*(t) + c, label=func_name, color = regression_line_degree2_color, linestyle = regression_line_degree2_style) #plotting this polynomial using the values from t
    plt.legend(loc='best') #location of label
else:
    pass #this is not necessary however this explicity shows how if anything but y is input it will default to showing no line of degree 2

#############################################################################################################
#plotting graph

if dark_mode_true in ('n','N'):
    pass
else:
    plt.style.use('dark_background') #change style to dark_background

plt.scatter(x_array,y_array,s=marker_size,marker=marker_style,color=marker_color) #plot a scatter graph of y vs x
plt.title(y_name +" vs " + x_name) #add title
plt.xlabel(x_name) #label x axis
plt.ylabel(y_name) #label y axis
plt.tight_layout()

if force_axes_start_0_true in ('n','N'):
    pass
else:
    plt.ylim(ymin=0) #forces y axis start at 0         ####WILL HIDE NEGATIVE VALUES####
    plt.xlim(xmin=0) #forces x axis start at 0         ####WILL HIDE NEGATIVE VALUES####
    
    
if grid_true in ('y','Y'):
    plt.grid(axis='both') #add grid to both axes
    
plt.show() #show the plot
