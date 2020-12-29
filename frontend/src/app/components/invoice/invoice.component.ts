import * as moment from 'moment';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

import { ChangeDetectionStrategy, Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { ServerResponseData } from '../../constants/common.constants';
import { PageService } from '../../services/page-service/page.service';

@Component({
  selector: 'app-invoice',
  templateUrl: './invoice.component.html',
  styleUrls: ['./invoice.component.scss'],
})
export class InvoiceComponent implements OnInit, OnDestroy {
  selectedFirm: ServerResponseData = null;
  sessionWiseInvoicesList: { [key: string]: any[] } = {};
  selectedSessionName = null;
  sessionsList = [];
  private destroySubject$ = new Subject();

  constructor(public route: ActivatedRoute, public pageService: PageService) { }

  ngOnInit(): void {
    this.pageService.isLoadingDataSubject.pipe(takeUntil(this.destroySubject$)).subscribe((isLoading) => {
      if (!isLoading) {
        this.init();
      }
    });
  }

  ngOnDestroy(): void {
    this.destroySubject$.complete();
  }

  init(): void {
    this.route.params.pipe(takeUntil(this.destroySubject$)).subscribe(params => {
      this.selectedFirm = this.pageService.firmsData.find(firm => firm.id === params?.id);

      this.pageService.sessionsData.forEach(session => {
        this.sessionsList.push(session.attributes?.name);
        this.sessionWiseInvoicesList[session.attributes?.name] = this.pageService.invoicesData.filter((invoice) => invoice.relationships?.seller?.data?.id === this.selectedFirm.id && invoice.relationships?.session?.data?.id === session.id).map((invoice) => {

          return {
            invoice_number: `${invoice.attributes['invoice_number']}/${session.attributes?.name}`,
            invoice_date: moment("2020-06-11").format("DD MMM YYYY"),
            total_tax_amount: parseFloat(invoice.attributes['invoice_cgst_amount']) + parseFloat(invoice.attributes['invoice_igst_amount']) + parseFloat(invoice.attributes['invoice_sgst_amount']) + parseFloat(invoice.attributes['invoice_utgst_amount']),
            total_amount: parseFloat(invoice.attributes['invoice_amount']),
            buyer: this.pageService.vendorsData.find(vendor => vendor.id === invoice.relationships?.buyer?.data?.id),
            created_at: moment(invoice.attributes['created_at']).format("LLLL"),
            updated_at: moment(invoice.attributes['updated_at']).format("LLLL"),
          }
        });
      })

      this.sessionsList.reverse();
      this.selectedSessionName = this.sessionsList[0];
    });
  }

  onChangeSession(sessionName: string): void {
    this.selectedSessionName = sessionName;
  }
}
