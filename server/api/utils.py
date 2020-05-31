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

def get_matched_job(job_data):
  return job_data[0]
