from django.db import models
from django.db.models import Avg

from profiles.models import TeamMember
from projects.models import Project

class Feedback(models.Model):
    RATING_CHOICES = zip(range(6), range(6)) # 0 - 5 scale of rating

    maker = models.ForeignKey(TeamMember, related_name='feedbacks_made')
    target = models.ForeignKey(TeamMember, related_name='feedbacks')
    project = models.ForeignKey(Project, related_name="feedbacks")
    participation_rating = models.IntegerField(choices=RATING_CHOICES)
    participation_rationale = models.TextField()
    contribution_rating = models.IntegerField(choices=RATING_CHOICES)
    contribution_rationale = models.TextField()
    communication_rating = models.IntegerField(choices=RATING_CHOICES)
    communication_rationale = models.TextField()
    ease_of_working_together_rating = models.IntegerField(choices=RATING_CHOICES)
    ease_of_working_together_rationale = models.TextField()
