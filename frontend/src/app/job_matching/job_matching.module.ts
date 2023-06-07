import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { JobMatchingComponent } from './job_matching.component';

@NgModule({
  declarations: [JobMatchingComponent],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule.forChild([
      {
        path: '',
        component: JobMatchingComponent,
      },
    ]),
  ],
})
export class JobMatchingModule {}