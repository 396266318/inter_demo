import json
import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from project_app.models import Project
from module_app.models import Module
from testcase_app.models import TestCase
from testtask_app.models import TestTask, TestResult
from  test_platform import settings
from testtask_app.extend.task_thread import TaskThread
# Create your views here.
