# models.py

from django.db import models

class President(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='profile_images/president', null=True)
    details = models.CharField(max_length=1500, null=True)

    # Additional fields for ratings
    health_rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    education_rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    security_rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    infrastructure_rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])

    def calculate_total_ranking(self):
        # Calculate the total ranking based on individual ratings
        total_ranking = (
            self.health_rating +
            self.education_rating +
            self.security_rating +
            self.infrastructure_rating
        )
        return total_ranking

    def __str__(self):
        return self.name
