import { NgxSpinnerService } from 'ngx-spinner';
import { forkJoin } from 'rxjs';

import { Component } from '@angular/core';

import { PageService } from './services/page-service/page.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'smartbookkeeper-frontend';

  constructor(public pageService: PageService, public spinner: NgxSpinnerService) { }

  ngOnInit(): void {
    this.pageService.isLoadingDataSubject.next(true);
    this.spinner.show();

    forkJoin([
      this.pageService.getFirmsList(),
      this.pageService.getVendorsList(),
      this.pageService.getSessionsList(),
      this.pageService.getProductsList(),
      this.pageService.getInvoicesList(),
    ]).subscribe({
      complete: () => {
        this.pageService.isLoadingDataSubject.next(false);
        this.spinner.hide();
      }
    });
  }
}
