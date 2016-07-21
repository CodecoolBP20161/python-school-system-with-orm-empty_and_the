from model_applicant import *
from model_interview import *
from model_question import *
from model_answer import *


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
                print("\nInterview date and time: {0}\nSchool: {1}\nMentor: {2}"
                      .format(applicant.interview.get().date_time, applicant.school.name,
                              applicant.interview.get().mentor))
            except Interview.DoesNotExist:
                print("\nNo interview registered for application code: {} in the database."
                      .format(applicant.application_code))
            cls.applicant_submenu(applicant)
        elif g == "3":
            print("\nApplication code: {0}".format(applicant.application_code))
            for_boolean = False
            for i in Answer.get_answers_by_application_code(applicant.application_code):
                    for_boolean = True
                    print("\nQuestion: {0}\nQuestion status: {1}\nAnswer: {2}".format(i[0], i[1], i[2]))
            if for_boolean is False:
                print("\nNo questions registered for application code: {} in the database."
                      .format(applicant.application_code))
            cls.applicant_submenu(applicant)
        elif g == "X" or g == "x":
            cls.main_menu()
        else:
            print("Not a valid option!")
            cls.applicant_submenu(applicant)

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
    def main_menu(cls):
        print("\nMain Menu\n----------------\n1. Administrator\n2. Applicant\nX. Exit\n")
        g = input("Choose a user: ")
        if g == "1":
            Menu.administrator_submenu()
        elif g == "2":
            applicant = cls.get_applicant_object()
            Menu.applicant_submenu(applicant)
        elif g == "X" or g == "x":
            exit()
        else:
            print("Not a valid option!")
            cls.main_menu()
