from django.db import models
from django.urls import reverse
# Create your models here.

class Usersinfo(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    Date = models.DateTimeField(auto_now_add=True)
    passuser= models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

class Solutions(models.Model):
    name = models.CharField(max_length=200)
    title=models.CharField(max_length=600)
    Description = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    etat= models.BooleanField()
    coulorfonvalue=models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('detail_solution', args=[str(self.id)])

class demandesolution(models.Model):
    datedemande = models.DateTimeField(auto_now_add=True)
    demandeur_id = models.ForeignKey(Usersinfo, on_delete=models.CASCADE,blank=True, null=True)
    solutiondemande_id = models.ForeignKey(Solutions, on_delete=models.CASCADE,blank=True, null=True)


class Message(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField()
        telephone = models.CharField(max_length=30)
        message = models.TextField(max_length=100)
        Datet = models.DateTimeField(auto_now_add=True)


