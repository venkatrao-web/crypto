import { Component, OnInit } from '@angular/core';
import { CryptoService } from './crypto.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  cryptoPrices: any = {};

  constructor(private cryptoService: CryptoService) {}

  ngOnInit() {
    this.cryptoService.getPrices().subscribe({
      next: (data) => this.cryptoPrices = data,
      error: (err) => console.error('Error fetching crypto prices:', err)
    });
  }
}
