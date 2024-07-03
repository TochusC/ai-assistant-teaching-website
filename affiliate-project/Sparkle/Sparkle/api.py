from typing import List

import requests
from django.db.models import Avg, Sum
from ninja import NinjaAPI, Form
from Sparkle.models import *
from Sparkle.scheme import *
from django.contrib.auth.hashers import make_password, check_password

api = NinjaAPI()
CDN_URL = "http://localhost:3000/assests/"


#查询学生
@api.get("/student", response=List[StudentSchema])
def student_all(request):
    return Student.objects.all()

@api.get("/student/{id}", response=StudentSchema)
def student_all(request, id: int):
    return Student.objects.get(id=id)

@api.post("/student",
          response={200: StudentSchema, 201: StudentSchema, 404: NotFoundSchema, 405: NotFoundSchema})
def student(request):
    try:
        if request.POST['request'] == 'login':
            sid = request.POST["id"]
            school = request.POST["school"]
            stu = Student.objects.get(sid=sid, school=school)
            if check_password(request.POST['password'], stu.password):
                return 200, stu
            else:
                return 404, {"message": "pwd"}

        elif request.POST['request'] == 'register':
            sid = request.POST["id"]
            name = request.POST["name"]
            password = request.POST["password"]
            email = request.POST["email"]
            school = request.POST["school"]
            if Student.objects.filter(sid=sid, school=school).exists():
                return 405, {"message": "acc"}
            stu = Student.objects.create(sid=sid, name=name, password=make_password(password), email=email,
                                         school=school)
            return 201, stu

    except Student.DoesNotExist as e:
        return 404, {"message": "acc"}
@api.get('/student/info/family/{sid}', response={200: StudentFamilyInfoSchema, 404: List})
def student_family(request, sid: int):
    if not StudentFamilyInfo.objects.filter(sid=sid).exists():
        return 404, []
    family = StudentFamilyInfo.objects.get(sid=sid)
    family.member = StudentFamilyMember.objects.filter(fid=family.id)
    return 200, family

@api.get("/student/course/progress/{sid}", response=List[StudentCourseProgressSchema])
def student_course_progress(request, sid: int):
    student_course = StudentCourse.objects.filter(sid=sid)
    student_course_progress = []

    for course in student_course:
        course_assignments = CourseAssignment.objects.filter(cid=course.cid)
        total_assignment = len(course_assignments)
        finished_assignment = 0
        for assignment in course_assignments:
            if StudentAssignment.objects.filter(sid=sid, aid=assignment.id).exists():
                finished_assignment += 1

        if total_assignment != 0:
            progress = int(finished_assignment / total_assignment * 100)
        else:
            progress = 100

        student_course_progress.append({
            'cid': course.cid,
            'cname': Course.objects.get(id=course.cid).name,
            'progress': progress
        })

    return student_course_progress

@api.get('/parent', response=List[ParentSchema])
def parent_all(request):
    return Parent.objects.all()
@api.post('/parent', response={200: StudentSchema, 201: SuccessFoundSchema, 404: NotFoundSchema, 405: NotFoundSchema})
def parent(request):
    school = request.POST['school']
    sid = request.POST['id']
    password = request.POST['password']
    try:
        if request.POST['request'] == 'login':
            if Parent.objects.filter(sid=sid, school=school).exists():
                parent = Parent.objects.get(sid=sid, school=school)
                if check_password(password, parent.password):
                    return 200, Student.objects.get(id=sid)
                else:
                    return 404, {"message": "pwd"}
            else:
                return 404, {"message": "acc"}
        return 405, {"message": "error"}
    except Student.DoesNotExist as e:
        return 404, {"message": "acc"}

@api.get("/student/course/activity/{sid}/{cid}", response=List[StudentCourseActivitySchema])
def student_course_progress(request, sid: int, cid: int):
    return StudentActivity.objects.filter(sid=sid, cid=cid).order_by('date')

@api.get("/student/activity/{sid}", response=List[DailyTotalActivitySchema])
def student_activity(request, sid: int):
    student_activity = StudentActivity.objects.filter(sid=sid, cid=1).order_by('date')
    data_activity = []
    for activity in student_activity:
        date = activity.date
        time = StudentActivity.objects.filter(sid=sid, date=date).aggregate(Sum('time'))['time__sum']
        data_activity.append({
            'date': date,
            'time': time,
        })
    return data_activity


