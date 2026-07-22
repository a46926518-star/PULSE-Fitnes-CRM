from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username') or request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({"message": "Muvaffaqiyatli kirdingiz!", "username": user.username}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Login yoki parol xato!"}, status=status.HTTP_400_BAD_REQUEST)