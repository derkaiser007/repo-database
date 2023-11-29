# Generated by Django 4.2.7 on 2023-11-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_isbn_books_ptr'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookOrders',
            fields=[
            ],
            options={
                'ordering': ['created'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('student.bookcontent',),
        ),
    ]
