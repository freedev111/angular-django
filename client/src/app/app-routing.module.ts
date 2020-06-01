import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { JobSearchComponent } from './job-search/job-search.component';
import { JobListComponent } from './job-list/job-list.component';
import { PositionListComponent } from './position-list/position-list.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'job',
  },
  {
    path: 'job',
    component: JobSearchComponent,
  },
  {
    path: 'jobs',
    component: JobListComponent,
  },
  {
    path: 'positions',
    component: PositionListComponent,
  },
  {
    path: '**',
    redirectTo: 'job',
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
