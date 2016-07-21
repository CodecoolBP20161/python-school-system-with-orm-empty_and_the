from model_applicant import *


def administrator_submenu():
    print("\nAdministrator submenu\n1. Handle new applications\nX. Exit to Main menu\n")
    g = input("Choose an option: ")
    if g == "1":
        Applicant.closest_school()
        print("System message: Closest school connected to the applicants.")
        Applicant.application_code_generator()
        print("System message: Application code generated for the applicants.")
        administrator_submenu()
    elif g == "X" or g == "x":
        main()
    else:
        print("Wrong number!")
        administrator_submenu()


def applicant_submenu():
    print("\nApplicant submenu\n1. Application details\nX. Exit to Main menu\n")
    g = input("Choose an option: ")
    if g == "1":
        valid_number = Applicant.select(Applicant.application_code).where(Applicant.id == 1).get().application_code
        applicant = Applicant.get_applicant_object_by_application_code(valid_number)
        status, school_name = applicant.get_status_and_school()
        print("\nApplication code: {0}\nStatus: {1}\nSchool: {2}".format(valid_number, status, school_name))
        applicant_submenu()
    elif g == "X" or g == "x":
        main()
    else:
        print("Wrong number!")
        applicant_submenu()


def main():
    print("\nMain Menu\n1. Administrator\n2. Applicant\nX. Exit\n")
    g = input("Choose a user: ")
    if g == "1":
        administrator_submenu()
    elif g == "2":
        applicant_submenu()
    elif g == "X" or "x":
        exit()
    else:
        print("Wrong number!")
        main()

if __name__ == '__main__':
    main()
