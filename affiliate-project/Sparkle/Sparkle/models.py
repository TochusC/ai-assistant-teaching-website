from django.db import models


# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    school = models.CharField(max_length=250)


class StudentCourse(models.Model):
    sid = models.IntegerField()
    cid = models.IntegerField()
    grade = models.IntegerField()
    rate = models.IntegerField()


class Teacher(models.Model):
    tid = models.IntegerField()
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    school = models.CharField(max_length=250)


class TeacherCourse(models.Model):
    tid = models.IntegerField()
    cid = models.IntegerField()


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    illustration = models.CharField(max_length=250)
    introduction = models.TextField()
    image = models.CharField(max_length=255)

    background = models.CharField(max_length=250)
    target = models.CharField(max_length=250)
    principle = models.CharField(max_length=250)


class CourseQuestion(models.Model):
    cid = models.IntegerField()
    tittle = models.CharField(max_length=250)
    question = models.TextField()

    sid = models.IntegerField()
    name = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    time = models.DateTimeField()


class CourseAssignment(models.Model):
    cid = models.IntegerField()
    type = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    deadline = models.DateTimeField()
    publish_time = models.DateTimeField()


class QuestionAnswer(models.Model):
    cid = models.IntegerField()
    answer = models.TextField()

    sid = models.IntegerField()
    name = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    time = models.DateTimeField()


class CourseChapter(models.Model):
    cid = models.IntegerField()
    chapter = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()


class ChildChapter(models.Model):
    cid = models.IntegerField()
    ccid = models.IntegerField()
    chapter = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()


class CourseAnnouncement(models.Model):
    cid = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    time = models.DateTimeField()


class ChapterResource(models.Model):
    cid = models.IntegerField()
    chapter = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.CharField(max_length=250)


class ChapterAssignment(models.Model):
    cid = models.IntegerField()
    chapter = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    deadline = models.DateTimeField()
    publish_time = models.DateTimeField()


class StudentAssignment(models.Model):
    sid = models.IntegerField()
    aid = models.IntegerField()


class Assignment(models.Model):
    id = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    deadline = models.DateTimeField()
    publish_time = models.DateTimeField()
