from django.db import models


class About(models.Model):
    title = models.CharField(max_length=128, blank=True)
    description = models.TextField(max_length=9999, blank=True)

    class Meta:
        verbose_name = 'Hakkımızda Bilgisi'
        verbose_name_plural = 'Hakkımızda Bilgileri'

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=64, blank=True)
    description = models.TextField(max_length=999, blank=True)
    image = models.ImageField(upload_to='project-images/')

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=9999, blank=False)

    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'

        def __str__(self):
            return self.email