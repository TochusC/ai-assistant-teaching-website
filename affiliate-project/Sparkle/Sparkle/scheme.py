from datetime import datetime

from ninja import Schema
from pydantic import BaseModel
from typing import List


class StudentSchema(Schema):
    id: int
    sid: int
    name: str
    password: str
    email: str
    school: str
    enrollment: str


class TeacherSchema(Schema):
    id: int
    tid: int
    name: str
    password: str
    email: str
    school: str
    enrollment: str


class TeacherStudentSchema(Schema):
    id: int
    sid: int
    name: str
    school: str
    enrollment: str
    mental: str
    score: int


class TeacherStatisticsSchema(Schema):
    course_number: int
    resource_number: int
    assignment_number: int
    student_number: int
    star_number: int


class StudentAcademyInfoSchema(Schema):
    id: int
    sid: int
    enrollment: str
    period: str
    department: str
    major: str
    s_class: str


class StudentFamilyMemberSchema(Schema):
    id: int
    fid: int
    name: str
    relationship: str
    phone: str


class StudentFamilyInfoSchema(Schema):
    id: int
    sid: int
    location: str
    address: str
    member: List[StudentFamilyMemberSchema]


class StudentMessageSchema(Schema):
    id: int
    sid: int
    tittle: str
    sender: str
    type: str
    message: str
    time: str


class TeacherMessageSchema(Schema):
    id: int
    tid: int
    tittle: str
    sender: str
    type: str
    message: str
    time: str


class ParentMessageSchema(Schema):
    id: int
    sid: int
    tittle: str
    sender: str
    type: str
    message: str
    time: str


class CourseSchema(Schema):
    id: int
    name: str
    description: str
    illustration: str
    introduction: str
    image: str
    background: str
    target: str
    principle: str


class NumberSchema(Schema):
    message: float


class StudentBasicInfoSchema(Schema):
    id: int
    sid: int
    avatar: str
    gender: str
    birthday: str
    phone: str


class StatisticsSchema(Schema):
    student_number: int
    total_rate: int
    average_rate: float
    question_number: int
    chapters: int
    resource_number: int
    chapter_assignment_number: int
    assignment_number: int
    announcement_number: int


class StudentCourseSchema(Schema):
    sid: int
    cid: int
    grade: int
    rate: int
    time: str


class StudentInstructorInfoSchema(Schema):
    id: int
    sid: int
    name: str
    phone: str
    email: str


class StudentEmotionSchema(Schema):
    id: int
    sid: int
    raw_image: str
    processed_image: str
    age: int
    gender: str
    gender_probability: float
    emotion: str
    emotion_probability: float
    left_eye_open: float
    right_eye_open: float
    time: str
    type: str


class StudentCourseProgressSchema(Schema):
    cid: int
    cname: str
    progress: int


class StudentCourseActivitySchema(Schema):
    sid: int
    cid: int
    date: str
    time: int


class DailyTotalActivitySchema(Schema):
    date: str
    time: int


class KeyConceptSchema(Schema):
    id: int
    title: str
    description: str
    importance: int
    difficulty: int


class ProblemHistorySchema(Schema):
    pid: int
    title: str
    type: str
    difficulty: int
    importance: int
    holistic: int
    innovation: int
    score: int
    time: str


class StudentAssignmentSchema(Schema):
    sid: int
    aid: int
    answer: str
    response: str
    time: str
    score: int


class CourseQuestionSchema(Schema):
    cid: int
    tittle: str
    question: str

    sid: int
    name: str
    school: str


class StudentProblemSchema(Schema):
    sid: int
    pid: int
    answer: str
    response: str
    time: str
    score: int


class ProblemSchema(Schema):
    id: int
    cid: int
    title: str
    type: str
    description: str
    difficulty: int
    importance: int
    holistic: int
    innovation: int
    answer: str


class CourseAssignmentSchema(Schema):
    cid: int
    type: str
    title: str
    time: str
    description: str


class CourseAnnouncementSchema(Schema):
    cid: int
    title: str
    type: str
    time: str
    description: str


class ChildChapterSchema(Schema):
    cid: int
    ccid: int
    chapter: int
    title: str
    description: str


class CourseChapterSchema(Schema):
    cid: int
    chapter: int
    title: str
    description: str
    child: List[ChildChapterSchema]


class ChapterResourceSchema(Schema):
    cid: int
    type: str
    chapter: int
    title: str
    description: str
    url: str
    time: str
    size: str


class ChapterAssignmentSchema(Schema):
    cid: int
    chapter: int
    title: str
    description: str


class SuccessFoundSchema(Schema):
    message: str


class NotFoundSchema(Schema):
    message: str


class StudentMentalSchema(Schema):
    id: int
    sid: int
    type: str
    score: int


class ParentSchema(Schema):
    id: int
    sid: int
    school: str
    password: str
