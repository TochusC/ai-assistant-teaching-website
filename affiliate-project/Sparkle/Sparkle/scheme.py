from ninja import Schema
from pydantic import BaseModel
from typing import List


class StudentSchema(Schema):
    id: int
    name: str
    password: str
    email: str
    school: str


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


class CourseQuestionSchema(Schema):
    cid: int
    tittle: str
    question: str
    sid: int
    name: str
    school: str
    time: str


class CourseAssignmentSchema(Schema):
    cid: int
    type: str
    title: str
    description: str
    deadline: str
    publish_time: str


class CourseAnnouncementSchema(Schema):
    cid: int
    title: str
    content: str
    time: str


class CourseChapterSchema(Schema):
    cid: int
    title: str
    content: str
    time: str


class ChapterResourceSchema(Schema):
    cid: int
    title: str
    content: str
    time: str


class ChapterAssignmentSchema(Schema):
    cid: int
    title: str
    content: str
    time: str


class ChapterResourceSchema(Schema):
    cid: int
    title: str
    content: str
    time: str


class SuccessFoundSchema(Schema):
    message: str


class NotFoundSchema(Schema):
    message: str
