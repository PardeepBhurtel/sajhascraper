import scrapy

class PostSpider(scrapy.Spider):
    name = "sajhalinks"
    
    start_urls = [
        'https://sajha.com/sajha/html/index.cfm#_'
        
    ]
    
    def parse(self, response):
        self.logger.info('Hi, this is a Job page! %s', response.url)
        post={}
        post['links'] = response.css('a::text').getall()
        
        return post
        # for post in response.css('div.'):
        #     yield{
        #         'links':response.css('a::text').getall()
                
        #         }
       