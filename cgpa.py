import os

# A class with constructor that calculats the Quality Point
class QualityPoint:
    def __init__(self, course_score, course_unit):
        self.course_score = course_score
        self.course_unit = course_unit

    # Method to calculate the quality point 
    def calculate_qp(self):
        return self.course_unit * self.course_score

# A Grade class that inherints from quality point class and calculates the grade
class Grade(QualityPoint):
    def __init__(self, course_score, course_unit):
        return QualityPoint.__init__(self, course_score, course_unit)
    
    # Method to calculate the grading
    def grade(self):
        grade_point = 0
        if self.course_score >= 70:
            return grade_point + 5
        elif self.course_score >= 60:
            return grade_point + 4
        elif self.course_score >= 50:
            return grade_point + 3
        elif self.course_score >= 45:
            return grade_point + 2
        else:
            return grade_point + 0

# Return Function to prompt a message to the user and get the response
def prompt(message):
    question = input(message)
    return question
    
# Function to display the table
def board_display(student_course, student_score, student_unit, student_grade):
    print("""
        Course                          Score                   Unit                            Grade
        ----------------------------------------------------------------------------------------------
    """)
    for n in range(len(student_course)):
        print(f"""
        {student_course[n]}                             {student_score[n]}                        {student_unit[n]}                             {student_grade[n]}
        """)
    

# Return Function to calculate the cumulative grade point avarage
def calc_cgpa(total_quantity_point, total_unit):
    return sum(total_quantity_point) / sum(total_unit)

# Main Function 
def main_func():
    course_lst = []
    score_lst = []
    grade_point_lst = []
    unit_lst = []
    quality_point_list = []


    try:
        number_of_course = int(prompt("Enter number of course: "))
    except(ValueError):
        print("Value Error, Should be a number not word")
        main_func()

    for n in range(number_of_course): 
        try:
            insert_course = prompt("Enter Course Code: ");course_lst.append(insert_course)
            insert_score = int(prompt("Enter Score: "));score_lst.append(insert_score)
            insert_unit = int(prompt("Enter Unit: "));unit_lst.append(insert_unit)
            grade_point = Grade(insert_score, insert_unit);insert_point = grade_point.grade();grade_point_lst.append(insert_point)
        except:
            print("Wrong input")
            os.system("cls")
            main_func()

        qp = QualityPoint(insert_point, insert_unit);insert_qp = qp.calculate_qp();quality_point_list.append(insert_qp)
        os.system("cls")
        
    cgpa = calc_cgpa(quality_point_list, unit_lst)
    board_display(course_lst, score_lst, unit_lst, grade_point_lst)
    print(f"YOUR CGPA IS: {cgpa}")

if __name__ =="__main__":
    main_func()

        




     