@api.get("/student/mental/", response=List[StudentMentalSchema])
def student_mental(request):
    return StudentMental.objects.all()


@api.get("/student/mental/{sid}", response=List[StudentMentalSchema])
def student_mental(request, sid: int):
    return StudentMental.objects.filter(sid=sid)


@api.get("/student/info/basic/{sid}", response=StudentBasicInfoSchema)
def student_info_basic(request, sid: int):
    return StudentBasicInfo.objects.get(sid=sid)


@api.post("/student/info/basic/{sid}", response={201: SuccessFoundSchema})
def student_info_basic(request, sid: int):
    gender = request.POST['gender']
    birthday = request.POST['birthday']
    phone = request.POST['phone']
    if StudentBasicInfo.objects.filter(sid=sid).exists():
        StudentBasicInfo.objects.filter(sid=sid).update(gender=gender, birthday=birthday, phone=phone)
    else:
        StudentBasicInfo.objects.create(sid=sid,
                                        avatar='http://localhost:3000/assests/default/avatar.png',
                                        gender=gender, birthday=birthday, phone=phone)

    return 201, {"message": "success"}

@api.post("/student/info/basic/avatar/{sid}", response={201: SuccessFoundSchema, 404: NotFoundSchema})
def student_update_avatar(request, sid: int):
    avatar = request.FILES['avatar']
    avatar_url = CDN_URL + 'user/' + str(sid) + '/avatar.png'
    headers = {
        'Content-Type': 'image/png'
    }
    response = requests.post(avatar_url, headers=headers, data=avatar)
    if response.status_code == 200:
        if StudentBasicInfo.objects.filter(sid=sid).exists():
            StudentBasicInfo.objects.filter(sid=sid).update(avatar=avatar_url)
        else:
            StudentBasicInfo.objects.create(sid=sid, avatar=avatar_url)
        return 201, {"message": "success"}
    else:
        return 404, {"message": "error"}


@api.post('/student/emotion/{sid}', response={201: SuccessFoundSchema})
def student_emotion(request, sid: int):
    raw_img = request.POST['image']
    processed_img = request.POST['processed_image']
    age = request.POST['age']
    gender = request.POST['gender']
    gender_probability = request.POST['gender_probability']
    emotion = request.POST['emotion']
    emotion_probability = request.POST['emotion_probability']
    left_eye_open = request.POST['left_eye_open']
    right_eye_open = request.POST['right_eye_open']
    record_type = request.POST['type']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    StudentEmotion.objects.create(sid=sid, raw_image=raw_img, processed_image=processed_img,
                                  age=age, gender=gender, gender_probability=gender_probability,
                                  emotion=emotion, emotion_probability=emotion_probability, type=record_type,
                                  left_eye_open=left_eye_open, right_eye_open=right_eye_open, time=time)
    return 201, {"message": "success"}


@api.get('/student/emotion/{sid}', response={200: List[StudentEmotionSchema]})
def student_emotion(request, sid: int):
    return reversed(StudentEmotion.objects.filter(sid=sid))


@api.get('/student/emotion/status/{sid}', response={200: SuccessFoundSchema})
def student_emotion(request, sid: int):
    emotion_values = {
        'angry': -80,
        'disgust': -60,
        'fear': -40,
        'happy': 100,
        'sad': -40,
        'surprise': 50,  # 惊讶可以被视为轻微的正向情绪
        'neutral': 10,
        'pouty': -10,  # 假设撅嘴是一种轻微的不满
        'grimace': 20  # 鬼脸可能是中性或混合情绪
    }

    emotions = StudentEmotion.objects.filter(sid=sid)
    energy_value = 0
    nums = 8

    for emotion in emotions[::-1]:
        energy_value += emotion_values[emotion.emotion] * emotion.emotion_probability
        nums -= 1
        if nums == 0:
            break
    energy_value = (energy_value + 640) / 14.4
    if energy_value < 0:
        energy_value = 0
    if energy_value > 100:
        energy_value = 100
    return 200, {"message": str(energy_value)}




@api.get("/student/info/academy/{sid}", response=StudentAcademyInfoSchema)
def student_info_academy(request, sid: int):
    return StudentAcademyInfo.objects.get(sid=sid)


