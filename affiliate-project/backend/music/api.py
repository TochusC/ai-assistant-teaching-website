from typing import List
from ninja import NinjaAPI,Form
from music.models import (Course,Design,Statistics,Homeworka,Resources,Qa,
                          Announcement,Catalogs,Sum,Student,Teacher,Lesson,Notice,Choose)
from music.scheme import (NotFoundSchema,CourseSchema,DesignSchema,Course_DesignSchema,
                          StatisticsSchema,HomeworkSchema,ResourceSchema,QaSchema,AnnouncementSchema,
                          CatalogSchema,CatalogSum,StudentSchema,TeacherSchema,LessonSchema,
                          NoticeSchema,Item,ChooseSchema,SuccessFoundSchmea,LoginStuedntSchema,
                          LoginTeacherSchema)

api = NinjaAPI()


#查
#查询学生

@api.get("/student", response=List[StudentSchema])
def student(request):
    return Student.objects.all()

@api.get("/student/{student_id}", response={200: List[StudentSchema], 404: NotFoundSchema})
def students(request, student_id: int):
    try:
        student = Student.objects.get(pk=student_id)
        return [student]
    except Student.DoesNotExist as e:
        return 404, {"message": "Student does not exist"}




#查询老师
@api.get("/teacher", response=List[TeacherSchema])
def teacher(request):
    return Teacher.objects.all()
@api.get("/teacher/{teacher_id}",response={200: List[TeacherSchema], 404: NotFoundSchema})
def teachers(request, teacher_id: int):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        return [teacher]
    except Teacher.DoesNotExist as e:
        return 404, {"message": "Teacher does not exist"}





#查询课程
@api.get("/lesson", response=List[LessonSchema])
def lesson(request):
    return Lesson.objects.all()

@api.get("/lesson/{lesson_id}", response={200: List[LessonSchema], 404: NotFoundSchema})
def lessons(request, lesson_id: int):
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
        return [lesson]
    except Lesson.DoesNotExist as e:
        return 404, {"message": "Lesson does not exist"}

#增
@api.post("/student",response={201: StudentSchema})
def create_student(request, student: StudentSchema):
    Student.objects.create(**student.dict())
    return student

@api.post("/teacher",response={201: TeacherSchema})
def create_teacher(request, teacher: TeacherSchema):
    Teacher.objects.create(**teacher.dict())
    return teacher

@api.post("/lesson",response={201: LessonSchema})
def creat_lesson(request, lesson: LessonSchema):
    Lesson.objects.create(**lesson.dict())
    return lesson


@api.get("/notice",response=List[NoticeSchema])
def notice(request):
    return Notice.objects.all()
@api.get("/notice/{notice_id}",response={200: List[NoticeSchema], 404: NotFoundSchema})
def notices(request, notice_id: int):
    try:
        notice = Notice.objects.get(pk=notice_id)
        return [notice]
    except Notice.DoesNotExist as e:
        return 404, {"message": "Notice does not exist"}


#验证学生登录
@api.post("/yanzheng/student",response={200:SuccessFoundSchmea, 404:NotFoundSchema})
def yanzheng_student(request,item:Form[StudentSchema]):
    student_exists = Student.objects.filter(
        Student_name = item.Student_name,
        Student_id = item.Student_id,
        password = item.password
    ).exists()

    if student_exists:
        # 如果匹配的学生存在
        return {"message": "学生信息在数据表中存在。"}
    else:
        # 如果没有找到匹配的学生
        return 404, {"message": "学生信息不在数据表中。"}

#验证教师登录
@api.post("/yanzheng/teacher",response={200:SuccessFoundSchmea, 404:NotFoundSchema})
def yanzheng_teacher(request,item:Form[TeacherSchema]):

    teacher_exists = Teacher.objects.filter(
        Teacher_name = item.Teacher_name,
        Teacher_id = item.Teacher_id,
        password = item.password
    ).exists()

    if teacher_exists:
        # 如果匹配的老师存在
        return {"message": "老师信息在数据表中存在。"}
    else:
        # 如果没有找到匹配的老师
        return 404, {"message": "老师信息不在数据表中。"}



