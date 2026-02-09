import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from school.models import Student, Teacher

students = Student.objects.all()
teachers = Teacher.objects.all()

print(f"Total students: {students.count()}")
print(f"Total teachers: {teachers.count()}")

for s in students:
    print(f"\nStudent: {s.name}")
    teacher_list = list(s.teachers.all())
    print(f"  Teachers count: {len(teacher_list)}")
    for t in teacher_list:
        print(f"  - {t.name}: {t.subject}")
