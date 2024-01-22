from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
# import uuid

# Create your models here.

# new_uuid = uuid.uuid4()

#Strands:
ABM = 'ABM'
GAS = 'GAS'
HUMSS = 'HUMSS'
STEM = 'STEM'
TVL = 'TVL'


STRAND = (
    (ABM, "Accountancy Business Management"),
    (GAS, "General Academics Strand"),
    (HUMSS, "Humanities and Social Sciences"),
    (STEM, "Science Technology Engineering and Mathematics"),
    (TVL, "Technical Vocational Livelihood"),

)

#Grade Level:

grade_11 = '11'
grade_12 = '12'

grade_level = (
    (grade_11, 'Grade 11'),
    (grade_12, 'Grade 12')
)

#School Year:
SCHOOL_YEAR_CHOICES = [
    ('2023-24', '2023-24'),
    ('2024-25', '2024-25'),
    ('2025-26', '2025-26'),
    ('2026-27', '2026-27'),
]


class Student(models.Model):
    school_year = models.CharField(max_length=50, choices=SCHOOL_YEAR_CHOICES, default='2023-24')
    studentNumber = models.CharField(max_length=50, unique=True, editable=False)
    LRN = models.PositiveIntegerField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    addrs = models.CharField(max_length=100)
    strand = models.CharField(max_length=20, choices=STRAND)
    gradeLevel = models.CharField(max_length=50, choices=grade_level)
    section = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{1,3}$')])
    picture = models.ImageField()

    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.studentNumber:
            current_year = str(self.created_at.year) if self.created_at else str(timezone.now().year)
            student_count = Student.objects.filter(created_at__year=current_year).count() + 1
            self.studentNumber = f"{current_year}{student_count:03d}"

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Student: {self.firstName} {self.lastName}"
    
class Coaches(models.Model):

    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=10, blank=True)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    addrs = models.CharField(max_length=50)
    cpNum = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')], blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Coach: {self.firstName} {self.lastName}"