#学生注册
@api.post("/zhuce/student", response={200:SuccessFoundSchmea, 404:NotFoundSchema})
def zhuce_student(request, item:Form[LoginStuedntSchema]):
    if item.password == item.password_verify:
        Student.objects.create(
             Student_name=item.Student_name,
             Student_id=item.Student_id,
             password=item.password
        )
        return {"message": "学生创建成功。"}
    else:
        return {"message": "学生创建失败。"}



#老师注册
@api.post("/zhuce/teacher", response={200:SuccessFoundSchmea, 404:NotFoundSchema})
def zhuce_teacher(request, item:Form[LoginTeacherSchema]):
    if item.password == item.password_verify:
        Teacher.objects.create(
             Teacher_name=item.Teacher_name,
             Teacher_id=item.Teacher_id,
             password=item.password
        )
        return {"message": "老师创建成功。"}
    else:
        return {"message": "老师创建失败。"}




#选课
@api.post("/choose",response={200: List[ChooseSchema],404: List[NotFoundSchema]})
def choose(request, item:Form[Item]):
    try:
        Student_id = item.Student_id
        Lesson_id = item.Lesson_id
        Choose.objects.create(
            Student_id = Student_id,
            Lesson_id = Lesson_id,
            grade = 0
        )
        return Choose.objects.all()
    except Choose.DoesNotExist as e:
        return 404, {"message": "Choose does not exist"}

#查课
@api.get("/choose/{student_id}", response=List[ChooseSchema])
def query(request, student_id: int):
    try:
        choose = Choose.objects.filter(Student_id=student_id)
        return choose
    except Choose.DoesNotExist as e:
        return 404, {"message": "Choose does not exist"}










#查第二个数据库


#查询所有数据库
@api.get("/course", response=List[CourseSchema])
def course(request):
    return Course.objects.all()

@api.get("/design", response=List[DesignSchema])
def design(request):
    return Design.objects.all()

@api.get("/statistic",response=List[StatisticsSchema])
def statistic(request):

    return Statistics.objects.all()

@api.get("/homework",response=List[HomeworkSchema])
def homework(request):
    return Homeworka.objects.all()

@api.get("/resource",response=List[ResourceSchema])
def resource(request):
    return Resources.objects.all()

@api.get("/qa",response=List[QaSchema])
def qa(request):
    return Qa.objects.all()

@api.get("/announcement",response=List[AnnouncementSchema])
def announcemnt(request):
    return Announcement.objects.all()

@api.get("/catalog",response=List[CatalogSum])
def catalog(request):
    cats = Catalogs.objects.filter(label_intern_id=1)  # 假设这里获取的是数据库中所有相关的目录项

    if not cats:
        return []
    # 初始化章节的标题和子节列表
    catalog_sum = CatalogSum(label="", children=[])

    for index, cat in enumerate(cats):
        # 将第一条作为章节标题
        if index == 0:
            catalog_sum.label = cat.label_fellow.split(maxsplit=1)[1]
        else:
            # 为每个子项创建一个CatalogSchema实例并添加到children列表中
            child_label = cat.label_fellow.split(maxsplit=1)[1]
            catalog_sum.children.append(CatalogSchema(label=child_label))

    return [catalog_sum]

def catalog_id(id):
    cats = Catalogs.objects.filter(label_intern_id=id)  # 假设这里获取的是数据库中所有相关的目录项

    if not cats:
        return []
    # 初始化章节的标题和子节列表
    catalog_sum = CatalogSum(label="", children=[])

    for index, cat in enumerate(cats):
        # 将第一条作为章节标题
        if index == 0:
            catalog_sum.label = cat.label_fellow
        else:
            # 为每个子项创建一个CatalogSchema实例并添加到children列表中
            child_label = cat.label_fellow
            catalog_sum.children.append(CatalogSchema(label=child_label))

    return catalog_sum
















