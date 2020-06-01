from django.test import TestCase
from .models import Job
from .serializers import JobSerializer
from .utils import (
  create_serializer_data,
  closeMatches,
  get_matched_job,
  get_jobs_from_openskills,
  get_positions_from_github,
)

# Create your tests here.
class JobTestCase(TestCase):
  def test_get_jobs_from_openskills(self):
    jobs = get_jobs_from_openskills('Software Engineer')
    self.assertEqual(len(jobs), 3)

  def test_close_matches(self):
    patterns = ['app', 'apple', 'peach', 'puppy']
    word = 'appel'
    closest_words = closeMatches(patterns, word)
    self.assertEqual(closest_words[0], 'apple')
    self.assertEqual(closest_words[1], 'app')

  def test_get_matched_job(self):
    title = 'Software Engineer'
    jobs = get_jobs_from_openskills(title)
    matched_job = get_matched_job(title, jobs)
    self.assertEqual(matched_job['suggestion'], 'Software Engineer')

  def test_create_serializer_data(self):
    request_data = {
      'title': 'Software Engineer',
      'location': 'New York'
    }
    matched_job = {
      "uuid": "14fa6e8b6cca66be98596c896d5a95fc",
      "suggestion": "Software Engineering Supervisor",
      "normalized_job_title": "software engineering supervisor",
      "parent_uuid": "adbc2046a7264152d61d23ecdc1606b3" 
    }
    serializer_data = create_serializer_data(request_data, matched_job)
    self.assertEqual(serializer_data['title'], 'Software Engineer')
    self.assertEqual(serializer_data['location'], 'New York')
    self.assertEqual(serializer_data['title_id'], '14fa6e8b6cca66be98596c896d5a95fc')
    self.assertEqual(serializer_data['normalized_title'], 'software engineering supervisor')

class PositionTestCase(TestCase):
  def test_get_positions(self):
    fields = ['id', 'type', 'url', 'created_at', 'company', 'company_url', 'location', 'title', 'description', 'how_to_appy', 'company_logo']
    positions = get_positions_from_github('Software Engineer', 'New York')
    self.assertEqual(len(positions), 7)

