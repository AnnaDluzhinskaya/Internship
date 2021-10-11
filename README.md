Created by: Anna Dluzhinskaya

# Tasks for internship
## 1) Python script for first task (task.py):

### Level_1:
    Implement function - process_data()

    Algorithm: 

    1) Find all *.csv files, and merge them
    2) From name of file, i get @user_id and put this data in output.cvs file
    3) After using @user_id i create names of *.png files
    3) Find path for existing images and put this data in output.cvs file
        - if image does not exist, then instead of image_path, i put "-"

### Level_2:
    Upgrate Level_1

    1)Create web service
    2)GET/date - create and show json file which creates from output.csv
        - implement filtering by is_image_exists = True/False
        - i can not implement filtering by min and max age
    3)POST/data - calls the function process_data()

###Level_3:
    Can not implement, i have never work this docker

## 2) Coding Tasks for Data Engineers

### SQL

#### 1
    
    SELECT id
    FROM users JOIN departments
    on users.id==departments.user_id
    WHERE departments.department_id != 1

####2

    SELECT lastname
    FROM user 
    GROUP By lastname
    HAVING COUNT(lastname) > 1;

####3

    SELECT username, salary FROM user
    JOIN salary
    ON user.id = salary.user_id
    ORDER BY salary.salary DESC
    LIMIT 1 OFFSET 1

###Algorithms and Data Structures
    
    *files in coding_tasks folder*

    1 task: (ex1.py)
    2 task: (ex2.py) - time and space complexity in file (as comments)
    3 task: (ex3.py)

###Linux Shell

    can not do it