import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { ApplicationComponent } from './application.component';
import { ApplicationHistoryComponent } from './history/history.component';

@NgModule({
  declarations: [
    ApplicationComponent,
    ApplicationHistoryComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterModule.forChild([
      {
        path: '',
        component: ApplicationComponent,
        children: [
          {
            path: 'history',
            component: ApplicationHistoryComponent
          }
        ]
      }
    ])
  ]
})
export class ApplicationModule { }