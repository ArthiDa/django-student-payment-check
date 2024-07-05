# Generated by Django 5.0.6 on 2024-07-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_check', '0003_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('token_num', models.IntegerField()),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(default='student', max_length=100)),
                ('service_date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(max_length=10)),
                ('payment_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payment',
                'managed': True,
            },
        ),
    ]
