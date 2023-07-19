from django.db import models

class Suggestion(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    

class Vote(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE, related_name='votes')
    user_ip = models.GenericIPAddressField()
    is_upvote = models.BooleanField(default=True)


    def __str__(self):
        return self.suggestion