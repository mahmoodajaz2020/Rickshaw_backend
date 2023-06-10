from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

class Incremental_values:
    id = 0

    def __init__(self, name):
        Incremental_values.id += 1
        self.empid = Incremental_values.id
    def increment(self):
        return self.empid

@api_view(['GET'])
def getData(request):
    if request.method == 'POST':
        person = "Welcome To My POST"
        return Response(person)
    elif request.method == 'GET':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        i = Incremental_values()
        id = i.increment()
        person = {'name' : body['name'], 'age' : body['age'], 'employee_id' : id}
        return JsonResponse(person)