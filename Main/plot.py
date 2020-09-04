#############################################################################################################
#import
import time #only used for the .sleep method
import csv #importing module allowing me to manipulate csv files easier

import matplotlib.pyplot as plt #from the matplotlib library import the pyplot module, refer to this as 'plt'
import numpy as np #numpy is used for the handling of arrays

#############################################################################################################
#importing setttings from settings.txt and setting variables to these settings for later use

f = open('settings.txt','r') #opening the settings file
lines = f.readlines() #defining lines to be a list of all lines. these can be indexed 

x_name = str((lines[17].split())[2]) #defining x_name to be the 3rd word on the 18th line. python counts from 0
y_name = str((lines[18].split())[2]) #defining y_name to be the 3rd word on the 19th line. 
grid_true = str((lines[19].split())[2]) #and so on.....
force_axes_start_0_true = str((lines[20].split())[2])
dark_mode_true = str((lines[21].split())[2])
marker_size = float((lines[22].split())[2])
marker_color = str((lines[23].split())[2])
marker_style = str((lines[24].split())[2])
regression_line_color = str((lines[25].split())[2])
regression_line_style = str((lines[26].split())[2])

#############################################################################################################
#initial inputs

def firstquestion(): #function that asks user what to do
    
    answer = input("Do you want to input another " + x_name + "/" + y_name + " pair? (Y/N): ")
    
    if answer in ('Y',''): #finding answer
        x = input("Input " + x_name + ": ") #input x
        y = input ("Input " + y_name + ": ") #input y
        file = open('data.csv','a') #locate data.csv
        writer = csv.writer(file) #parse data.csv
        writer.writerow([x,y]) #add a row for the data the user just input
        file.close()
        return True #does not break loop
        
    elif answer in ('N'): #finding answer
        return False #loop is broken
                
    else:
        print("Please enter a valid answer")
        return True #user is prompted to answer a valid answer. loop not broken

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
#plotting regression line (works but not elegant - improvements in progress)

def secondquestion():
    reg_answer = input("Do you want to add a regression line (Up to ^2)? (Y/N): ")

    if reg_answer in ('Y'):
        return False, True
        
    elif reg_answer in ('N'):
        return False, False
                
    else:
        print("Please enter a valid answer")
        return True, False

x_array = np.array(x_list) #converting lists to numpy arrays. this is so I can use the numpy methods
y_array = np.array(y_list)

repeat2 = True
regress = False #boolean data type notes if the user wants a regression line or not.
while repeat2 == True:
    repeat2, regress = secondquestion() #returns two variables. 'reg' refers to if the user wants to plot a regression line or not

if regress == True:
    step = ((np.amax(x_array))-(np.amin(x_array)))*(1/1000)
    t = np.arange((np.amin(x_array)),(np.amax(x_array)),step) #defining array 't' which represents all the x values that will have the polynomial function applied to it.
                                                              #The step correlates the 'resolution' of the regression line. Change 'step' to a constant like 10 to see this in action
    degree = int(input("Input the degree of the regression line: "))
    if degree in (1,'1'):
        if dark_mode_true in ('n','N'):
            pass
        else:
            plt.style.use('dark_background') #change style to dark_background
        b,c = np.polyfit(x_array,y_array,1) #definining the coefficents of the linear polynomial
        b = round(b,2)
        c = round(c,2)
        func_name = ('y = '+str(b)+"x + "+str(c))
        plt.plot(t, b*(t) + c, label=func_name, color = regression_line_color, linestyle = regression_line_style) #plotting this polynomial using the values from t
        plt.legend(loc='best') #location of label

    elif degree in (2,'2'):
        if dark_mode_true in ('n','N'):
            pass
        else:
            plt.style.use('dark_background') #change style to dark_background
        a,b,c = np.polyfit(x_array,y_array,2) #definining the coefficents of the quadratic polynomial
        a = round(a,2)
        b = round(b,2) #round to 2dp
        c = round(c,2)
        func_name = ('y = '+str(a)+'x^2 + '+str(b)+"x + "+str(c)) #definining label name
        plt.plot(t, a*(t**2) + b*(t) + c, label=func_name, color = regression_line_color, linestyle = regression_line_style) #plotting this polynomial using the values from t
        plt.legend(loc='best') #location of label

    else:
        print("""
Not valid. No regression line will be displayed.""")
        time.sleep(1) #wait 1 second for the user to read

#############################################################################################################
#plotting graph

if dark_mode_true in ('n','N'):
    pass
else:
    plt.style.use('dark_background') #change style to dark_background

plt.scatter(x_list,y_list,s=marker_size,marker=marker_style,color=marker_color) #plot a scatter graph of y vs x
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
