# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:16:05 2020

@author: Steven Kyle D.C. Villanueva
"""
import random
import csv
import pandas as pd
schedule=[]
choice=0
def clear():
    print ("\n" * 50)

def sched():
    print("\n-------------Employee Task Schedule-------------")
    for i in schedule:
        for j in i:
            print(j,end = "\t")
        print()
    print("-------------------------------------------------")
        
clear()        
print("----------Employee Task Scheduling Program----------")
print("Setting up the table...", end = "")
emp = int(input("Enter the number of employees: "))
mos = int(input("Enter the overall time period: "))

for i in range(emp+1):
    row=[]
    for j in range(mos+1):
        row.append("")
    schedule.append(row)
schedule[0][0] = "Sched"
 
for j in range(mos):
    schedule[0][j+1] = "month"+str(j+1)

nam = int(input("Would you like to name the employees [1-Yes, 0-No]? "))
if nam==1:
    for i in range(emp):
        name = input("Enter "+str(i+1)+"th name: ")          
        schedule[i+1][0] = name
else:
    for i in range(emp):
        schedule[i+1][0] = "emp"+str(i+1)

while choice!=9:
    emp = len(schedule)-1
    mos = len(schedule[0])-1
    clear()
    sched()
    print("Menu:")
    print("[1] Clear all tasks")
    print("[2] Add an employee")
    print("[3] Add a month")
    print("[4] Add a task")
    print("[5] Remove an employee")
    print("[6] Save schedule")
    print("[7] Load schedule")
    print("[9] Exit")
    choice = int(input("Choice: "))
    
    if choice == 1:
        clear()
        print("[1] Clear all tasks")
        print("Clearing all tasks...")
        for i in range(emp):
            for j in range(mos):
                schedule[i+1][j+1]=""
        input("Enter any character to continue... ")  
    
    elif choice == 2:
        clear()
        print("[2] Add an employee")
        nam = int(input("Would you like to name the employees [1-Yes, 0-No]? "))
        if nam==1:
            row=[]
            name = input("Enter name: ")
            row.append(name)
            for j in range(mos):
                row.append("")
            schedule.append(row)
        else:
            print
            row=[]
            name = "emp"+ str(emp+1)
            row.append(name)
            for j in range(mos):
                row.append("")
            schedule.append(row)     
        
    elif choice == 3:
        clear()
        print("[3] Add a month")
        print("Adding a month...")
        schedule[0].append("month"+str(mos+1))
        for i in range(emp):
            schedule[i+1].append("")
        sched()
        input("Enter any character to continue... ")
        
    elif choice == 4:
        clear()
        assigned=0
        print("[4] Add a task")
        for i in range(emp):                #check if there are any available employees                    
                if schedule[i+1][1] != "":
                    assigned=assigned+1
        if assigned==emp:
            print("There are no more available employees for assignment.")
            input("Enter any character to continue... ")
            continue
            
        task = input("Enter task name: ")
        team = int(input("How many employees should work on this task monthly? "))
        
        if assigned+team>emp:              #check if task can still be handled by remaining emp
            print("\nThe remaining employees are less than the task's requirement.")
            input("Enter any character to continue... ")
            continue
        
        q = int(input("Can an employee be assigned to the same task [1-Yes, 0-No]? "))
        if  q == 1:
            rep = int(input("How long (in mos) can an employee rest before doing the same task? "))
            assigned=0                         #task assignment on the first month
            while assigned!=team:
                assign = random.randint(1,emp)
                if schedule[assign][1] == "":
                    schedule[assign][1] = task
                    assigned=assigned+1
            vacant=emp-assigned
            
            while vacant>0:
                for j in range(2,mos+1):
                    assigned=0
                    for i in range(2,emp):     #limit assigned emp per month 
                        if schedule[i][j] == task:
                            assigned=assigned+1
                    curteam=assigned
                    
                    fail=0
                    while curteam<team and fail<emp*10:
                        assign = random.randint(1,emp)
                        start = j-rep
                        if start < 1:
                             start = 1
                        stop = j
                        checker = schedule[assign][start:stop]
                        if schedule[assign][j] == "" and task not in checker:
                            schedule[assign][j] = task
                            vacant=vacant-1
                            curteam=curteam+1
                        else:
                            fail=fail+1
                            continue
            
        else:     
            assigned=0                         #task assignment on the first month
            while assigned!=team:
                assign = random.randint(1,emp)
                if schedule[assign][1] == "":
                    schedule[assign][1] = task
                    assigned=assigned+1
            vacant=emp-assigned
            
            while vacant>0:
                for j in range(2,mos+1):
                    assigned=0
                    for i in range(2,emp):     #limit assigned emp per month 
                        if schedule[i][j] == task:
                            assigned=assigned+1
                    curteam=assigned
                    
                    fail=0
                    while curteam<team and fail<emp*10:
                        assign = random.randint(1,emp)
                        if schedule[assign][j] == "" and task not in schedule[assign]:
                            schedule[assign][j] = task
                            vacant=vacant-1
                            curteam=curteam+1
                        else:
                            fail=fail+1
                            continue
                        
    elif choice == 5:
        clear()
        print("[5] Remove an employee")
        d = input("Who is the employee you want to remove? ")
        
        for i in range(emp+1):
            if schedule[i][0] == d:
                schedule.pop(i)
                print("Employee removed...")
        input("Enter any character to continue... ")  
            
    elif choice == 6:
        clear()
        print("[6] Save schedule")
        print("Saving the schedule...")
        with open('schedule.csv','w',newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONE)
            writer.writerows(schedule)
        input("Enter any character to continue... ")
        
    elif choice == 7:
        clear()
        print("[7] Load schedule")
        print("Loading the schedule...")
        with open('schedule.csv',newline="") as f:
            reader = csv.reader(f)
            schedule = list(reader)
            sched()
        input("Enter any character to continue... ")
    
    elif choice == 9:
        print("The program will now close...")
        
    
    
    

    