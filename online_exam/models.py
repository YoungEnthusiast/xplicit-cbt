# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
import pytz
from django.db import models

class user(models.Model):
    first_name = models.CharField(default = "", max_length = 100)
    last_name = models.CharField(default = "", max_length = 100)
    phone = models.CharField(default = "", max_length =15)
    email = models.CharField(default = "", max_length =100)
    password = models.CharField(default = "", max_length=100)
    account_type = models.IntegerField(default = 1)
    status = models.IntegerField(default = 1)
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.id) + " | " + str(self.first_name) + " " + str(self.last_name) + " | " + str(self.email)

class course(models.Model):
    course_name = models.CharField(default = "", max_length=100)
    description = models.TextField(null="True", blank=True)
    faculty = models.CharField(default = "", max_length=100)
    # faculty = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default = 1)
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return str(self.course_name) + " | " + str(self.faculty)

class exam_detail(models.Model):
    exam_name = models.CharField(default = "", max_length = 100)
    description = models.TextField(null="True", blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    no_of_questions = models.IntegerField()
    attempts_allowed = models.IntegerField()
    pass_percentage = models.IntegerField()
    course_id = models.ForeignKey(course, on_delete = models.CASCADE)
    year = models.IntegerField()
    status = models.IntegerField(default = 1)
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.id) + "; " + str(self.exam_name) + "; " + str(self.description) + "; " + str(self.start_time) + "; " + str(self.end_time) + "; " + str(self.no_of_questions) + "; " + str(self.attempts_allowed) + "; " + str(self.pass_percentage) + "; " + str(self.course_id) + "; " + str(self.year) + "; " + str(self.status) + "; " + str(self.created) + "; " + str(self.modified)

class question_type(models.Model):
    q_type = models.CharField(default = "", max_length = 100)
    def __str__(self):
        return str(self.id) + "; " + str(self.q_type)

class question_bank(models.Model):
    question = models.TextField(null="True", blank=True)
    description = models.TextField(null="True", blank=True)
    question_type = models.ForeignKey(question_type, on_delete = models.CASCADE)
    exam_id = models.ForeignKey(exam_detail, on_delete =models.CASCADE)
    score = models.FloatField()
    status = models.IntegerField(default = 1)
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Question Bank'
        verbose_name_plural = 'Question Banks'

    def __str__(self):
        return str(self.question)

class registration(models.Model):
    user_id = models.ForeignKey(user, on_delete = models.CASCADE)
    exam_id = models.ForeignKey(exam_detail, on_delete = models.CASCADE)
    attempt_no = models.IntegerField()
    registered = models.IntegerField(default = 0)
    view_answers  = models.IntegerField(default = 0)
    answered = models.IntegerField(default = 0)
    registered_time = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.id) + "; " + str(self.user_id) + "; " + str(self.exam_id) + "; " + str(self.attempt_no) + "; " + str(self.registered) + "; " + str(self.view_answers) + "; " + str(self.answered) + "; " + str(self.registered_time)

class result(models.Model):
    registration_id = models.ForeignKey(registration, on_delete = models.CASCADE)
    question_id = models.ForeignKey(question_bank, on_delete = models.CASCADE)
    answer = models.TextField(null="True", blank=True)
    score = models.FloatField()
    verify = models.IntegerField(default = 0)
    def __str__(self):
        return str(self.id) + "; " + str(self.registration_id) + "; " + str(self.question_id) + "; " + str(self.answer) + "; " + str(self.score) + "; " + str(self.verify)

class option(models.Model):
    question_id = models.ForeignKey(question_bank, on_delete=models.CASCADE)
    option_no = models.IntegerField()
    option_value = models.TextField(null="True", blank=True)
    def __str__(self):
        return str(self.id) + "; " + str(self.question_id) + "; " + str(self.option_no) + "; " + str(self.option_value)

class answer(models.Model):
    question_id = models.ForeignKey(question_bank, on_delete=models.CASCADE)
    answer = models.TextField(null="True", blank=True)
    def __str__(self):
        return str(self.id) + "; " + str(self.question_id) + "; " + str(self.answer)

class MatchTheColumns(models.Model):
    question_id = models.ForeignKey(question_bank, on_delete=models.CASCADE)
    question = models.TextField(null="True", blank=True)
    answer = models.TextField(null="True", blank=True)
    def __str__(self):
        return str(self.id) + "; " + str(self.question_id) + "; " + str(self.question) + "; " + str(self.answer)
