from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


from .models import Employee
from .serializers import GetEmployeeSerializer,  PostEmployeeSerializer

# Create your views here.
class GetEmployeesView(APIView):

     permission_classes = []

     def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = GetEmployeeSerializer
        if serializer.is_valid:
            data = serializer(employees, many=True).data
            return Response(
                data=sorted(data, key=lambda d: d['reg_number'], reverse=False),
                status=200
            )
        return Response(serializer.errors, status=400)
        


class GetEmployeeView(APIView):

    permission_classes = []

    def get(self, request, pk, format=None):
        employee = Employee.objects.get(id=pk)
        serializer = GetEmployeeSerializer
        if serializer.is_valid:
            data = serializer(employee, many=False).data
            if data:
                return Response(data, status=200)
        return Response(serializer.errors, status=400)



class PostEmployeeView(APIView):

     permission_classes = []

     def post(self, request, format=None):
        serializer = PostEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=dict(
                    status='success',
                    message='Employee is successfully created.'
                ),
                status=200)
        return Response(data=dict(status='error', message=serializer.errors), status=400)



class UpdateEmployeeView(APIView):

     permission_classes = []

     def put(self, request, pk, *args, **kwargs):
        # user = request.user
        comment = Employee.objects.get(pk=pk)
        data = request.data
        serializer = PostEmployeeSerializer
        serializer = serializer(instance=comment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            # if user == comment.author:
            serializer.save()
            return Response(
                data=dict(
                    status="success",
                    message=f"Employee {pk} is successfully updated!"
                ),
                status=200)
            # return Response(
            #     data=dict(
            #         status="Fail",
            #         message="You are not authorised to update the comment."
            #     ),
            #     status=400)
        return Response(
            data=dict(
                status="Failed",
                message=f"Employee {pk} is not successfully updated!"
            ),
            status=400)





class DeleteEmployeeView(APIView):

     permission_classes = []

     def delete(self, request, pk, *args, **kwargs):
        # user = request.user
        comment = Employee.objects.get(pk=pk)
        # if user == comment.author:
        comment.delete()
        return Response(
            data=dict(
                status="success",
                message=f"Employee {pk} is successfully deleted!"
            ),
            status=200)
        # return Response(
        #     data=dict(
        #         status="Fail",
        #         message="Youa are not authorised to delete comment."
        #     ),
        #     status=400)