# Django Assignment - 4

Marks : 80
(80 + 10 + 10) 100 Marks Deadline : 9 Dec 2023 ; 11:59 pm
(72 + 9 + 9) 90 Marks Deadline : 10 Dec 2023 ; 11:59 pm
(64 + 8 + 8) 80 Marks Deadline : Any time after that

What You Need to Submit : 
     Sample : 
1. Practice 14.5 : github link
2. Practice 15.5 : github link
3. Doc File : doc file link
4. Assignment 4 : github link

Instructions: Watch the video sincerely

Task Management System

You are asked to implement a Django ‘Task Management System’ project where anyone can add a task under different categories, edit the tasks, and delete the tasks. You need to create a model i.e 

## ‘TaskModel’ having fields 
- taskTitle 
- taskDescription 
- is_completed by default False
- Task Assign Date
N.B : Here ‘is_completed’ field should be of type models.BooleanField and default values for this field should be ‘False’                                                             ( Marks - 10 )

## TaskCategory Model will have
- Category Name
- Many-to-Many Relationships with task model                              ( Marks - 10 )

## Main Requirements

1. In this project, users should be able to: Add a navigation bar where user will see Add Task,Add Category, Show Tasks menu (Marks - 5)
2. In the Show Tasks Page users can see all the tasks in bootstrap card style for every task there will be two buttons Edit Delete  . For completed tasks the user won’t see the edit and delete button rather see Completed. (Marks - 15)
3. An User can edit the task, delete the task, complete the task. When a task is completed then the is_completed will be True.                               (Marks - 10)
4. In the Add Task Page, users can see a form based on the task model form, can provide title, description, can select multiple categories, Is Completed and then submit the form and the data must be added to the database and then redirect the user to the Show Tasks page. You must use the model form here.  (Marks - 10)
5. In the Add Category page, users can add a category by its name. Use model form here (Marks - 10 ) 
6. Following requirements must be filled : ( Marks - 10 )
There must be two apps named task and category
Global templates for base.html and and app templates for showing forms in both apps
