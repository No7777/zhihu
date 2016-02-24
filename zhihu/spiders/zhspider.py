import scrapy

from zhihu.secret import USERNAME, PASSWORD

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    start_urls = ['https://www.zhihu.com/#signin']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                formdata={'account':USERNAME, 'password':PASSWORD},
                callback=self.after_login)

        
    def after_login(self, response):
        print response.body

