import { Component, OnInit } from '@angular/core';

import { PageService } from '../../services/page-service/page.service';

@Component({
  selector: 'app-firms',
  templateUrl: './firms.component.html',
  styleUrls: ['./firms.component.scss']
})
export class FirmsComponent implements OnInit {
  attributesToShow = {
    "firmDetailsSection1": {
      "sectionName": "Company Details",
      "attributes": {
        "Contact Name": "contact_name",
        "GSTIN": "gstin",
      }
    }
    ,
    "firmDetailsSection2": {
      "sectionName": "Company Contact Number", "attributes": {
        "Phone Number": "phone_number",
        "Email": "email",
      }
    },
    "firmDetailsSection3": {
      "sectionName": "Company Registered Address", "attributes": {
        "Address Line 1": "address_line_1",
        "Address Line 2": "address_line_2",
        "City": "city",
        "State": "state",
        "Zipcode": "zipcode",
      }
    },
    "firmDetailsSection4": {
      "sectionName": "Company Bank Details", "attributes": {
        "Bank Account Number": "bank_account_number",
        "Bank Account Name": "bank_account_name",
        "Bank Name": "bank_name",
        "Bank Branch Name": "bank_branch_name",
        "Bank IFS Code": "bank_ifs_code",
      }
    }
  };

  constructor(public pageService: PageService) { }

  ngOnInit(): void {
    console.log("attributesToShow = ", this.attributesToShow);
  }
}
