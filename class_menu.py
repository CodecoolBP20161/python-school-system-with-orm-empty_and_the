from model_interview import *
from model_answer import *
from model_mentor import *
from model_interview_slot import *
from class_table import *


class Menu:

    @classmethod
    def administrator_submenu(cls):
        print("\nAdministrator submenu\n--------------------------\n1. Handle new applications\nX. Exit to Main menu\n")
        g = input("Choose an option: ")
        if g == "1":
            Applicant.get_closest_school()
            print("System message: Closest school connected to the applicants.")
            Applicant.application_code_generator()
            print("System message: Application code generated for the applicants.")
            print("System message: E-mails about application details have been sent to the applicants.")
            InterviewSlot.get_interview_for_applicants()
            print("System message: Interview time generated for the applicants.")
            print("System message: E-mails about interview details have been sent to the applicants.")
            print("System message: E-mails about interview details have been sent to the mentors.")
            cls.administrator_submenu()
        elif g == "X" or g == "x":
            cls.main_menu()
        else:
            print("Not a valid option!")
            cls.administrator_submenu()

    @classmethod
    def applicant_submenu(cls, applicant):
        print("\nApplicant submenu\n----------------------")
        print("\n1. Application details\n2. Interview details\n3. Questions\nX. Exit to Main menu\n")
        g = input("Choose an option: ")
        if g == "1":
            print("\nApplication code: {0}\nStatus: {1}\nSchool: {2}"
                  .format(applicant.application_code, applicant.status, applicant.school.name))
            cls.applicant_submenu(applicant)
        elif g == "2":
            try:
                details_list = list(Interview.get_interview_details_by_application_code(applicant.application_code))
                print("\nInterview date and time: {0}\nSchool: {1}\nMentors: {2} {3} and {4} {5}"
                      .format(*details_list))
            except Interview.DoesNotExist:
                print("\nNo interview registered for application code: {} in the database."
                      .format(applicant.application_code))
            cls.applicant_submenu(applicant)
        elif g == "3":
            print("\nApplication code: {0}".format(applicant.application_code))
            if not list(Answer.get_answers_by_application_code(applicant.application_code)):
                print("\nNo questions registered for application code: {} in the database."
                      .format(applicant.application_code))
            else:
                table = Table(list(Answer.get_answers_by_application_code(applicant.application_code)),
                              ["Question", "Question status", "Answer"])
                print(table)
            cls.applicant_submenu(applicant)
        elif g == "X" or g == "x":
            cls.main_menu()
        else:
            print("Not a valid option!")
            cls.applicant_submenu(applicant)

    @classmethod
    def mentor_submenu(cls, mentor):
        print("\nMentor submenu\n--------------------------")
        print("\n1. Interviews\n2. Questions\n3. Answer question\nX. Exit to Main menu\n")
        g = input("Choose an option: ")
        if g == "1":
            if not list(mentor.get_interviews_by_mentor_object()):
                print("\nNo interviews registered for this mentor in the database.")
            else:
                table = Table(list(mentor.get_interviews_by_mentor_object()),
                              ["Date and time", "Application code", "First name", "Last name"])
                print(table)
<<<<<<< HEAD
=======
            cls.mentor_submenu(mentor)
        if g == "2":
            if not list(mentor.get_question_data_for_mentor()):
                print("\nNo questions registered for this mentor in the database.")
            else:
                table = Table(list(mentor.get_question_data_for_mentor()),
                              ["Question ID", "Date and time", "Application code", "Question"])
                print(table)
            cls.mentor_submenu(mentor)
        if g == "3":
            question = input("\nWhich question do you want to answer? ")
            answer = input("\nWhat is your answer? ")
            try:
                Answer.answer_question(question, answer, mentor.id)
            except:
                print("Wrong question number!")
>>>>>>> user_story_10
            cls.mentor_submenu(mentor)
        elif g == "X" or g == "x":
            cls.main_menu()
        else:
            print("Not a valid option!")
            cls.mentor_submenu(mentor)

    @classmethod
    def get_applicant_object(cls):
        try:
            user_input = int(input("Please, enter an Application code: "))
            if user_input > 99999 or user_input < 10000:
                raise ValueError
            applicant = Applicant.get_applicant_object_by_application_code(user_input)
            return applicant
        except ValueError:
            print("This is not a valid Application code, try again!")
            cls.main_menu()
        except Applicant.DoesNotExist:
            print("This Application code is not in the database!")
            cls.main_menu()

    @classmethod
    def get_mentor_object(cls):
        try:
            user_input = int(input("Please enter your password: "))
            if user_input > 999999 or user_input < 100000:
                raise ValueError
            mentor = Mentor.get_mentor_object_by_password(user_input)
            return mentor
        except ValueError:
            print("This is not a valid password, try again!")
            cls.main_menu()
        except Mentor.DoesNotExist:
            print("This Mentor is not in the database!")
            cls.main_menu()

    @classmethod
    def main_menu(cls):
        print("\nMain Menu\n----------------\n1. Administrator\n2. Applicant\n3. Mentor\nX. Exit")
        g = input("Choose a user: ")
        if g == "1":
            cls.administrator_submenu()
        elif g == "2":
            applicant = cls.get_applicant_object()
            cls.applicant_submenu(applicant)
        elif g == "3":
            mentor = cls.get_mentor_object()
            cls.mentor_submenu(mentor)
        elif g == "X" or g == "x":
            exit()
        else:
            print("Not a valid option!")
            cls.main_menu()
