import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { FirmsComponent } from './components/firms/firms.component';
import { InvoiceComponent } from './components/invoice/invoice.component';

const routes: Routes = [{
  path: '',
  component: FirmsComponent,
}, {
  path: 'firms',
  children: [
    { path: '', component: FirmsComponent },
    {
      path: ':id/invoices',
      component: InvoiceComponent
    }]
}];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
