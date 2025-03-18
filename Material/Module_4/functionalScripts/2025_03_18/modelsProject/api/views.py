from rest_framework.response import Response
from modelTrial.models import Firstname
from .serializers import FirstnameSerializer
from rest_framework.decorators import api_view

# @api_view (['GET'])
# def getData (request):
#     person = {
#         'firstname' : 'Clark Kent'
#     }
#     return Response (person)

@api_view (['GET'])
def getData (request):
    firstnames = Firstname.objects.all ()
    serializer = FirstnameSerializer (firstnames, many=True)
    return Response (serializer.data)

@api_view (['POST'])
def postData (request):
    serializer = FirstnameSerializer (data=request.data)
    if serializer.is_valid ():
        serializer.save ()
    return Response (serializer.data)

# @api_view (['POST'])
# def postData (request):
#     firstname = request.data ['firstname']
#     output = {
#         'output' : firstname
#     }
#     return Response (output)