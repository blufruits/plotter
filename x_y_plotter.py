import csv #importing module allowing me to manipulate csv files easier
import matplotlib.pyplot as plt #from the matplotlib library import the pyplot module, refer to this as 'plt'

#############################################################################################################

def firstquestion(): #function that asks user what to do
    
    answer = input("Do you want to input another x/y pair? (Y/N) ")
    
    if answer in ('Y'): #finding answer
        x = input("Input x ") #input x
        y = input ("Input y ") #input y
        file = open('data.csv','a') #locate data.csv
        writer = csv.writer(file) #parse data.csv
        writer.writerow([x,y]) #add a row for the data the user just input
        file.close()
        return True
        
    elif answer in ('N'): #finding answer
        return False
                
    else:
        print("Please enter a valid answer")
        return True

repeat = True #defining repeat
while repeat == True:
    repeat = firstquestion() #repeat is defined as what is returned from the function

#############################################################################################################

file = open('data.csv','r') #referencing the csv file
reader = csv.reader(file) #parsing the csv file. There is no need for the csv file to be sorted hence I do not bother to do this

x_list = [] #defining empty x list
y_list = [] #defining empty y list

for row in reader:  #iterates through each row
    x_list.append(float(row[0])) #adding the first piece of data to the x list (distance)
    y_list.append(float(row[1])) #adding the second piece of data to the y list (pay)

file.close()

#############################################################################################################

plt.style.use('dark_background') #change style to dark_background
plt.scatter(x_list,y_list,color='r') #plot a scatter graph of y vs x
plt.title('y vs x') #add title
plt.xlabel('x') #label x axis
plt.ylabel('y') #label y axis
plt.tight_layout()
plt.show() #show the plot



 
    

    

