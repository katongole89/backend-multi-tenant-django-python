from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as alt_status


class SimpleTenancyApiView(APIView):
    def get(self, request, company_url):
    	if company_url == 'app':
    		data = {
    			'status': 'success',
    			'company_name': 'app company'
    		}
    	elif company_url == 'pilot':
    		data = {
    			'status': 'success',
    			'company_name': 'pilot company'
    		}
    	else:
    		data = {
    			'status': 'failed',
    			'company_name': 'No comapany'
    		}
    	return Response(data, status=alt_status.HTTP_200_OK)

