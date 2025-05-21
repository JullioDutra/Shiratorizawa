from django.db import models

class Match(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200)
    opponent = models.CharField(max_length=100)
    tournament = models.CharField(max_length=100)
    opponent_logo = models.ImageField(upload_to='logos_oponentes/', null=True, blank=True)
    confirmed_fans = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} vs {self.opponent}"


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    height = models.PositiveIntegerField(help_text="Altura em cm")
    weight = models.PositiveIntegerField(help_text="Peso em kg")
    jersey_number = models.PositiveIntegerField()
    bio = models.TextField()
    tags = models.CharField(max_length=200)

    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",")]

    def __str__(self):
        return f"#{self.jersey_number} - {self.name}"

class Highlight(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    imagem = models.ImageField()
    image_url = models.URLField(null=True, blank=True)
    alt_text = models.CharField(max_length=200)

    def __str__(self):
        return self.alt_text

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email