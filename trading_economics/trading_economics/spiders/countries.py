import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/country-list/inflation-rate?continent=world/"]

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            yield{
                #'country_name': name,
                #'link': link
                #scrapy.Request(url=link)
                response.follow(url=link, callback = self.parse_country, meta={'country_name': name})
            }
    def parse_country(self, response):       #Создаем метод парсинг ответа с сайта
        rows = response.xpath("//tr[contains(@class, 'datatable')]")
        for row in rows:
            related = row.xpath(".//td/a/text()").get()
            last = float(row.xpath(".//td[2]/text()").get())
            previous = float(row.xpath(".//td[3]/text()").get())
            name = response.request.meta['country_name']

            yield{
                'country_name': name,
               'related': related,
                'last': last,
                'previous': previous
            }
            