from django.db import models


# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    enrollment = models.CharField(max_length=250)

class StudentMessage(models.Model):
    sid = models.IntegerField()
    tittle = models.CharField(max_length=250)
    sender = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    time = models.CharField(max_length=250)

class TeacherMessage(models.Model):
    tid = models.IntegerField()
    tittle = models.CharField(max_length=250)
    sender = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    time = models.CharField(max_length=250)

class ParentMessage(models.Model):
    sid = models.IntegerField()
    tittle = models.CharField(max_length=250)
    sender = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    time = models.CharField(max_length=250)

class StudentMental(models.Model):
    sid = models.IntegerField()
    type = models.CharField(max_length=250)
    score = models.IntegerField()


class StudentCourse(models.Model):
    sid = models.IntegerField()
    cid = models.IntegerField()
    grade = models.IntegerField()
    rate = models.IntegerField()
    time = models.CharField(max_length=250)


class StudentActivity(models.Model):
    sid = models.IntegerField()
    cid = models.IntegerField()
    time = models.IntegerField()
    date = models.CharField(max_length=250)


class Teacher(models.Model):
    tid = models.IntegerField()
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    enrollment = models.CharField(max_length=250)


class Parent(models.Model):
    sid = models.IntegerField()
    school = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


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


class CourseAssignment(models.Model):
    cid = models.IntegerField()
    type = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    description = models.TextField()


class QuestionAnswer(models.Model):
    cid = models.IntegerField()
    answer = models.TextField()

    sid = models.IntegerField()
    name = models.CharField(max_length=250)
    school = models.CharField(max_length=250)


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
    type = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    description = models.TextField()


class ChapterResource(models.Model):
    cid = models.IntegerField()
    type = models.CharField(max_length=250)
    chapter = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    size = models.CharField(max_length=250)


class ChapterAssignment(models.Model):
    cid = models.IntegerField()
    chapter = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()


class StudentProblem(models.Model):
    sid = models.IntegerField()
    pid = models.IntegerField()
    answer = models.TextField()
    response = models.TextField()
    score = models.IntegerField()
    time = models.CharField(max_length=250)


class StudentInstructorInfo(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)


class StudentBasicInfo(models.Model):
    sid = models.IntegerField()
    avatar = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    birthday = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)


class StudentEmotion(models.Model):
    sid = models.IntegerField()
    raw_image = models.TextField()
    processed_image = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    gender_probability = models.FloatField()
    emotion = models.CharField(max_length=250)
    emotion_probability = models.FloatField()
    left_eye_open = models.FloatField()
    right_eye_open = models.FloatField()
    time = models.CharField(max_length=250)
    type = models.CharField(max_length=250)


class StudentAcademyInfo(models.Model):
    sid = models.IntegerField()
    enrollment = models.CharField(max_length=250)
    period = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    major = models.CharField(max_length=250)
    s_class = models.CharField(max_length=250)


class StudentFamilyInfo(models.Model):
    sid = models.IntegerField()
    location = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


class StudentFamilyMember(models.Model):
    fid = models.IntegerField()
    name = models.CharField(max_length=250)
    relationship = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)


class ChapterProblem(models.Model):
    cid = models.IntegerField()
    ccid = models.IntegerField()
    pid = models.IntegerField()


class ChapterKeyConcept(models.Model):
    cid = models.IntegerField()
    ccid = models.IntegerField()
    kid = models.IntegerField()


class Problem(models.Model):
    cid = models.IntegerField()
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    description = models.TextField()
    difficulty = models.IntegerField()
    importance = models.IntegerField()
    holistic = models.IntegerField()
    innovation = models.IntegerField()
    answer = models.TextField()


class ProblemKeyConcept(models.Model):
    pid = models.IntegerField()
    kcid = models.IntegerField()


class KeyConcept(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    importance = models.IntegerField()
    difficulty = models.IntegerField()


class StudentAssignment(models.Model):
    sid = models.IntegerField()
    aid = models.IntegerField()
    answer = models.TextField()
    response = models.TextField()
    score = models.IntegerField()
    time = models.CharField(max_length=250)


class Assignment(models.Model):
    id = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.TextField()
