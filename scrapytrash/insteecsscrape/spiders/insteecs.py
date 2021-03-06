from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

from insteecsscrape.items import Scrape70Item

global IGNORED_EXTENSIONS

class InstEECSSpider(CrawlSpider):
    name = "insteecs"
    allow_domains = ["berkeley.edu"]

    start_urls = [
        "http://inst.eecs.berkeley.edu/~cs70/fa13/",
        "http://inst.eecs.berkeley.edu/~cs61c/",
        "http://inst.eecs.berkeley.edu/~cs61a/fa13/"
    ]

    allowedext = ["pptx", "PPTX", "tex", "TEX", "pdf", "PDF"]
    allowedexts = "|".join(str(s) for s in allowedext)
    allowregex = "^.*\.(%s)$"%allowedexts

    rules = (Rule(
        #SgmlLinkExtractor( allow=(allowregex, )),
        SgmlLinkExtractor(),
        callback='parsedoc' ) ,
    )

    links = []

    def parsedoc(self, response):
        # item = Scrape70Item()
        # item['doc'] = response.body
        # item['url'] = response.url

        # return item
        print response.url