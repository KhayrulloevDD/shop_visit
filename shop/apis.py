from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from . models import Employee, TradePoint, Attendance, User
from . serializers import EmployeeSerializer, TradePointSerializer, AttendanceSerializer


@api_view(['GET'])
def get_all_trade_points(request):
    phone_number = request.query_params.get("phone_number")
    trade_points = TradePoint.objects.filter(employee__phone=phone_number)
    serializer = TradePointSerializer(trade_points, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def attend_trade_point(request):
    phone_number = request.query_params.get("phone_number")
    trade_point = TradePoint.objects.select_related('employee').get(id=request.data['trade_point'])
    employee_serializer = EmployeeSerializer(trade_point.employee)
    attached_phone_number_to_tp = employee_serializer.data['phone']

    if phone_number != attached_phone_number_to_tp:
        return Response({
            "status": "error",
            "message": "Переданный номер телефона Работника НЕ привязан к указанной ТТ"
        }, status=status.HTTP_400_BAD_REQUEST)
    attendance_serializer = AttendanceSerializer(data=request.data)
    if attendance_serializer.is_valid():
        attendance_serializer.save()
        return Response({
            "id": attendance_serializer.data['id'],
            "date": attendance_serializer.data['date'],
        }, status=status.HTTP_201_CREATED)
    return Response(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

