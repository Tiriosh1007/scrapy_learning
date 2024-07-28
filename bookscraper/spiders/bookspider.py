import scrapy

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com'] # this will confine the spider to only scrape from this domain
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            yield {
                'title': book.css('h3 a::text').get(),
                'price': book.css('p.price_color::text').get(),
                'url': book.css('h3 a::attr(href)').get()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)