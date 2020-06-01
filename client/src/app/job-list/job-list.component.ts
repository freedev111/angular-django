import { Component, OnInit } from '@angular/core';
import { JobService } from '../service/job.service';
import { Job } from '../model/job';

@Component({
  selector: 'app-job-list',
  templateUrl: './job-list.component.html',
  styleUrls: ['./job-list.component.scss', '../app.component.scss'],
})
export class JobListComponent implements OnInit {
  jobs: Job[] = [];
  constructor(public jobService: JobService) {}

  ngOnInit(): void {
    this.getJobs();
  }

  getJobs(): void {
    this.jobService.getJobs().subscribe((jobs) => (this.jobs = jobs));
  }
}
