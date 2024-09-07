
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from Authentication.models import User
from API.models import Project

class Solution(models.Model):
    
    class State(models.IntegerChoices):
        STARTED = 1, 'pending'
        IN_PROCESS = 2, 'approved'
        COMPLETED = 3, 'rejected'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    state = models.PositiveSmallIntegerField('State', choices=State.choices, default=State.STARTED)
    title = models.CharField('Solution Title', max_length=500)
    description = models.TextField('Solution Description')
    file = models.FileField(upload_to='solutions/', null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    token = models.CharField('Token Payment', max_length=200,)
    proposed_tokens = models.FloatField('Proposed Tokens', default=100)
    hash_id = models.TextField('Hash', none=True, default=None)
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('solution')
        verbose_name_plural = _('Solutions')