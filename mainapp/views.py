from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()
