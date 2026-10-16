from abc import ABC,abstractmethod
class Course:
    total_courses = 0

    def __init__(self,course_id ,course_name, course_code, faculty):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.faculty = faculty
        
        Course.total_courses += 1
        
    

    def __str__(self):
        return f"{self.course_id} -{self.course_name} - {self.course_code} -({self.faculty})"

class Student:
    
    
    def __init__(self, student_id, first_name, last_name, faculty, contact, reg_no, year_of_study, gender, course):
    
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.faculty = faculty
        self.contact = contact
        self.email = self.get_email()
        self.reg_no = reg_no
        self.year_of_study = year_of_study
        self.gender = gender
        self.course = course

    
    
    def get_email(self):
        self.email = f" {self.first_name}{self.last_name}@iuiu.ac"
        return self.email
        
        
    def __str__(self):
        return (
            f"{self.student_id} -> {self.first_name} -> {self.last_name} -> "
            f"{self.faculty} -> {self.contact} -> {self.email} -> {self.reg_no} -> "
            f"{self.year_of_study} -> {self.gender} -> {self.course}"
        )
    

class Lecturer:
    def __init__(self, lecturer_id, first_name, last_name, faculty,gender,  contact,  department):
        self.lecturer_id = lecturer_id
        self.first_name = first_name
        self.last_name = last_name
        self.faculty = faculty
        self.gender = gender
        self.contact = contact
        self.email = self.get_email()
        self.department = department

    def get_email(self):
        self.email = f" {self.first_name}{self.last_name}@iuiu.ac"
        return self.email
    
    def __str__(self):
        return f"{self.lecturer_id} -> {self.first_name} {self.last_name} -> {self.faculty} ->{self.gender} -> {self.contact} -> {self.email} ->{self.department} "
    

    

class CourseUnit:
    def __init__(self,courseunit_id, courseunit_name, courseunit_code, course, credit_units):
        self.corseunit_id = courseunit_id
        self.courseunit_name = courseunit_name
        self.courseunit_code = courseunit_code
        self.course = course
        self.credit_units = credit_units

    def __str__(self):
        return f"{self.courseunit_name} ({self.courseunit_code})"
    
    
class Timetable:
    def __init__(self, session, day, course_unit, lecturer, start_time, end_time):
        self.session = session
        self.day = day
        self.course_unit = course_unit
        self.lecturer = lecturer
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return (
            f"{self.day} | {self.course_unit} | {self.lecturer} | "
            f"{self.start_time} - {self.end_time}"
        )

class Attendance(ABC):
    def __init__(self,id, date, ):
        self.id = id
        self.date = date
        
    def __str__(self):
        return f"{self.id} -> {self.date}"
    
    @abstractmethod
    def change_status(self):
        pass
    
    def record_status(self):
        pass
    
    @property
    def get_status(self):
        return self._status
    
    @property
    def record_status(self, value):
        if value in ["Present","Absent"]:
                    
            self._status = value
        else:
            print("Invalid option")
                
    
class StudentAttendance(Attendance):
    
    def __init__(self, id, date,  student_id, timetable):
        super(). __init__(id , date)
        self._status = "Present"
        self.student_id = student_id
        self.timetable = timetable
         
    
    def change_status(self,value):
        
        return self.record_status (value)
    
    
            
            
    def __str__(self):
        return f"{self.id} | {self.date} | {self._status} | {self.student_id}"
    
class LecturerAttendance(Attendance):
    def __init__(self, id ,date,  lecturer_id):
        super(). __init__(id, date)
        self._status = "Present"
        self.lecturer_id = lecturer_id
        
    def change_status(self,value):
            
        return self.record_status(value)
            
        
    def __str__(self):
        return f"{self.id} -> {self.date} -> {self._status} -> {self.lecturer_id}"
        
    

class Studysession:
    def __init__(self, study_session_id, academic_year, semester):
        self.study_session_id = study_session_id
        self.academic_year = academic_year
        self.semester = semester



    def __str__(self):
        return f"{self.academic_year} - {self.semester} - {self._status}"

    

   

 
 
 