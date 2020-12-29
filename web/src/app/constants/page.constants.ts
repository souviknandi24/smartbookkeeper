import { environment } from 'src/environments/environment';

export const apiUrl = environment.production ? 'http://nandidental.com' : 'http://localhost:8000';

export const clientUrl = environment.production ? 'http://nandidental.com' : 'http://127.0.0.1:4200';

export const urls = {
  getAllFirmsUrl: () => '/api/v1/firms/',
  getAllVendorsUrl: () => '/api/v1/vendors/',
  getAllSessionsUrl: () => '/api/v1/sessions/',
  getAllProductsUrl: () => '/api/v1/products/',
  getAllInvoicesUrl: () => '/api/v1/invoices/',
}