@api.get("/student/info/instructor/{sid}", response={200: StudentInstructorInfoSchema, 404: List})
def student_info_instructor(request, sid: int):
    if not StudentInstructorInfo.objects.filter(sid=sid).exists():
        return 404, []
    return 200, StudentInstructorInfo.objects.get(sid=sid)


@api.get("/student/info/family/{sid}", response={200: StudentFamilyInfoSchema, 404: List})
def student_info_family(request, sid: int):
    if not StudentFamilyInfo.objects.filter(sid=sid).exists():
        return 404, []
    family = StudentFamilyInfo.objects.get(sid=sid)
    family.member = StudentFamilyMember.objects.filter(fid=family.id)
    return 200, family


@api.get("/student/info/family/member/{fid}", response=List[StudentFamilyMemberSchema])
def student_info_family_member(request, fid: int):
    return StudentFamilyMember.objects.filter(fid=fid)


@api.get("/student/problem/history/{sid}", response=List[ProblemHistorySchema])
def student_problem_history(request, sid: int):
    student_problem = StudentProblem.objects.filter(sid=sid)
    problem_history = []
    for sp in student_problem:
        problem = Problem.objects.get(id=sp.pid)
        problem_history.append({
            'pid': problem.id,
            'title': problem.title,
            'type': problem.type,
            'difficulty': problem.difficulty,
            'importance': problem.importance,
            'holistic': problem.holistic,
            'innovation': problem.innovation,
            'score': sp.score,
            'time': sp.time
        })
    return problem_history


