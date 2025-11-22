from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    statut = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.titre

