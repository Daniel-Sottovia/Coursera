from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy_cultural_sp.scrapy_cultural_sp.items import Atracao
from datetime import date
from datetime import datetime

class ViradaCulturalSpider(CrawlSpider):
    name = 'virada_cultural'
    start_urls = ['http://web.archive.org/web/20160825145532/http://www.viradaculturalpaulista.sp.gov.br/cidades']

    def parse(self, response):
        body_sel = Selector(response)
        urls_cidade = body_sel.xpath("//div[@class='list-cities']//ul//li//a/@href").extract()

        for url in urls_cidade:
            yield Request(url, self.parse_atracao)

    def parse_atracao(self, response):
        body_sel = Selector(response)

        cidade = self.to_str(body_sel.xpath("//hq/text()"))
        endereco = self.to_str(body_sel.xpath("//span[@class='address']/text()"))

        atracao_selectors = body_sel.xpath("//ul[@class='list-events']//li")

        for sel in atracao_selectors:
            atracao = Atracao(cidade=cidade, endereco=endereco)
            atracao["dia"] = self.to_date(sel.xpath(".//span[@class='date']//text()"))
            atracao["hora"] = self.to_str(sel.xpath(".//span[@class='hour']//text()"))
            atracao["artista"] = self.to_str(sel.xpath(".//span[@class='artist']//text()"))

            self.print_item(atracao)


    def to_str(self, selector):
        return selector.extract()[0].encode("utf-8")

    def to_date(self, selector):
        data = self.to_str(selector) # => '14/5'
        dia, mes = data.split("/") # => ["14", "5"]
        ano = date.today().year # => 2016
        return datetime(ano, int(mes), int(dia)).strftime("%d-%m-%Y")

    def print_item(self, atracao):
        for k, v in atracao.items():
            print(f"{k}: {v}")
        print("---------------------")