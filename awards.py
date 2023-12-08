'''
TASK INFORMATION: 
- Design a program that determines the award a person competing in a triathlon will receive. 
- Your program should read in the times (in minutes) for all three events of a triathlon, namely 
  swimming, cycling, and running, and then calculate and display the total time taken to complete the triathlon.
- The award a participant receives is based on the total time taken to complete the triathlon. 
  The qualifying time for awards is 100 minutes. Display the award that the participant will receive based on the following criteria:


Qualifying Criteria:                                    Time Range:          Award:
Within the qualifying time                              0 - 100 minutes      Provincial Colours
Within 5 minutes of the qualifying time                 101 - 105 minutes    Provincial Half Colours
Within 10 minutes of the qualifying time                106 - 110 minutes    Provincial Scroll 
More than 10 minutes off from the qualifying time       111+ minutes         No award 
'''

'''

Start
1. have user input minutes for the following variables (and turn into integers): swimming_minutes, cycling_minutes, and running_minutes
2. create variable called triathlon_minutes with value being sum of all events
3. "if" statement for <100 print "Provincial Colours"
4. elif statement for >= 101 and <= 105 print "Provincial Half Colours"
5. elif statement for >= 106 and <= 110 print "Provincial Scroll"
6. else statement print "No award"
End
'''

swimming_minutes = int(input("Enter time taken to complete the swimming event in minutes: "))
cycling_minutes = int(input("Enter time taken to complete the cycling event in minutes: "))
running_minutes = int(input("Enter time taken to complete the running event in minutes: "))

triathlon_minutes = swimming_minutes + cycling_minutes + running_minutes

if triathlon_minutes <= 100:
    print("Provincial Colours")

elif triathlon_minutes >= 101 and triathlon_minutes <= 105:
    print("Provincial Half Colours")

elif triathlon_minutes >= 106 and triathlon_minutes <= 110:
    print("Provincial Scroll")

else:
    print("No award")