#查单个课程基本属性
@api.get("/course/{course_id}", response={200: List[CourseSchema], 404: NotFoundSchema})
def courses(request, course_id: int):
    try:
        course = Course.objects.get(pk=course_id)
        # 使用 Pydantic 的 .dict() 方法排除字段
        #course_data = CourseSchema.from_orm(course).dict(exclude={"Course_id"})
        return [course]
    except Course.DoesNotExist as e:
        return 404, {"message": "course does not exist"}




#查单个design基本属性
@api.get("/design/{design_id}", response={200: List[DesignSchema], 404: NotFoundSchema})
def designs(request, design_id: int):
    try:
        design = Design.objects.get(pk=design_id)
        # 使用 Pydantic 的 .dict() 方法排除字段
        design_data = DesignSchema.from_orm(design).dict(exclude={"design_id"})
        return [design_data]
    except Design.DoesNotExist as e:
        return 404, {"message": "design does not exist"}








#暂时查全部的
@api.get("/course-design/{course_design_id}", response=List[Course_DesignSchema])
def course_design(request, course_design_id: int):
    # 获取所有课程设计关联

    cd = Sum.objects.get(pk=course_design_id)
    #sbs = Sum.objects.all()


    results = []

    # 获取相应的课程和设计
    course = Course.objects.get(Course_id=cd.Course_id)
    design = Design.objects.get(Design_id=cd.Design_id)
    cas =Catalogs.objects.filter(label_id=cd.label_id)
    ans =Announcement.objects.filter(announcement_id=cd.announcement_id)
    qas = Qa.objects.filter(qa_id=cd.qa_id)
    res = Resources.objects.filter(resource_id=cd.resource_id)
    hos =Homeworka.objects.filter(Homework_id=cd.homework_id)
    statistic =Statistics.objects.get(Statistics_id=cd.Statistics_id)


    ca_list = []
    mmax=0
    mmin=1000
    for ca in cas:
        mmax=max(mmax,ca.label_intern_id)
        mmin=min(mmin,ca.label_intern_id)

    for i in range(mmin,mmax+1):
        ca_list.append(catalog_id(i))









    an_list = []
    for an in ans:
        an_list.append({
            "type": an.type,
            "content": an.content,
            "time": an.time,
        })

    qa_list = []  # Prepare a list to hold all Qa data
    for qa in qas:  # Iterate over the queryset
        qa_list.append({
            "question": qa.question,
            "answer": qa.answer,
            # Include other fields as needed
        })

    re_list = []
    for re in res:
        re_list.append({
            "id": re.resource_id,
            "type": re.type,
            "name": re.name,
            "time": re.time,
            "size": re.size,
            "url": re.url,
        })

    ho_list = []
    for ho in hos:
        ho_list.append({
            "type": ho.type,
            "name": ho.name,
            "start": ho.start,
            "end": ho.end,
            "id": ho.Homework_intern_id
        })


    result = {
        "id": course.Course_id,
        "name": course.name,
        "description": course.description,
        "illustration": course.illustration,
        "introduction": course.introduction,
        "image": course.image,
        "design": {
            "background": design.background,
            "target": design.target,
            "principle": design.principle
        },
        "catalog": ca_list,

        "announcement": an_list,
        "qa": qa_list,
        "resources": re_list,
        "homework":ho_list,

        "statistics":{
            "student": statistic.student,
            "rate": statistic.rate,
            "total_rate": statistic.total_rate,
            "rate_num": statistic.rate_num,
            "qa": statistic.qa,
            "resources": statistic.resources,
            "homework": statistic.homework,
            "announcement": statistic.announcement,
            "chapter": statistic.chapter
        }

    }
    results.append(result)

    return results