from build import *
from new_applicants import *
from model_applicant import *
# Write here your console application
Applicant.closest_school()
Applicant.application_code_generator()

# testing with a valid number
valid_number = Applicant.select(Applicant.application_code).where(Applicant.id == 1).get().application_code
applicant = Applicant.get_applicant_object_by_application_code(valid_number)
status, school_name = applicant.get_status_and_school()
print ("Application code: {0}\nStatus: {1}\nSchool: {2}".format(valid_number, status, school_name))
