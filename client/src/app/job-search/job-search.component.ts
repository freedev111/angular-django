import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { SearchService } from '../service/search.service';

@Component({
  selector: 'app-job-search',
  templateUrl: './job-search.component.html',
  styleUrls: ['./job-search.component.scss', '../app.component.scss'],
})
export class JobSearchComponent implements OnInit {
  form: FormGroup;
  public postInvalid: boolean;

  constructor(
    private searchService: SearchService,
    private fb: FormBuilder,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.form = this.fb.group({
      title: ['', Validators.required],
      location: ['', Validators.required],
    });
  }

  async onSubmit() {
    this.postInvalid = false;
    if (this.form.valid) {
      try {
        const title = this.form.get('title').value;
        const location = this.form.get('location').value;

        this.searchService.searchJob(title, location).subscribe(() => {
          this.router.navigate(['/jobs']);
        });
      } catch (err) {
        this.postInvalid = true;
      }
    }
  }
}
