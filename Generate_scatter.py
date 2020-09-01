import csv #importing module allowing me to manipulate csv files easier
import matplotlib.pyplot as plt #from the matplotlib library import the pyplot module, refer to this as 'plt'

#############################################################################################################

def firstquestion(): #function that asks user what to do
    
    answer = input("Do you want to input another distance/pay pair? (Y/N) ")
    
    if answer in ('Y'): #finding answer
        distance = input("Distance travelled ? (miles) ") #input the distance
        pay = input ("Courier pay for that distance? (£) ") #input the pay corresponding to this distance
        file = open('data.csv','a') #locate data.csv
        writer = csv.writer(file) #parse data.csv
        writer.writerow([distance,pay]) #add a row for the data the user just input
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
reader = csv.reader(file) #parsing the csv file. There is no need for the csv file to be in ascending order hence I do not bother

x = [] #defining empty x list
y = [] #defining empty y list

for row in reader:  #iterates through each row
    x.append(float(row[0])) #adding the first piece of data to the x list (distance)
    y.append(float(row[1])) #adding the second piece of data to the y list (pay)

file.close()

#############################################################################################################

plt.style.use('dark_background') #change style to dark_background
plt.scatter(x,y,color='r') #plot a scatter graph of y vs x
plt.xlim(0,6) #axis range
plt.ylim(0,13) #axis range
plt.title('Pay vs Distance travelled') #add title
plt.xlabel('Distance travelled (miles)') #label x axis
plt.ylabel('Pay (£)') #label y axis
plt.tight_layout()
plt.show() #show the plot



 
    

    

