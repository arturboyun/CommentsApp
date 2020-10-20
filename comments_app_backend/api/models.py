from django.db import models


class Comment(models.Model):
    text = models.TextField('Text')
    reply_to = models.ForeignKey('self', models.CASCADE, null=True, blank=True, related_name='replies')
    username = models.CharField('User name', max_length=64)
    email = models.EmailField('E-mail')
    home_page = models.CharField('Home page', max_length=255, null=True, blank=True)
    ip = models.CharField('IP', max_length=32, null=True, blank=True)
    browser_info = models.CharField('Browser info', max_length=255, null=True, blank=True)
    modifed_at = models.DateTimeField("Modification Date", auto_now=True)
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)

    def __str__(self):
        return f"[{self.pk}] {self.username}: {self.text[:30]}"
