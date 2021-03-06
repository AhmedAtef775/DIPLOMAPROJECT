from django.db import models

from student.models import Student

class Option(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   timer = models.PositiveIntegerField(null=True, blank=True)# Wafi edits timer for examens
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    options = models.ManyToManyField(Option)
    # option1=models.CharField(max_length=200)
    # option2=models.CharField(max_length=200)
    # option3=models.CharField(max_length=200, null=True, blank=False)# Wafi edits add null, blank as true
    # option4=models.CharField(max_length=200, null=True, blank=False)# Wafi edits add null, blank as true
    image = models.ImageField(upload_to='Images/quiz', default= 'foo.jpg', null=True, blank=True)# Wafi edits add null, blank as true
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

    def __str__(self):
        return self.question
    
    

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marks}'
    


