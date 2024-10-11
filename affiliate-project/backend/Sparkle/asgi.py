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

    return {"student_number": student_number, "total_rate": total_rate, "average_rate": average_rate,
            "question_number": question_number, "chapters": chapters, "resource_number": resource_number,
            "chapter_assignment_number": chapter_assignment_number, "assignment_number": assignment_number,
            "announcement_number": announcement_number}


@api.get('/student/course/{school}/{sid}', response=List[StudentCourseSchema])
def student_course(request, school: int, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    return StudentCourse.objects.filter(sid=id)


@api.post('/student/course/{school}/{sid}',
          response={201: SuccessFoundSchema,
                    403: NotFoundSchema,
                    404: NotFoundSchema})
def student_select_course(request, school: str, sid: int):
    try:
        id = Student.objects.get(sid=sid, school=school).id
        cid = request.POST['cid']
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if StudentCourse.objects.filter(sid=id, cid=cid).exists():
            return 403, {"message": "error"}
        StudentCourse.objects.create(sid=id, cid=cid, grade=0, rate=0, time=time)
        course_assignment = CourseAssignment.objects.filter(cid=cid)
        for assignment in course_assignment:
            StudentAssignment.objects.create(sid=id, aid=assignment.id, answer="", response="", time=time, score=0)
        return 201, {"message": "success"}
    except Student.DoesNotExist as e:
        return 404, {"message": "error"}

@api.get('/student/course/{school}/{sid}/{cid}',
          response={201: SuccessFoundSchema,
                    404: NotFoundSchema})
def student_course(request, school: str, sid: int, cid: int):
    try:
        id = Student.objects.get(sid=sid, school=school).id
        course = StudentCourse.objects.get(sid=id, cid=cid)
        return 201, {"grade": course.grade, "rate": course.rate}
    except Student.DoesNotExist as e:
        return 404, {"message": "error"}

@api.get('/student/assignment/{school}/{sid}', response=List[StudentAssignmentSchema])
def student_assignment(request, school: str, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    return StudentAssignment.objects.filter(sid=id)

@api.get('/student/assignment/unfinished/{school}/{sid}', response=List[StudentAssignmentSchema])
def student_assignment(request, school: str, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    unfinished = []
    for assignment in StudentAssignment.objects.filter(sid=id):
        if assignment.response == "":
            unfinished.append(assignment)
    return unfinished

@api.get('/student/assignment/finished/{school}/{sid}', response=List[StudentAssignmentSchema])
def student_assignment(request, school: str, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    finished = []
    for assignment in StudentAssignment.objects.filter(sid=id):
        if assignment.response != "":
            finished.append(assignment)
    return finished

@api.get('/student/course/assignment/{school}/{sid}/{cid}', response=List[StudentAssignmentSchema])
def student_course_assignment(request, school: str, sid: int, cid: int):
    id = Student.objects.get(sid=sid, school=school).id
    student_assignment = StudentAssignment.objects.filter(sid=id)
    student_course_assignment = []
    for assignment in student_assignment:
        course_assignment = CourseAssignment.objects.get(id=assignment.aid)
        if course_assignment.cid == cid:
            student_course_assignment.append(assignment)
    return student_course_assignment


@api.get('/student/course/assignment/unfinished/{school}/{sid}/{cid}', response=List[StudentAssignmentSchema])
def student_course_assignment(request, school: str, sid: int, cid: int):
    id = Student.objects.get(sid=sid, school=school).id
    StudentAssignment.objects.filter(sid=id)
    unfinished = []
    for assignment in StudentAssignment.objects.filter(sid=id):
        if assignment.response == "":
            course_assignment = CourseAssignment.objects.get(id=assignment.aid)
            if course_assignment.cid == cid:
                unfinished.append(assignment)
    return unfinished

@api.get('/student/course/assignment/finished/{school}/{sid}/{cid}', response=List[StudentAssignmentSchema])
def student_course_assignment(request, school: str, sid: int, cid: int):
    id = Student.objects.get(sid=sid, school=school).id
    finished = []
    for assignment in StudentAssignment.objects.filter(sid=id):
        if assignment.response != "":
            course_assignment = CourseAssignment.objects.get(id=assignment.aid)
            if course_assignment.cid == cid:
                finished.append(assignment)
    return finished

# 面部相关
