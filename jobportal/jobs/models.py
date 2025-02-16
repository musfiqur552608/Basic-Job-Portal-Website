from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
