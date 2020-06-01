import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Job } from '../model/job';

@Injectable({
  providedIn: 'root',
})
export class JobService {
  private jobURL: string = 'http://localhost:8000/api/jobs/';
  constructor(private http: HttpClient) {}

  getJobs(): Observable<Job[]> {
    return this.http.get<Job[]>(this.jobURL);
  }
}
