from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer

@api_view(['GET', 'POST'])
def client_list_create(request):
    if request.method == 'GET':
        clients = Client.objects.all().order_by('-id')
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response({"message": "Mijoz topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    # 1. Bitta mijoz haqida ma'lumot olish
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    # 2. Mijoz ma'lumotlarini tahrirlash (PUT)
    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Mijozni o'chirish (DELETE)
    elif request.method == 'DELETE':
        client.delete()
        return Response({"message": "Mijoz muvaffaqiyatli o'chirildi"}, status=status.HTTP_204_NO_CONTENT)