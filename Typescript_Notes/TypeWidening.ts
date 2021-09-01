type Options = {
    baseURL: string
    cacheSize?: number
    tier?: 'prod' | 'dev'
  }
  
  class API {
    constructor(private options: Options) {}
  }
  
  new API({
    baseURL: 'https://api.mysite.com',
    tier: 'prod'
  })