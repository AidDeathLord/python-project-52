from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext as _


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=150,
                             unique=True,
                             verbose_name=_('Имя'))
    description = models.CharField(max_length=500,
                                   verbose_name=_('Описание'))
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               verbose_name=_('Статус'))
    creator = models.ForeignKey(User,
                                on_delete=models.PROTECT,
                                verbose_name=_('Автор'),
                                related_name='Creator')
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 verbose_name=_('Исполнитель'),
                                 related_name='Executor',
                                 null=True,
                                 blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Дата создания'))
    labels = models.ManyToManyField(Label,
                                   verbose_name=_('Метки'),
                                   blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')
