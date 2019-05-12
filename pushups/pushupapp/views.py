from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def num_pushups(request):
    from collections import defaultdict
    pushups = defaultdict(list)
    with open('/Users/arajo/pushups/pushups/pushups/pushups.csv') as f:
        for line in f:
            time, num_pushups, country = line.strip().split(',')
            pushups[country].append(num_pushups)
    return Response(pushups)

# Create your views here.
