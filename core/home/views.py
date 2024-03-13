from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    # courses = {
    #         'course_name': 'Python',
    #         'instructor': 'John Doe',
    #         'coding': ['flask', 'Django', 'Tornado', 'FastApi'],
            
        # }
    if request.method == 'GET':
        # print(request.GET.get('search'))
        # print(f"Request Method: GET")
        # return Response(courses)
        json_response = {
            'course_name': 'Python',
            'instructor': 'John Doe',
            'coding': ['flask', 'Django', 'Tornado', 'FastApi'],
            
        }
    else:
        data = request.data
        print(data)
        json_response = {
            'course_name': 'Python',
            'instructor': 'John Doe',
            'coding': ['flask', 'Django', 'Tornado', 'FastApi'],
            
        }
    return Response(json_response)
        
    # elif request.method == 'POST':
    #     data = request.data
    #     print("*******")
    #     print(data)
    #     print("*******")
        
    #     print("This is a POST Request")
    #     print(f"name is {data['name']}")
    #     print(f"age is {data['age']}")
    #     return Response(courses)
    
    # elif request.method == 'PUT':
    #     print("This is a PUT     Request")
    #     return Response(courses)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH'])       
def people_create(request):
    if request.method == 'GET': 
       objs = Person.objects.all()
       serializer = PeopleSerializer(objs,  many=True)
       return Response(serializer.data)
    elif request.method == 'POST':  
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':  #Doesn't support partial UPDATION
        data= request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return  Response(serializer.errors)
    
    elif request.method == 'PATCH':  #Supports partial UPDATION
        data= request.data
        serializer = PeopleSerializer(data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return  Response(serializer.errors)