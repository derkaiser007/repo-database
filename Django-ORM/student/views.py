from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q


def student_list(request):
    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html', {'posts':posts})


# Part 2
#################################################################

################
# Simple OR
################


# def student_list(request):
#     posts = Student.objects.filter(surname__startswith='Singh') | Student.objects.filter(surname__startswith='Mishra')

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html', {'posts':posts})



# def student_list(request):
#     posts = Student.objects.filter(Q(surname__startswith='Singh') | Q(surname__startswith='Shrivastav'))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html', {'posts':posts})



# def student_list(request):
#     posts = Student.objects.filter(Q(surname__startswith='Singh') | ~Q(surname__startswith='Shrivastav'))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html', {'posts':posts})


# Part 3
#################################################################

################
# Simple AND
################


# def student_list(request):
#     posts = Student.objects.filter(classroom=1) & Student.objects.filter(age=18)

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})



# def student_list(request):
#     posts = Student.objects.filter(Q(classroom=1) & Q(age=15))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html', {'posts':posts})



# def student_list(request):
#     posts = Student.objects.filter(Q(classroom=1) & ~Q(age=15))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html', {'posts':posts})

# Part 4
#################################################################

################
# Simple UNION
################

# def student_list(request):
#     # posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))
#     posts = Student.objects.all().values("firstname").union(Teacher.objects.all().values("firstname"))

#     print(posts)
#     print(connection.queries)

#     return render(request,'output.html', {'posts': posts})


# Part 5
#################################################################

################
# Simple EXCLUDE
################

# def student_list(request):
#     posts = Student.objects.exclude(age__gt=19)

#     # gt
#     # gte
#     # lt
#     # lte

#     print(posts)
#     print(connection.queries)

#     return render(request,'output.html', {'posts': posts})



# def student_list(request):
#     posts = Student.objects.filter(~Q(age__gt=20) & ~Q(surname__startswith='Shrivastav'))

#     print(posts)
#     print(connection.queries)

#     return render(request,'output.html',{'posts': posts})


# Part 6
#################################################################

################
# SELECT & OUTPUT INDIVIDUAL FILEDS
################

# def student_list(request):
#     posts = Student.objects.filter(classroom=1).only('firstname','age')

#     print(posts)
#     print(connection.queries)

#     return render(request,'output.html',{'posts': posts})


# Part 7
#################################################################

################
# Simple PERFORMING RAW QUERIES
################

# def student_list(request):

#     # posts = Student.objects.all()

#     # posts = Student.objects.raw("SELECT * FROM student_student")
#     # posts = Student.objects.raw("SELECT * FROM student_student WHERE age=15")

#     # sql = "SELECT * FROM student_student"
#     # posts = Student.objects.raw(sql)

#     # posts = Student.objects.raw("SELECT * FROM student_student")
#     # for s in posts:
#     #     print(s)

#     # sql = "SELECT * FROM student_student"
#     # posts = Student.objects.raw(sql)[:2]

#     print(posts)
#     print(connection.queries)

#     return render(request,'output.html', {'posts': posts})

# Deferred Model Instance


# Part 8
#################################################################

################
# Simple BYPASSING ORM
################

# def student_list(request):

#     # cursor = connection.cursor()
#     # cursor.execute("SELECT count(*) FROM student_student")
#     # r = cursor.fetchone()

#     # cursor = connection.cursor()
#     # cursor.execute("SELECT * FROM student_student")
#     # r = cursor.fetchall()

#     print(r)
#     print(connection.queries)

#     return render(request, 'output.html', {'posts':r})

# def dictfetchall(cursor):
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], row))
#         for row in cursor.fetchall()
#     ]

# def student_list(request):

#     # cursor = connection.cursor()
#     # cursor.execute("SELECT * FROM student_student")
#     # r = dictfetchall(cursor)

#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM student_student WHERE age > 20")
#     r = dictfetchall(cursor)

#     print(r)
#     print(connection.queries)

#     return render(request, 'output.html', {'posts':r})

# exact, iexact, contains, icontains, in, gt, gte, lt, lte, startswith, istartswith, endswith, iendswith, range, year, month, date, 
# week_day, isnull, search, regex, iregex 