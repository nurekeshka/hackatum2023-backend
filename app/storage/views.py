from django.contrib.sites import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

from app.component.models import User, Issue
from app.security.models import Security
from django.core.serializers import serialize

import json

@api_view(['GET'])
def get_data_and_store(request):
    current_token_data = request.session.get('current_token_data', {})
    expected_value = current_token_data.split(':')
    # Extract the second part (index 1) and remove any surrounding whitespace and single quotes
    value = expected_value[1].strip().strip("'")
    security = Security.objects.get(value) #implement this later
    url = 'https://miras.youtrack.cloud/api/issues'
    yt_token='Bearer perm:cm9vdA==.NDgtMA==.TKJ7CvgnSsSAxxl0FB2eTHtlgaclrG'
    headers = {
        'Accept': 'application / json',
        'Authorization': yt_token,
        'Cache-Control': 'no-cache',
        'Access-Control-Allow-Origin': '*',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        data_converted = json.loads(data)
        ids = []
        for item in data_converted:
            ids.insert(item["id"])
            if not Issue.objects.filter(title=item['id']).exists():
                new_issue = Issue(title=item['id'])
                new_issue.save()
        ids.sort()
        serialized_data = serialize('json', Issue.objects.all())
        #return JsonResponse({'message': 'Data stored successfully'})
        return JsonResponse(json.loads(serialized_data), safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)
