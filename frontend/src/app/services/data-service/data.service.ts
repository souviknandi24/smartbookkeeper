import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(public http: HttpClient) { }

  getRequest(urlPath: string) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' })
    return this.http.get(urlPath, { responseType: 'json', headers });
  }
}
