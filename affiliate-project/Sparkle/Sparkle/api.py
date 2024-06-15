from typing import List

from django.db.models import Avg, Sum
from ninja import NinjaAPI, Form
from Sparkle.models import *
from Sparkle.scheme import *
from django.contrib.auth.hashers import make_password, check_password

api = NinjaAPI()


#查询学生
@api.get("/student", response=List[StudentSchema])
def student_all(request):
    return Student.objects.all()


@api.post("/student",
          response={200: SuccessFoundSchema, 201: SuccessFoundSchema, 404: NotFoundSchema, 405: NotFoundSchema})
def student(request):
    try:
        if request.POST['request'] == 'login':
            sid = request.POST["id"]
            school = request.POST["school"]
            stu = Student.objects.get(sid=sid, school=school)
            if check_password(request.POST['password'], stu.password):
                return 200, {"message": stu.name}
            else:
                print(stu.password)
                return 404, {"message": "pwd"}

        elif request.POST['request'] == 'register':
            sid = request.POST["id"]
            name = request.POST["name"]
            password = request.POST["password"]
            email = request.POST["email"]
            school = request.POST["school"]
            try:
                stu = Student.objects.get(sid=sid, school=school)
                return 405, {"message": "acc"}
            except Student.DoesNotExist as e:
                Student.objects.create(sid=sid, name=name, password=make_password(password), email=email, school=school)
                return 201, {"message": name}

    except Student.DoesNotExist as e:
        return 404, {"message": "acc"}


#查询教师
@api.get("/teacher", response=List[StudentSchema])
def teacher_all(request):
    return Student.objects.all()


@api.post("/teacher",
          response={200: SuccessFoundSchema, 201: SuccessFoundSchema, 404: NotFoundSchema, 405: NotFoundSchema})
def teacher(request):
    try:
        if request.POST['request'] == 'login':
            tid = request.POST["id"]
            school = request.POST["school"]
            stu = Teacher.objects.get(tid=tid, school=school)
            if check_password(request.POST['password'], stu.password):
                return 200, {"message": stu.name}
            else:
                print(stu.password)
                return 404, {"message": "pwd"}

        elif request.POST['request'] == 'register':
            tid = request.POST["id"]
            name = request.POST["name"]
            password = request.POST["password"]
            email = request.POST["email"]
            school = request.POST["school"]
            try:
                tea = Teacher.objects.get(tid=tid, school=school)
                return 405, {"message": "acc"}
            except Teacher.DoesNotExist as e:
                Teacher.objects.create(tid=tid, name=name, password=make_password(password), email=email, school=school)
                return 201, {"message": name}

    except Student.DoesNotExist as e:
        return 404, {"message": "acc"}


@api.get("/course", response=List[CourseSchema])
def course(request):
    return Course.objects.all()


@api.get("/course/{id}", response=CourseSchema)
def course(request, id: int):
    return Course.objects.get(id=id)


@api.get("/course/statistics/{id}", response=StatisticsSchema)
def course_statistics(request, id: int):
    student_number = StudentCourse.objects.filter(cid=id).count()
    rating = StudentCourse.objects.filter(cid=id).aggregate(Sum('rate'), Avg('rate'))
    total_rate = rating['rate__sum']
    if total_rate is None:
        total_rate = 0
    average_rate = rating['rate__avg']
    if average_rate is None:
        average_rate = 0

    question_number = QuestionAnswer.objects.filter(cid=id).count()
    chapters = CourseChapter.objects.filter(cid=id).count()
    resource_number = ChapterResource.objects.filter(cid=id).count()
    chapter_assignment_number = ChapterAssignment.objects.filter(cid=id).count()
    assignment_number = CourseAssignment.objects.filter(cid=id).count()
    announcement_number = CourseAnnouncement.objects.filter(cid=id).count()

    print(total_rate)
    print(average_rate)

    return {"student_number": student_number, "total_rate": total_rate, "average_rate": average_rate,
            "question_number": question_number, "chapters": chapters, "resource_number": resource_number,
            "chapter_assignment_number": chapter_assignment_number, "assignment_number": assignment_number,
            "announcement_number": announcement_number}


@api.get("/course/chapter/{id}", response=List[CourseChapterSchema])
def course_chapter(request, id: int):
    return CourseChapter.objects.filter(cid=id)


@api.get("/course/chapter/{id}/{cid}", response=CourseChapterSchema)
def course_chapter(request, id: int, cid: int):
    return CourseChapter.objects.get(cid=id, id=cid)


@api.get("/course/question/{id}", response=List[CourseQuestionSchema])
def course_question(request, id: int):
    return CourseQuestion.objects.filter(cid=id)


@api.get("/course/question/{id}/{qid}", response=CourseQuestionSchema)
def course_question(request, id: int, qid: int):
    return CourseQuestion.objects.get(cid=id, id=qid)


@api.get("/course/assignment/{id}", response=List[CourseAssignmentSchema])
def course_assignment(request, id: int):
    return CourseAssignment.objects.filter(cid=id)


@api.get("/course/{id}/assignment/{aid}", response=CourseAssignmentSchema)
def course_assignment(request, id: int, aid: int):
    return CourseAssignment.objects.get(cid=id, id=aid)


@api.get("/course/{id}/announcement", response=List[CourseAnnouncementSchema])
def course_announcement(request, id: int):
    return CourseAnnouncement.objects.filter(cid=id)


@api.get("/course/{id}/announcement/{aid}", response=CourseAnnouncementSchema)
def course_announcement(request, id: int, aid: int):
    return CourseAnnouncement.objects.get(cid=id, id=aid)


@api.get("/course/{id}/resource", response=List[ChapterResourceSchema])
def course_resource(request, id: int):
    return ChapterResource.objects.filter(cid=id)


@api.get("/course/{id}/resource/{rid}", response=ChapterResourceSchema)
def course_resource(request, id: int, rid: int):
    return ChapterResource.objects.get(cid=id, id=rid)


@api.get("/course/{id}/chapter/{cid}/assignment", response=List[ChapterAssignmentSchema])
def chapter_assignment(request, id: int, cid: int):
    return ChapterAssignment.objects.filter(cid=id, chapter=cid)


@api.get("/course/{id}/chapter/{cid}/assignment/{aid}", response=ChapterAssignmentSchema)
def chapter_assignment(request, id: int, cid: int, aid: int):
    return ChapterAssignment.objects.get(cid=id, chapter=cid, id=aid)

@api.get("/course/{id}/chapter/{cid}/resource", response=List[ChapterResourceSchema])
def chapter_resource(request, id: int, cid: int):
    return ChapterResource.objects.filter(cid=id, chapter=cid)

@api.get("/course/{id}/chapter/{cid}/resource/{rid}", response=ChapterResourceSchema)
def chapter_resource(request, id: int, cid: int, rid: int):
    return ChapterResource.objects.get(cid=id, chapter=cid, id=rid)



