"""System Module"""
import sys

class student():
    def __init__(self,name, gpa, credit):
        self.name = name
        self.gpa = gpa
        self.credit = credit

def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        school = sys.stdin.readline().rstrip()
        cases2 = int(sys.stdin.readline().rstrip())
        students:list[student] = []
        for _ in range(cases2):
            gpa = 0
            grade_point = 0
            credit_hours = 0
            line = sys.stdin.readline().rstrip()
            name, grades = line.split(":")
            grade_list = grades.split(",")
            for grades in grade_list:
                grade,credit = grades[0], grades[1]
                if grade == "A":
                    grade_point += 4*int(credit)
                elif grade == "B":
                    grade_point += 3*int(credit)
                elif grade == "C":
                    grade_point += 2*int(credit)
                elif grade == "D":
                    grade_point += int(credit)

                credit_hours += int(credit)
            gpa = grade_point/credit_hours
            students.append(student(name,gpa,credit_hours))
        top_gpa = 0
        top_students:list[student] = []
        for children in students:
            if children.gpa > top_gpa:
                top_gpa = children.gpa
        for children in students:
            if children.gpa == top_gpa:
                top_students.append(children)
        if len(top_students) == 1:
            print(f"{school} = {top_students[0].name}")
        else:
            best_credits = 0
            for child in top_students:
                if child.credit > best_credits:
                    best_credits = child.credit
            for child in top_students:
                if child.credit == best_credits:
                    print(f"{school} = {child.name}")

main()