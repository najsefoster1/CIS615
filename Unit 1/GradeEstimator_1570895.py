#Following Unit 7 direction A by importing pandas as pd
import pandas as pd
import json
#Following Unit 5 direction A by importing requests
import requests
from datetime import datetime

#Requesting last name in the variable lastname
#Saying Hello and printing the last name that was given in line 4 & first name that was given in line 2 and added a space.
#User Input 
firstname = input("What is your first name? ").strip().lower().capitalize()
lastname = input("What is your last name? ").strip().lower().capitalize()
print("Hello " + lastname + " " + firstname)

#Function to read grades from CSV file
def read_grades(file_path):
    try:
        file_choice = input("Enter '0' to use grades_0.csv or '50' to use grades_50.csv: ").strip()
        file_path = f'/Users/Mine/Desktop/CIS615/Unit 8/grades_{file_choice}.csv'
        grades_df = pd.read_csv('/Users/Mine/Desktop/CIS615/Unit 8/grades_0.csv')
        return grades_df
    except FileNotFoundError:
        print(f"Error: File 'grades_0.csv' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None

def clean_grades(grades_df, max_grade):
    try:
        #Iterate over each week column and clean the grades
        for week in range(1, 9):
            week_col = f'week{week}'
            grades_df[week_col] = grades_df[week_col].apply(lambda x: max(0, min(x, max_grade)))
        return grades_df
    except Exception as e:
        print(f"Error while cleaning grades: {e}")
        return None

#Main function
def main():
    # Read grades from CSV file
    grades_df = read_grades('grades_0.csv')
    if grades_df is None:
        return

    #Read data from JSON file to get maximum grade
    with open('tasks.json') as f:
        max_grade_json = json.load(f)
        max_grade = max_grade_json["max_grade"]

    #Clean data
    cleaned_grades_df = clean_grades(grades_df, max_grade)
    if cleaned_grades_df is None:
        return
    
    #Manually enter the last two grades for Unit 8
    for i in range(2):
        grade = float(input(f"Enter grade {i+1} for Unit 8: "))
        cleaned_grades_df.at[cleaned_grades_df.index[-1-i], 'week8'] = grade
    
    #Display to the user the grade the student has and the maximum grade direction from Unit 8 B
    actual_grade = cleaned_grades_df[['week1', 'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8']].sum().sum()
    print(f"You have {actual_grade} out of {max_grade}")

    #Calculate percentage current grade in comparison to maximum grade Unit 8 direction C
    percentage = (actual_grade / max_grade) * 100
    print(f"Your percentage is {percentage:.2f}%")


    #Calculate letter grade Unit 8 direction D
    if percentage > 90:
        letter_grade = 'A'
    elif percentage > 80:
        letter_grade = 'B'
    elif percentage > 70:
        letter_grade = 'C'
    elif percentage > 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    #Output the letter grade to the user from direction E unit 8. 
    print(f"Your letter grade is: {letter_grade}")


if __name__ == "__main__":
    main()
    
    ##Removed unnecessary content and moved user input up. Direction from Unit 8 A.   
    #Display contents of grades.csv for Unit 7 direction C
    #print("Contents of grades.csv:")
    #print(grades_df)

    #Display all grades just for discussions for Unit 7 direction D
    #discussion_grades = grades_df[grades_df['type'] == 'Discussion']
    #print("\nDiscussion Grades:")
    #print(discussion_grades)
     
    #Read data from JSON file to get maximum grade
    #with open('/Users/Mine/Desktop/CIS615/Unit 5/tasks.json') as f:  #Update path to your JSON file
        #max_grade_json = json.load(f)
        #max_grade = max_grade_json["max_grade"]

    
    #Display cleaned data for Unit 7 direction G
    #print("\nCleaned Data:")
    #print(cleaned_grades_df)

#if __name__ == "__main__":
    #main()
#Make a web request to the World Time API
#Following Unit 5 direction A imported requests to make a web request to the World Time API but had to update Python to allow for requests to be made
#response = requests.get("http://worldtimeapi.org/api/timezone/America/Chicago")
#data = response.json()

#Get client_ip, day_of_year, and utc_datetime from the response
#client_ip = data['client_ip']
#day_of_year = data['day_of_year']
#utc_datetime = data['utc_datetime']

# Display the information obtained
#print("Client IP:", client_ip)
#print("Day of the year:", day_of_year)
#print("UTC Datetime:", utc_datetime)

#Create a variable for the date when the course began
#Unit 6 direction D to update the date to the date the course began so it has a starting point to do calculations from
#begin_course_day = datetime(2024, 1, 8).timetuple().tm_yday

#Create a variable for the current date/time using the unixtime field from the JSON response from Unit 6 direction E 
#now_date = datetime.utcfromtimestamp(data['unixtime']) did not work due to having a macbook and it stated it would be removed in a future python update
#now_date = datetime.fromtimestamp(data['unixtime'])

#Convert now_date to have only date (without time)
#Direction Unit 6 letter G
#now_day = now_date.timetuple().tm_yday

#Calculate the difference in days between begin_course_day and now_day
#difference_days = now_day - begin_course_day

#Convert days to Units (1 Unit = 7 days)
#Direction Unit 6 letter H
#units_completed = difference_days // 7

#Read data from tasks.json file
#with open('/Users/Mine/Desktop/CIS615/Unit 5/tasks.json') as f:
    #json_data = json.load(f)



#Create Task_type class for Unit 5 direction A with displayname, taskspersemester, and maximumpointspertask
#class Task_type:
    #def __init__(self, name, display_name, tasks_per_semester, maximum_points_per_task):
        #self.name = name
        #self.display_name = display_name
        #self.tasks_per_semester = tasks_per_semester
        #self.maximum_points_per_task = maximum_points_per_task

#Read data from tasks.json file Unit 5 direction B
#Create an empty list for storing task types Unit 5 direction C
#task_types_list = []

#Create classes for each task type and add them to the list Unit 5 direction D
#Loop through for each assignment in the JSON data
#for assignment in json_data["assignments"]:
    #Take information from JSON for each assignment 
    #name = assignment["name"]
    #display_name = assignment["display_name"]
    #tasks_per_semester = assignment["tasks_per_semester"]
    #maximum_points_per_task = assignment["max_points_per_submission"]
    #Create a Task_type object and append it to the list
    #task_type = Task_type(name, display_name, tasks_per_semester, maximum_points_per_task)
    #task_types_list.append(task_type)

#Calculate total maximum points
#total_maximum_points = sum(task.maximum_points_per_task * task.tasks_per_semester for task in task_types_list)

#Requesting first name in the variable firstname
#Requesting last name in the variable lastname
#Saying Hello and printing the last name that was given in line 4 & first name that was given in line 2 and added a space.
#User Input 
#firstname = input("What is your first name? ").strip().lower().capitalize()
#lastname = input("What is your last name? ").strip().lower().capitalize()
#print("Hello " + lastname + " " + firstname)

#Create 3 classes to store information about assignment types named (Discussions, Course_projects, Core_assessments). Unit 4 direction C. 
#Added maximum_points_per_task, tasks_per_semester, display_name with appropriate values/Unit 4 direction D.
#class Discussions:
    #def __init__(self, unit, points):
        #self.unit = unit
        #self.points = points
        #self.maximum_points_per_task= 50
        #self.tasks_per_semester= 8
        #self.display_name= "Discussions"

#class CourseProjects:
    #def __init__(self, unit, points):
        #self.unit = unit
        #self.points = points
        #self.maximum_points_per_task = 50
        #tasks_per_semester = 8
        #display_name = "Course Projects"

#class CoreAssessments:
    #def __init__(self, unit, points):
        #self.unit = unit
        #self.points = points
        #self.maximum_points_per_task = 50
        #self.tasks_per_semester = 4
        #self.display_name = "Core Assessments"


#def display_result(total_points, max_points, display_name):
    #result = f"Currently you have {sum(total_points)} points for {display_name} out of {max_points}"
    #print(result)


#Display the current Unit of the class
#Following Unit 6 direction I 
#print("You have completed", units_completed, "Units of 8.")

#Calculates the total maximum points a student can get for the class using the task types from the JSON file Unit 5 direction E and F
#print("Maximum grade you can get for this class is:", total_maximum_points)

#Assigning points for the homeworks for unit 1 of what I received.
#Unit1_discussion_points= 50
#Unit1_course_project_points= 50
#Unit1_core_assessment_points= 45


#This is the maximum amount of points for each task to help determine 
#discussion_task_maximum_points= 250
#course_project_max_points= 250
#core_assessment_max_points= 150

#This is to calculate the total points for the unit by adding the units that have been completed Unit 4 direction A request for this to be updated with Unit 3 grades.
#Raw numbers were input due to variables weren't requested to be made.
#total_discussion_points= [Unit1_discussion_points, 50, 50, 50, 50]
#total_course_project_points= [Unit1_course_project_points, 50, 50, 50, 45]
#total_core_assessment_points= [Unit1_core_assessment_points, 50, 50]

# Displaying the information from the classes
#This is uesd to display the total points for each of the different areas that decide the grade for the overall class while using a string as requested from Unit 3 direction C. 
#disresult = "Currently you have " + str(sum(total_discussion_points)) + " points for discussions out of "+ str(discussion_task_maximum_points) 
#print(disresult)

#couresult= "Currently you have " + str(sum(total_course_project_points)) + " points for the Course Project out of " + str(course_project_max_points)
#print(couresult)

#corresult= "Currently you have " + str(sum(total_core_assessment_points))+ " points for the Core Assessment out of "+ str(core_assessment_max_points)
#print(corresult)

# Check if maximum points were received for each of the tasks Unit 4 direction B
#discussion_max_points= (sum(total_discussion_points) == discussion_task_maximum_points)
#course_project_max_points= (sum(total_course_project_points) == course_project_max_points)
#core_assessment_max_points= (sum(total_core_assessment_points) == core_assessment_max_points)

# Display the results for whether or not max points were received for each area of study using the class information
#if discussion_max_points:
    #print("Congrats! You got maximum points for ALL discussion homeworks so far!")
#else:
    #print("Unfortunately you did not get maximum points for ALL discussion homeworks.")

#if course_project_max_points:
    #print("Congrats! You got maximum points for ALL course project homeworks so far!")
#else:
    #print("Unfortunately you did not get maximum points for ALL course project homeworks.")

#if core_assessment_max_points:
    #print("Congrats! You got maximum points for ALL core assessment homeworks so far!")
#else:
    #print("Unfortunately you did not get maximum points for ALL core assessment homeworks.")
