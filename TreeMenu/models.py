from django.db import models

class TreeMenu(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
