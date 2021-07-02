from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import *
from main.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser, FormParser
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# @csrf_exempt
@api_view(['POST',])
# @parser_classes([FormParser])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Account registered successfully."
            data['email'] = account.email
            data['username'] = account.username
            data['Token'] = Token.objects.get(user = account).key
        else:
            data = serializer.errors
        return Response(data)


#
# @csrf_exempt
# @api_view(['POST'])
# @parser_classes([JSONParser])
# def login(request, format=None):
#     # if request.method == 'POST':
#     data = request.query_params
#     print(data)
#     user = authenticate(request, username=data['username'], password=data['password'])
#     if user is None:
#         return JsonResponse({'Error':'Failed to login, please check username and password!'}, status=400)
#     else:
#         try:
#             token = Token.objects.get(user=user)
#         except:
#             token = Token.objects.create(user=user)
#         return JsonResponse({'token':str(token)}, status=201)

@permission_classes([])
@authentication_classes([])
class FacilitiesList(generics.ListAPIView):
    queryset = Facility.objects.all().order_by('-id')
    serializer_class = FacilitySerializer
    # permission_class = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user

    # def perform_create(self, serializer):
    #     serializer.save(use=self.request.user)


# class FacilityCreate(generics.ListCreateAPIView):
#     queryset = Facility.objects.all().order_by('-id')
#     serializer_class = FacilitySerializer
#     # permission_classes = [permissions.IsAuthenticated]
#
#     # def get_queryset(self):
#     #     user = self.request.user
#     #     return Facility.objects.filter(user=user, code__isnull=False)
#
# class FacilityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Facility.objects.all().order_by('-id')
#     serializer_class = FacilitySerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#

# class FacilityComplete(generics.UpdateAPIView):
#     queryset = Facility.objects.all().order_by('-id')
#     serializer_class = FacilityCompleteSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.instance.name = "Facility changed name"
#         serializer.save()


@api_view(['POST', ])
@authentication_classes([])
@permission_classes([])
def FacilityCreateView(request):
    # Do this when you are saving the user object referenced in Facility table
    # user = User.objects.get(pk=1)
    # Facility = Facility(user = user)

    if request.method == "POST":
        serializer = FacilitySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@authentication_classes([])
@permission_classes([])
def FacilityDetailView(request, pk):
    facility_object =  Facility.objects.all()[0]
    facility = Facility.objects.get(id = facility_object.id)

    if not facility:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacilitySerializer(Facility)
        return Response(serializer.data)


@api_view(['PUT', ])
@authentication_classes([])
@permission_classes([])
def FacilityUpdateView(request, pk):
    try:
        Facility = Facility.objects.get(id = pk)
    except Facility.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = FacilitySerializer(Facility, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Facility Updated Successfully"
            return Response(data = data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_404_BAD_REQUEST)


@api_view(['DELETE', ])
@authentication_classes([])
@permission_classes([])
def FacilityDeleteView(request, pk):
    try:
        Facility = Facility.objects.get(id = pk)
    except Facility.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = Facility.delete()
        data = {}
        if operation:
            data["success"] = "Facility Deleted Successfully"
        else:
            data["failure"] = "Facility couldn't be deleted"
        return Response(data = data)
    return Response(status = status.HTTP_400_BAD_REQUEST)
