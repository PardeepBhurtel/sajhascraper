import scrapy

class PostSpider(scrapy.Spider):
    name = "sajha"
    
    start_urls = [
        'https://sajhalist.com/view.cfm?listingid=1C3B4DED-E536-B57D-5CD0-0BDABAAF0F53',
        'https://sajhalist.com/view.cfm?listingid=776DD8DF-E704-D4ED-AB96-C636ADC02A0D',
        'https://sajhalist.com/view.cfm?listingid=EB919705-F425-C3B8-AF30-F9D78211D12D',
        'https://sajhalist.com/view.cfm?listingid=627E25CD-90D7-6029-885E-68467D830AA8',
        'https://sajhalist.com/view.cfm?listingid=CD236F2F-DB73-CE85-AF0B-A65B743C9C81',
        'https://sajhalist.com/view.cfm?listingid=E59CEC75-9E2A-1EA5-7413-696001D331CA',
        'https://sajhalist.com/view.cfm?listingid=3E8EF1C9-9CFF-9F89-916B-6FC853EA8990',
        'https://sajhalist.com/view.cfm?listingid=E59CEC75-9E2A-1EA5-7413-696001D331CA',
        'https://sajhalist.com/view.cfm?listingid=E5747AF7-F89F-F545-DDD4-36CC56A53740',
        'https://sajhalist.com/view.cfm?listingid=77D19DAF-940F-4E16-8EEE-9123EC836761',
        'https://sajhalist.com/view.cfm?listingid=DCE0C6FC-EA2E-B2DB-1CF2-8F26CA068299',
        
        
        # https://sajhalist.com/view.cfm?listingid=776DD8DF-E704-D4ED-AB96-C636ADC02A0D,
        # 'https://sajha.com/sajha/html/index.cfm#_'
        
    ]
    
    def parse(self, response):
        # items = {
        #     'job_desp':response.css('div::text').extract()
        # }
        
        for post in response.css('div.art-postcontent'):
            # post = [i.replace("\t", "").replace("\n", "") for i in post]
            # for quote in response.css('div::text'):
            # quote  = response.css('div::text')
            # quote = [i.replace("\t", "").replace("\n", "") for i in quote]
            yield{
                'job_desp':''.join(s.strip()  for s in response.css('div::text').getall())
                }
            # text = list(map(str.strip, job))
            # print(text)
            
        next_page = response.css('a.megamenu_drop::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)           
        # for list in response.css('div.art-postcontent'):
        #     job_desp = response.css('div::text').getall()
        #     return job_desp
            # var = list.text
            # data_list.append(var.replace("\n,\r",""))
            
    
        
        
       
        
        