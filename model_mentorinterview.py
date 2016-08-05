from model_base import *
from model_mentor import *
from model_interview import *


class MentorInterview(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name="mentorinterview")
    interview = ForeignKeyField(Interview, related_name="interviews")

    def return_neccessary_data(self):
        return (self.mentor.first_name + ' ' + self.mentor.last_name, self.interview.date_time,
                self.interview.applicant.first_name + ' ' + self.interview.applicant.last_name,
                self.interview.applicant.school.name)

    @classmethod
    def get_interview_by_filter(cls, filter_number):
        if filter_number == "1":
            filter_string = input("Mentor name:")
            for element in cls.select().join(Mentor).where(Mentor.first_name.concat(" ").concat(Mentor.last_name) ==
                                                           filter_string):
                yield element.return_neccessary_data()
        elif filter_number == "2":
            filter_string = input("Date:")
            for element in cls.select().join(Interview).where(Interview.date_time == filter_string):
                yield element.return_neccessary_data()
        elif filter_number == "3":
            filter_string = input("Applicant name:")
            for element in cls.select().join(Interview).join(Applicant).where(
                    Applicant.first_name.concat(" ").concat(Applicant.last_name) == filter_string):
                yield element.return_neccessary_data()
        elif filter_number == "4":
            filter_string = input("School name:")
            for element in cls.select().join(Mentor).join(School).where(School.name == filter_string):
                yield element.return_neccessary_data()
        elif filter_number == "5":
            for element in cls.select():
                yield element.return_neccessary_data()
        else:
            print("Not a valid option!")
