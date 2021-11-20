from django.db import models

class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    refresh_token = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150)
    expires_in = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    token_type = models.CharField(max_length=50)
