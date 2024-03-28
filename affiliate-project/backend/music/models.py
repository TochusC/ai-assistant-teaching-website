from django.db import models

# Create your models here.


class Student(models.Model):
    Student_name = models.CharField(max_length=250)
    Student_id = models.IntegerField()
    password = models.CharField(max_length=250)

class Teacher(models.Model):
    Teacher_name = models.CharField(max_length=250)
    Teacher_id = models.IntegerField()
    password = models.CharField(max_length=250)


class Lesson(models.Model):
    Lesson_name = models.CharField(max_length=250)
    Lesson_id = models.IntegerField()

class Choose(models.Model):
    Student_id = models.IntegerField()
    Lesson_id = models.IntegerField()
    grade = models.IntegerField()

class Professor(models.Model):
    Teacher_id = models.IntegerField()
    Lesson_id = models.IntegerField()


class Notice(models.Model):
    types = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    startTime = models.CharField(max_length=250)
    endTime = models.CharField(max_length=250)
    announceTime = models.CharField(max_length=250)


class Course(models.Model):
    Course_id = models.IntegerField()
    name = models.CharField(max_length=250)
    description = models.TextField()
    illustration = models.CharField(max_length=250)
    introduction = models.TextField()
    image = models.CharField(max_length=255)


class Design(models.Model):
    Design_id = models.IntegerField()
    background = models.CharField(max_length=250)
    target = models.CharField(max_length=250)
    principle = models.CharField(max_length=250)


class Course_Design(models.Model):
    Course_id = models.IntegerField()
    Design_id = models.IntegerField()






class Sum(models.Model):
    Course_id = models.IntegerField()
    Design_id = models.IntegerField()
    label_id =models.IntegerField()
    announcement_id = models.IntegerField()
    qa_id = models.IntegerField()
    resource_id = models.IntegerField()
    homework_id = models.IntegerField()
    Statistics_id = models.IntegerField()

class Statistics(models.Model):
    Statistics_id = models.IntegerField()
    student = models.IntegerField()
    rate = models.FloatField()
    total_rate = models.FloatField()
    rate_num = models.IntegerField()
    qa = models.IntegerField()
    resources = models.IntegerField()
    homework = models.IntegerField()
    announcement = models.IntegerField()
    chapter = models.IntegerField()

class Homeworka(models.Model):
    Homework_id = models.IntegerField()
    type = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    start = models.CharField(max_length=250)
    end = models.CharField(max_length=250)
    Homework_intern_id=models.IntegerField()


class Resources(models.Model):
    resource_id = models.IntegerField()
    type = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    size = models.CharField(max_length=250)
    url = models.CharField(max_length=250)


class Qa(models.Model):
    qa_id = models.IntegerField()
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)

class Announcement(models.Model):
    announcement_id = models.IntegerField()
    type = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    time = models.CharField(max_length=250)

class Catalogs(models.Model):
    label_id = models.IntegerField()
    label_intern_id = models.IntegerField()
    label_fellow = models.CharField(max_length=250)







