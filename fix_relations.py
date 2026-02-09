import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from school.models import Student, Teacher

teachers = list(Teacher.objects.all())
print(f'Teachers: {len(teachers)}')

for s in Student.objects.all():
    s.teachers.clear()
    for t in teachers:
        s.teachers.add(t)
    print(f'{s.name}: {s.teachers.count()} teachers')
