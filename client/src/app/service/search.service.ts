import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Job } from '../model/job';

@Injectable({
  providedIn: 'root',
})
export class SearchService {
  private searchURL: string = 'http://localhost:8000/api/job/';
  constructor(private http: HttpClient) {}

  searchJob(title: string, location: string) {
    return this.http.post<Job>(this.searchURL, { title, location });
  }
}
