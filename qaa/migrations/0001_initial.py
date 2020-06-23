# Generated by Django 3.0.5 on 2020-04-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=50)),
                ('question_answer', models.CharField(max_length=50)),
                ('human_answer', models.CharField(blank=True, default=None, max_length=50)),
            ],
        ),
    ]