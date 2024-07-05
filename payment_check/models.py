from django.db import models


# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    token_num = models.IntegerField()
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=100, default="student")
    service_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2)
    # payment_status either pending or paid
    payment_status = models.CharField(max_length=10)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Payment for token num {self.token_num} by student id {self.student_id} on {self.service_date}"

    class Meta:
        db_table = "payment"
        managed = True
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
