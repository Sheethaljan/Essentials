from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.course


class Details(models.Model):
    name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    # purpose = models.CharField(max_length=250)
    # materials = models.CharField(max_length=250)

    def __str__(self):
        return self.name

