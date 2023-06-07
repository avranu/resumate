import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthenticationModule } from './authentication/authentication.module';
import { ProfileModule } from './profile/profile.module';
import { JobMatchingModule } from './job_matching/job_matching.module';
import { ApplicationModule } from './application/application.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    AuthenticationModule,
    ProfileModule,
    JobMatchingModule,
    ApplicationModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }