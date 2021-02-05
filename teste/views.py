from django.shortcuts import render
from django.db.models import Count, Sum, F, Avg, Value as V
from django.db.models.functions import TruncMonth, Coalesce
from dateutil.relativedelta import relativedelta

from datetime import timedelta, date, datetime as dt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Teste(APIView):

    def get(self, request):

        res = {
            'a': 'qqq'
        }
        
        return Response(res)