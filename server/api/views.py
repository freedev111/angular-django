from django.shortcuts import render
from django.http import JsonResponse
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
  get_jobs_from_openskills,
  get_positions_from_github,
)
import requests

# Create your views here.
class JobPostView(CreateAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer

  def post(self, request, *args, **kwargs):
    # Validate request data
    title = request.data['title']
    if not title:
      return Response('Invalid Request Data', status=HTTP_400_BAD_REQUEST)

    # Check search data is existed
    job = Job.objects.filter(title=title).first()
    
    if job:
      return Response('Search Record is Existed', status=HTTP_200_OK)

    # Fetch the request data from Open Skills
    job_data = get_jobs_from_openskills(title)
    
    if not job_data:
      return Response('Not Found', status=HTTP_200_OK)
    
    # Save best matched job to database
    matched_job = get_matched_job(title, job_data)
    serializer_data = create_serializer_data(request.data, matched_job)
    serializer = self.get_serializer(data=serializer_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response('Search Result Saved', status=HTTP_201_CREATED)

class JobListView(ListAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer

class PositionListView(ListAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer

  def list(self, request, id):
    job = Job.objects.filter(title_id=id).first()
    position_data = []

    # Get all available positions with title and location
    if job:
      position_data = get_positions_from_github(job.title, job.location)

    return JsonResponse(position_data, status=HTTP_200_OK, safe=False)
