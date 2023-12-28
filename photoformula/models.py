from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TimeField()
    duration = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty_level = models.CharField(max_length=100)
    lessons = models.ManyToManyField('Lesson', related_name='courses')
    category = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo', blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    materials = models.ManyToManyField('Material', related_name='lessons')

    def __str__(self):
        return self.name


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=255)
    experience = models.TextField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='photo', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Material(models.Model):
    material_type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='materials/')
    photo = models.ImageField(upload_to='photo', blank=True)

    def __str__(self):
        return self.title