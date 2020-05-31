from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import (
  HTTP_400_BAD_REQUEST,
  HTTP_500_INTERNAL_SERVER_ERROR,
  HTTP_200_OK,
  HTTP_201_CREATED,
)
from .serializers import JobSerializer
from .models import Job
from .utils import (
  get_matched_job,
  create_serializer_data,
)
import requests

# Create your views here.
class JobPostView(CreateAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer

  def post(self, request, *args, **kwargs):
    # Validate request data
    if 'title' not in request.data:
      return Response('Invalid Request Data', status=HTTP_400_BAD_REQUEST)

    # Check if the jobs are already existed
    title = request.data['title']
    jobs = Job.objects.filter(title=title)
    
    if len(jobs) > 0:
      return Response(JobSerializer(jobs[0]).data, status=HTTP_201_CREATED)

    # Fetch the request data from Open Skills
    response = requests.get('http://api.dataatwork.org/v1/jobs/autocomplete?begins_with={}'.format(title))

    if response.status_code != 200:
      return Response('API Request Error', status=HTTP_500_INTERNAL_SERVER_ERROR)

    job_data = response.json()
    
    if len(job_data) == 0:
      return Response('Not Found', status=HTTP_200_OK)
    
    # Save Jobs to database
    matched_job = get_matched_job(job_data)
    serializer_data = create_serializer_data(request.data, matched_job) 
    serializer = self.get_serializer(data=serializer_data)
    serializer.is_valid(raise_exception=True)
    job = serializer.save()

    # Make Response data
    headers = self.get_success_headers(serializer.data)
    response_data = {
      'job': serializer.data,
    }

    return Response(response_data, status=HTTP_201_CREATED, headers=headers)

class JobListView(ListAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer

class PositionListView(ListAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer

  def list(self, request, id):
    job = Job.objects.filter(title_id=id)

    if len(job) == 0:
      return Resonse('Invalid Request Data', status=HTTP_400_BAD_REQUEST)

    title = job[0].title
    location = job[0].location
    response = requests.get('https://jobs.github.com/positions.json?description={}&location={}'.format(title, location))

    return Response(response)
