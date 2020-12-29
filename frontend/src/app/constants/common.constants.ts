export interface ServerResponse {
  data: ServerResponseData[],
  included?: ServerResponseData[]
  links?: {
    first: string,
    last: string,
    next: string,
    prev: string
  },
  meta?: {
    pagination: {
      page: number,
      pages: number,
      count: number
    }
  }
}

export interface ServerResponseData {
  id: number,
  attributes: any,
  type: string
  relationships?: any,
}