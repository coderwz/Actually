from django.shortcuts import render, render_to_response
import builtins
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext

# 包装csrf请求， 避免django认为是跨站攻击脚本
from django.views.docorators.csrf import crsf_exempt

import random
from githubActually.models import User, Project, Milestone, Section, Task, Commit
from django.core.context_processors import csrf

# Create your views here.

def findById(request):
	b = Student.objects.get()