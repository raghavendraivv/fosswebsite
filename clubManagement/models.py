# -*- coding: utf-8 -*-
# created by Chirath R, chirath.02@gmail.com
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import date

from projects.models import Project
from registration.models import UserInfo


class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'pk': self.id})


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user.username + " - " + self.team.name


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="added_by")
    date = models.DateField()
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    attendance = models.BooleanField(default=False)

    def __str__(self):
        if self.attendance:
            return self.user.username + " " + str(self.date) + " - present"
        else:
            return self.user.username + " " + str(self.date) + " - absent"


class Responsibility(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name='created_by')
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('responsibility_detail', kwargs={'pk': self.pk})


class StudentResponsibility(models.Model):
    responsibility = models.ForeignKey(Responsibility, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class StatusUpdate(models.Model):
    """
    The status update for each data is stored as a string
    `user_id1 Y/N, user_id Y/N, .....`
    """
    date = models.DateField()
    value = models.CharField(max_length=1000)
    data = models.CharField(max_length=2000, blank=True)

    def get_value_dict(self):
        status_list = self.value.split(', ')
        status_dict = {}

        for status in status_list:
            user_id, status = status.split(' ')
            status_dict[int(user_id)] = status

        return status_dict

    def process_report(self):
        """
        saves a dict with key as the year and value as a list of user to the
        data field
        list-of-users = [[user, status]] where status is  a string with default
        value N
        :return:  {year, list[user, status]}
        """

        start_year = date.today().year

        if date.today().month < 8:
            start_year -= 1

        user_data = {}

        for year in range(start_year, start_year + 4, -1):
            user_info_list = UserInfo.objects.filter(year=year)
            user_list = []
            for user_info in user_info_list:
                if user_info.user.is_active:
                    user_list.append([user_info.user, 'N'])
            user_data[year] = user_list

        return user_data

    def get_report_with_year(self):
        """
        Returns a dict with key = year and value = list of [user, status_update]
        , where status update represents a string with value (Y/N)
        :return: dict of {year, list[user, status]}
        """
        pass

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('status_update_detail', kwargs={'pk': self.date})
