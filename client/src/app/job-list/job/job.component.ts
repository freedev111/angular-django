import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { Job } from '../../model/job';

@Component({
  selector: 'app-job',
  templateUrl: './job.component.html',
  styleUrls: ['./job.component.scss'],
})
export class JobComponent implements OnInit {
  @Input() job: Job;

  constructor(private router: Router) {}

  ngOnInit(): void {}

  handleClick(): void {
    this.router.navigate(['/positions'], {
      queryParams: {
        title_id: this.job.title_id,
        title: this.job.title,
      },
    });
  }
}
