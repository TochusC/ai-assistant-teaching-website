from ninja import Schema
from pydantic import BaseModel
from typing import List


class StudentSchema(Schema):
    Student_name: str
    Student_id: int
    password: str

class TeacherSchema(Schema):
    Teacher_name: str
    Teacher_id: int
    password: str


class LessonSchema(Schema):
    Lesson_name: str
    Lesson_id: int

class NoticeSchema(Schema):
    types: str
    title: str
    course: str
    startTime: str
    endTime: str
    announceTime: str

class Item(Schema):
    Student_id: int
    Lesson_id: int

class ChooseSchema(Schema):
    Student_id: int
    Lesson_id: int
    grade: int

class CourseSchema(Schema):
    Course_id: int
    name: str
    description: str
    illustration: str
    introduction: str
    image: str




class DesignSchema(Schema):
    background: str
    target: str
    principle: str

class QaSchema(Schema):
    question: str
    answer: str
class StatisticsSchema(Schema):
    student: int
    rate: float
    total_rate: float
    rate_num: int
    qa: int
    resources: int
    homework: int
    announcement: int
    chapter: int
class HomeworkSchema(Schema):
    # Homework_id: int
    type: str
    name: str
    start: str
    end: str
    id: int

class ResourceSchema(Schema):
    type: str
    name: str
    time: str
    size: str
    url: str


class AnnouncementSchema(Schema):
    type: str
    content: str
    time: str
class CatalogSchema(Schema):
    label: str

class CatalogSum(Schema):
     label: str
     children: List[CatalogSchema]


class Course_DesignSchema(Schema):
    id: int
    name: str
    description: str
    illustration: str
    introduction: str
    image: str
    design: DesignSchema
    catalog: List[CatalogSum]
    announcement: List[AnnouncementSchema]
    qa: List[QaSchema]
    resources: List[ResourceSchema]
    homework: List[HomeworkSchema]
    statistics: StatisticsSchema



class LoginStuedntSchema(Schema):
    Student_name: str
    Student_id: int
    password: str
    password_verify: str

class LoginTeacherSchema(Schema):
    Teacher_name: str
    Teacher_id: int
    password: str
    password_verify: str





class SuccessFoundSchmea(Schema):
    message: str
class NotFoundSchema(Schema):
    message: str




