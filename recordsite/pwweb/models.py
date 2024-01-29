from django.db import models

class WorkRecord(models.Model):
    class TicketStatus(models.TextChoices):
        Pending = 'Pending', 'Pending'
        Approved = 'Approved', 'Approved'
        Denied = 'Denied', 'Denied'
        Removed = 'Removed', 'Removed'
    
    TRUE_FALSE_CHOICES = [
        ('True', '是'),
        ('False', '否'),
    ]
    game_type = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    is_challenger_rank = models.CharField(
        max_length=5,
        choices=TRUE_FALSE_CHOICES,
        default='True')
    paid_amount = models.FloatField()
    commission_rate = models.FloatField(default=0.75)
    @property
    def commision_amount(self):
        return self.paid_amount * self.commission_rate
    date = models.DateTimeField("date published")
    status = models.CharField(
        max_length = 20,
        choices = TicketStatus.choices,
        default = TicketStatus.Pending
    )

    def __str__(self):
        return ".".join([str(self.id), self.game_type, self.customer_name, str(self.commision_amount), self.status])
