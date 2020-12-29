import { BehaviorSubject } from 'rxjs';
import { map } from 'rxjs/operators';

import { Injectable } from '@angular/core';

import { ServerResponse, ServerResponseData } from '../../constants/common.constants';
import { urls } from '../../constants/page.constants';
import { DataService } from '../data-service/data.service';

@Injectable({
  providedIn: 'root'
})
export class PageService {
  firmsData: ServerResponseData[];
  vendorsData: ServerResponseData[];
  sessionsData: ServerResponseData[];
  productsData: ServerResponseData[];
  invoicesData: ServerResponseData[];
  isLoadingDataSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

  constructor(public dataService: DataService) { }

  getFirmsList() {
    return this.dataService.getRequest(urls.getAllFirmsUrl()).pipe(map((response: ServerResponse) => {
      this.firmsData = response.data
    }));
  }

  getVendorsList() {
    return this.dataService.getRequest(urls.getAllVendorsUrl()).pipe(map((response: ServerResponse) => {
      this.vendorsData = response.data
    }));
  }

  getSessionsList() {
    return this.dataService.getRequest(urls.getAllSessionsUrl()).pipe(map((response: ServerResponse) => {
      this.sessionsData = response.data
    }));
  }

  getProductsList() {
    return this.dataService.getRequest(urls.getAllProductsUrl()).pipe(map((response: ServerResponse) => {
      this.productsData = response.data
    }));
  }

  getInvoicesList() {
    return this.dataService.getRequest(urls.getAllInvoicesUrl()).pipe(map((response: ServerResponse) => {
      this.invoicesData = response.data
    }));
  }
}
