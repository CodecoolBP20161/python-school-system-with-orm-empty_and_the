# Interview_slot table contains the mentor's free time for the interviews
from model_mentor import *
from model_applicant import *
from model_interview import *
from model_mentorinterview import *


class InterviewSlot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name="mentor")

    # Get interview slot and save it for the new applicant and sends email(from webpage registration)
    @classmethod
    def get_interview_for_applicant(cls, applicant):
        break_boolean = False
        interview_slot_object_list = cls.get_mentor_object_list_not_reserved()
        for j in interview_slot_object_list:
            if break_boolean:
                break
            elif j.mentor.school_id == applicant.school_id:
                for k in interview_slot_object_list:
                    if k.mentor.id != j.mentor.id and k.start == j.start and k.mentor.school_id == applicant.school_id:
                        j.reserved = True
                        j.save()
                        k.reserved = True
                        k.save()
                        applicant.has_interview = True
                        applicant.save()
                        interview_object = Interview.create(date_time=j.start, applicant=applicant)
                        MentorInterview.create(interview=interview_object, mentor=j.mentor)
                        MentorInterview.create(interview=interview_object, mentor=k.mentor)
                        # Connect Gmail server
                        server = Email.connect_server()

                        # Send email to the applicant about the interview
                        file = open("body_interview_applicant_email.txt", "r")
                        body = file.read().format(applicant.first_name, applicant.last_name, applicant.applicantinterview.get().date_time,
                                                  j.mentor.first_name, j.mentor.last_name,
                                                  k.mentor.first_name, k.mentor.last_name)
                        file.close()
                        email_application = Email(applicant.email, "Interview details", body)
                        email_application.send_email(server)

                        # Send email to the mentors about the inteview
                        for mentor_obj in [j, k]:
                            file = open("body_interview_mentor_email.txt", "r")
                            body = file.read().format(mentor_obj.mentor.first_name, mentor_obj.mentor.last_name,
                                                      applicant.applicantinterview.get().date_time,
                                                      applicant.first_name, applicant.last_name)
                            file.close()
                            email_application = Email(mentor_obj.mentor.email, "Interview details for mentor", body)
                            email_application.send_email(server)

                        # Disconnect Gmail server
                        Email.disconnect_server(server)
                        break_boolean = True
                        break

    # Return the list of the slots not reserved
    @classmethod
    def get_mentor_object_list_not_reserved(cls):
        # used suppress warning(# noqa) because issue: https://github.com/coleifer/peewee/issues/612
        interview_slot_object_list = list(cls.select().where(cls.reserved == False))  # noqa
        return interview_slot_object_list

    # Find two not reserved mentor in the applicant's school, save it for the applicant
    # and send an automatic email about the details of the interview
    @classmethod
    def get_interview_for_applicants(cls):
        object_list = Applicant.get_applicants_without_interview()
        for i in object_list:
            break_boolean = False
            interview_slot_object_list = cls.get_mentor_object_list_not_reserved()
            for j in interview_slot_object_list:
                if break_boolean:
                    break
                elif j.mentor.school_id == i.school_id:
                    for k in interview_slot_object_list:
                        if k.mentor.id != j.mentor.id and k.start == j.start and k.mentor.school_id == i.school_id:
                            j.reserved = True
                            j.save()
                            k.reserved = True
                            k.save()
                            i.has_interview = True
                            i.save()
                            interview_object = Interview.create(date_time=j.start, applicant=i)
                            MentorInterview.create(interview=interview_object, mentor=j.mentor)
                            MentorInterview.create(interview=interview_object, mentor=k.mentor)

                            # Connect Gmail server
                            server = Email.connect_server()

                            # Send email to the applicant about the interview
                            file = open("body_interview_applicant_email.txt", "r")
                            body = file.read().format(i.first_name, i.last_name, i.applicantinterview.get().date_time,
                                                      j.mentor.first_name, j.mentor.last_name,
                                                      k.mentor.first_name, k.mentor.last_name)
                            file.close()
                            email_application = Email(i.email, "Interview details", body)
                            email_application.send_email(server)

                            # Send email to the mentors about the inteview
                            for mentor_obj in [j, k]:
                                file = open("body_interview_mentor_email.txt", "r")
                                body = file.read().format(mentor_obj.mentor.first_name, mentor_obj.mentor.last_name,
                                                          i.applicantinterview.get().date_time,
                                                          i.first_name, i.last_name)
                                file.close()
                                email_application = Email(i.email, "Interview details for mentor", body)
                                email_application.send_email(server)

                            # Disconnect Gmail server
                            Email.disconnect_server(server)

                            break_boolean = True
                            break
