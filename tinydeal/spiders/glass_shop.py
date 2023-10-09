import scrapy


class GlassShopSpider(scrapy.Spider):
    name = "glass_shop"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        for products in response.xpath("//div[@class='mt-3']"):
            glass_name = products.xpath(".//div[@class='p-title']/a[1]/text()").get()
            glass_name = glass_name.strip()
            glass_price = products.xpath(".//div[@class='p-price']/div[1]/span/text()").get()

            yield{
                "Name" : glass_name,
                "Price" : glass_price
            }

        next_page = response.xpath("//a[@class='page-link']/@href").get()
        if next_page:
            yield scrapy.Request(url = next_page, callback=self.parse)
        

