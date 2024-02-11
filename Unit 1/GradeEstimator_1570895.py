
#Add JSON data in a variable 
json_data = {
  "assignments": [
    {
      "name": "Core Assessment",
      "display_name": "Assessment",
      "tasks_per_semester": 4,
      "max_points_per_submission": 50
    },
    {
      "name": "Discussion",
      "display_name": "Group Discussions",
      "tasks_per_semester": 8,
      "max_points_per_submission": 50
    },
    {
      "name": "Course Project",
      "display_name": "Project",
      "tasks_per_semester": 8,
      "max_points_per_submission": 50
    }
  ]
}

#Create Task_type class for Unit 5 direction A with displayname, taskspersemester, and maximumpointspertask
class Task_type:
    def __init__(self, name, display_name, tasks_per_semester, maximum_points_per_task):
        self.name = name
        self.display_name = display_name
        self.tasks_per_semester = tasks_per_semester
        self.maximum_points_per_task = maximum_points_per_task

#Read data from tasks.json file Unit 5 direction B
#Create an empty list for storing task types Unit 5 direction C
task_types_list = []

#Create classes for each task type and add them to the list Unit 5 direction D
#Loop through for each assignment in the JSON data
for assignment in json_data["assignments"]:
    #Take information from JSON for each assignment 
    name = assignment["name"]
    display_name = assignment["display_name"]
    tasks_per_semester = assignment["tasks_per_semester"]
    maximum_points_per_task = assignment["max_points_per_submission"]
    #Create a Task_type object and append it to the list
    task_type = Task_type(name, display_name, tasks_per_semester, maximum_points_per_task)
    task_types_list.append(task_type)

#Calculate total maximum points
total_maximum_points = sum(task.maximum_points_per_task * task.tasks_per_semester for task in task_types_list)

#Requesting first name in the variable firstname
#Requesting last name in the variable lastname
#Saying Hello and printing the last name that was given in line 4 & first name that was given in line 2 and added a space.
#User Input 
firstname = input("What is your first name? ").strip().lower().capitalize()
lastname = input("What is your last name? ").strip().lower().capitalize()
print("Hello " + lastname + " " + firstname)

#Create 3 classes to store information about assignment types named (Discussions, Course_projects, Core_assessments). Unit 4 direction C. 
#Added maximum_points_per_task, tasks_per_semester, display_name with appropriate values/Unit 4 direction D.
class Discussions:
    def __init__(self, unit, points):
        self.unit = unit
        self.points = points
        self.maximum_points_per_task= 50
        self.tasks_per_semester= 8
        self.display_name= "Discussions"

class CourseProjects:
    def __init__(self, unit, points):
        self.unit = unit
        self.points = points
        self.maximum_points_per_task = 50
        tasks_per_semester = 8
        display_name = "Course Projects"

class CoreAssessments:
    def __init__(self, unit, points):
        self.unit = unit
        self.points = points
        self.maximum_points_per_task = 50
        self.tasks_per_semester = 4
        self.display_name = "Core Assessments"


def display_result(total_points, max_points, display_name):
    result = f"Currently you have {sum(total_points)} points for {display_name} out of {max_points}"
    print(result)

#Calculates the total maximum points a student can get for the class using the task types from the JSON file Unit 5 direction E and F
print("Maximum grade you can get for this class is:", total_maximum_points)

#Assigning points for the homeworks for unit 1 of what I received.
Unit1_discussion_points= 50
Unit1_course_project_points= 50
Unit1_core_assessment_points= 45


#This is the maximum amount of points for each task to help determine 
discussion_task_maximum_points= 200
course_project_max_points= 200
core_assessment_max_points= 150

#This is to calculate the total points for the unit by adding the units that have been completed Unit 4 direction A request for this to be updated with Unit 3 grades.
#Raw numbers were input due to variables weren't requested to be made.
total_discussion_points= [Unit1_discussion_points, 50, 50, 50]
total_course_project_points= [Unit1_course_project_points, 50, 50, 50]
total_core_assessment_points= [Unit1_core_assessment_points, 50, 50]

# Displaying the information from the classes
#This is uesd to display the total points for each of the different areas that decide the grade for the overall class while using a string as requested from Unit 3 direction C. 
disresult = "Currently you have " + str(sum(total_discussion_points)) + " points for discussions out of "+ str(discussion_task_maximum_points) 
print(disresult)

couresult= "Currently you have " + str(sum(total_course_project_points)) + " points for the Course Project out of " + str(course_project_max_points)
print(couresult)

corresult= "Currently you have " + str(sum(total_core_assessment_points))+ " points for the Core Assessment out of "+ str(core_assessment_max_points)
print(corresult)

# Check if maximum points were received for each of the tasks Unit 4 direction B
discussion_max_points= (sum(total_discussion_points) == discussion_task_maximum_points)
course_project_max_points= (sum(total_course_project_points) == course_project_max_points)
core_assessment_max_points= (sum(total_core_assessment_points) == core_assessment_max_points)

# Display the results for whether or not max points were received for each area of study using the class information
if discussion_max_points:
    print("Congrats! You got maximum points for ALL discussion homeworks so far!")
else:
    print("Unfortunately you did not get maximum points for ALL discussion homeworks.")

if course_project_max_points:
    print("Congrats! You got maximum points for ALL course project homeworks so far!")
else:
    print("Unfortunately you did not get maximum points for ALL course project homeworks.")

if core_assessment_max_points:
    print("Congrats! You got maximum points for ALL core assessment homeworks so far!")
else:
    print("Unfortunately you did not get maximum points for ALL core assessment homeworks.")
