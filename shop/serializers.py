from rest_framework import serializers
from . models import Employee, TradePoint, Attendance


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'phone']


class TradePointSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradePoint
        fields = ['id', 'name', 'employee']


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['id', 'trade_point', 'date', 'latitude', 'longitude']

