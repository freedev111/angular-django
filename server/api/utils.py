from difflib import get_close_matches
import requests

def create_serializer_data(request_data, job_data):
  response = dict()

  for prop in request_data:
    if prop in ['title', 'location']:
      response[prop] = request_data[prop]
  
  if 'uuid' in job_data:
    response['title_id'] = job_data['uuid']

  if 'normalized_job_title' in job_data:
    response['normalized_title'] = job_data['normalized_job_title']

  return response

def closeMatches(patterns, word):
  return get_close_matches(word, patterns)

def get_matched_job(title, job_data):
  job_title = []
  
  for job in job_data:
    job_title.append(job['suggestion'])
  
  matches = closeMatches(job_title, title)
  
  if len(matches) == 0:
    return job_data[0]
  
  index = job_title.index(matches[0])

  return job_data[index]

def get_jobs_from_openskills(title):
  response = requests.get('http://api.dataatwork.org/v1/jobs/autocomplete?begins_with={}'.format(title))

  if response.status_code != 200:
    return []

  return response.json()

def get_positions_from_github(title, location):
  response = requests.get('https://jobs.github.com/positions.json?description={}&location={}'.format(title, location))

  if response.status_code != 200:
    return []

  return response.json()
