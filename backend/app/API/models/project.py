
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from API.models import Company

class Project(models.Model):
    
    class State(models.IntegerChoices):
        STARTED = 1, 'started'
        IN_PROCESS = 2, 'in_process'
        COMPLETED = 3, 'completed'
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    state = models.PositiveSmallIntegerField('State', choices=State.choices, default=State.STARTED)
    title = models.CharField('project Title', max_length=500)
    description = models.TextField('Project Description', null=False)
    resume = models.FileField(upload_to='projects/', null=False)
    creation_date = models.DateTimeField(default=now)
    expiration_date = models.DateTimeField(default=now)
    token = models.CharField('Token', max_length=200,)
    tokens_limit = models.FloatField('Token Limit', default=100)
    hash_id = models.TextField('Hash', null=True, default=None)
    
    
    @property
    def state_name(self):
        return self.get_state_display()
    
    @property
    def _data(self) -> str:
        return str({
            'id': self.id,
            'company_id': self.company.id,
            'company': self.company.name,
            'title': self.title,
            'description': self.description,
            'creation_date': str(self.creation_date),
            'expiration_date': str(self.expiration_date),
            'state': self.state_name,
            'token': self.token,
            'tokens_limit': self.tokens_limit
        })
    
    
    class Meta:
        ordering = ('id',)
        verbose_name = _('project')
        verbose_name_plural = _('Projects')