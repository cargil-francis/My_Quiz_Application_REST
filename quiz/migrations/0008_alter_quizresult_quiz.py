# Generated by Django 4.1.7 on 2023-02-25 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_quiz_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresult',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='quiz.quiz'),
        ),
    ]
