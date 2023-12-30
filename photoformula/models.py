from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    is_anchor = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty_level = models.CharField(max_length=50)
    lessons = models.ManyToManyField('Lesson', related_name='courses')
    category = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        if self.is_anchor:
            return reversed('main:home') + f'#{self.slug}'
        return self.slug

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Course"
        ordering = ('name', 'price')


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    materials = models.ManyToManyField('Material', related_name='lessons')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=255)
    experience = models.TextField()
    bio = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super(Instructor, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Material(models.Model):
    material_type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='materials/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Material, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    photo = models.ImageField(upload_to='photo/')
    name = models.CharField(max_length=255, blank=True)



