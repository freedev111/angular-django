import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Position } from '../model/position';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PositionService {
  private positionURL = 'http://localhost:8000/api/jobs/';
  constructor(private http: HttpClient) {}

  getPositions(jobId: string): Observable<Position[]> {
    console.log(jobId);
    return this.http.get<Position[]>(`${this.positionURL}${jobId}/positions/`);
  }
}