@api.get("/student/problem/record/{school}/{sid}", response=List[StudentProblemSchema])
def student_problem(request, school: str, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    student_problem = StudentProblem.objects.filter(sid=id)
    return student_problem


@api.get("/student/problem/unfinished/{school}/{sid}", response=List[ProblemSchema])
def student_problem(request, school: str, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    student_course = StudentCourse.objects.filter(sid=id)
    student_problem = []
    for course in student_course:
        course_problem = Problem.objects.filter(cid=course.cid)
        for problem in course_problem:
            if not StudentProblem.objects.filter(pid=problem.id, sid=id).exists():
                student_problem.append(problem)
    return student_problem


#查询教师
@api.get("/teacher", response=List[StudentSchema])
def teacher_all(request):
    return Student.objects.all()


@api.post("/teacher",
          response={200: TeacherSchema, 201: SuccessFoundSchema, 404: NotFoundSchema, 405: NotFoundSchema})
def teacher(request):
    try:
        if request.POST['request'] == 'login':
            tid = request.POST["id"]
            school = request.POST["school"]
            tea = Teacher.objects.get(tid=tid, school=school)
            if check_password(request.POST['password'], tea.password):
                return 200, tea
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

@api.get('/teacher/statistics/{tid}', response=TeacherStatisticsSchema)
def teacher_statistics(request, tid: int):
    course_number = 0
    resource_number = 0
    assignment_number = 0
    student_number = 0
    star_number = 0
    teacher_course = TeacherCourse.objects.filter(tid=tid)
    course_number = len(teacher_course)
    for course in teacher_course:
        resource_number += ChapterResource.objects.filter(cid=course.cid).count()
        assignment_number += CourseAssignment.objects.filter(cid=course.cid).count()
        student_number += StudentCourse.objects.filter(cid=course.cid).count()
        star_number += StudentCourse.objects.filter(cid=course.cid).aggregate(Sum('rate'))['rate__sum']
    return {"course_number": course_number, "resource_number": resource_number, "assignment_number": assignment_number,
            "student_number": student_number, "star_number": star_number}


@api.get('/teacher/student/{tid}', response=List[TeacherStudentSchema])
def teacher_student(request, tid: int):
    teacher_course = TeacherCourse.objects.filter(tid=tid)
    students = []
    students_tuple = ()
    for course in teacher_course:
        student_course = StudentCourse.objects.filter(cid=course.cid)
        for sc in student_course:
            stu = Student.objects.get(id=sc.sid)
            if stu not in students_tuple:
                student_mental = StudentMental.objects.filter(sid=stu.sid)
                students.append({
                    'id': stu.id,
                    'sid': stu.sid,
                    'name': stu.name,
                    'school': stu.school,
                    'enrollment': stu.enrollment,
                    'mental': student_mental[0].type,
                    'score': student_mental[0].score
                })
                students_tuple += (stu,)

    return students


@api.get("/teacher/course/{tid}", response=List[CourseSchema])
def teacher_course(request, tid: int):
    teacher_course = TeacherCourse.objects.filter(tid=tid)
    courses = []
    for course in teacher_course:
        courses.append(Course.objects.get(id=course.cid))
    return courses


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


@api.get('/student/course/{sid}', response=List[CourseSchema])
def student_course(request, sid: int):
    student_course = StudentCourse.objects.filter(sid=sid)
    courses = []
    for course in student_course:
        courses.append(Course.objects.get(id=course.cid))
    return courses

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


@api.get('/student/assignment/unfinished/{school}/{sid}', response=List[CourseAssignmentSchema])
def student_assignment(request, school: str, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    unfinished = []
    for course in StudentCourse.objects.filter(sid=id):
        for assignment in CourseAssignment.objects.filter(cid=course.cid):
            if not StudentAssignment.objects.filter(sid=id, aid=assignment.id).exists():
                unfinished.append(assignment)
    return unfinished


@api.get('/student/assignment/finished/{school}/{sid}', response=List[StudentAssignmentSchema])
def student_assignment(request, school: str, sid: int):
    id = Student.objects.get(sid=sid, school=school).id
    return StudentAssignment.objects.filter(sid=id)


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


@api.get("/course/chapter/{id}", response=List[CourseChapterSchema])
def course_chapter(request, id: int):
    chapters = CourseChapter.objects.filter(cid=id)
    for chapter in chapters:
        chapter.child = ChildChapter.objects.filter(cid=id, ccid=chapter.id)
    return chapters


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


@api.get("/course/assignment/{id}/{aid}", response=CourseAssignmentSchema)
def course_assignment(request, id: int, aid: int):
    return CourseAssignment.objects.get(cid=id, id=aid)


@api.get("/course/announcement/{id}", response=List[CourseAnnouncementSchema])
def course_announcement(request, id: int):
    return CourseAnnouncement.objects.filter(cid=id)


@api.get("/course/announcement/{id}/{aid}", response=CourseAnnouncementSchema)
def course_announcement(request, id: int, aid: int):
    return CourseAnnouncement.objects.get(cid=id, id=aid)


@api.get("/course/resource/{id}", response=List[ChapterResourceSchema])
def course_resource(request, id: int):
    return ChapterResource.objects.filter(cid=id)


@api.get("/course/resource/{id}/{rid}", response=ChapterResourceSchema)
def course_resource(request, id: int, rid: int):
    for i in ChapterResource.objects.filter(cid=id):
        print(i.id, i.title, i.description, i.chapter)
    return ChapterResource.objects.get(cid=id, id=rid)


@api.get("/course/chapter/assignment/{id}/{cid}", response=List[ChapterAssignmentSchema])
def chapter_assignment(request, id: int, cid: int):
    return ChapterAssignment.objects.filter(cid=id, chapter=cid)


@api.get("/course/chapter/assignment/{id}/{aid}/{cid}", response=ChapterAssignmentSchema)
def chapter_assignment(request, id: int, cid: int, aid: int):
    return ChapterAssignment.objects.get(cid=id, chapter=cid, id=aid)


@api.get("/course/chapter/resource/{id}/{cid}", response=List[ChapterResourceSchema])
def chapter_resource(request, id: int, cid: int):
    return ChapterResource.objects.filter(cid=id, chapter=cid)


@api.get("/course/chapter/resource/{id}/{cid}/{rid}", response=ChapterResourceSchema)
def chapter_resource(request, id: int, cid: int, rid: int):
    return ChapterResource.objects.get(cid=id, chapter=cid, id=rid)


#题目相关
@api.get('/problem', response=List[ProblemSchema])
def problem_all(request):
    return Problem.objects.all()


@api.get('/problem/{id}', response=ProblemSchema)
def problem(request, id: int):
    return Problem.objects.get(id=id)


@api.get('/problem/key_concept/{pid}', response=List[KeyConceptSchema])
def problem_key_concept(request, pid: int):
    problem_key_concept = ProblemKeyConcept.objects.filter(pid=pid)
    key_concept = []
    for pkc in problem_key_concept:
        key_concept.append(KeyConcept.objects.get(id=pkc.kcid))
    return key_concept
