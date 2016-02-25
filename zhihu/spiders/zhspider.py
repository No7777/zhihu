import scrapy

from zhihu.secret import USERNAME, PASSWORD

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    start_urls = ['http://www.zhihu.com/#signin']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                formdata={'email':USERNAME, 'password':PASSWORD},
                callback=self.after_login,
                method='POST',
                url='http://www.zhihu.com/login/email')

        
    def after_login(self, response):
        return scrapy.Request('http://www.zhihu.com', self.parse_index) 

    def parse_index(self, response):
        for title in response.xpath('//a[@class="question_link"]/text()').extract():
            print title
