import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CryptoService {

  private baseUrl = '/api/prices/'; // proxy will forward this to Django

  constructor(private http: HttpClient) { }

  getPrices(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}
