# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_jumia project
#


BOT_NAME = 'scrapy_jumia'

SPIDER_MODULES = ['scrapy_jumia.spiders']
NEWSPIDER_MODULE = 'scrapy_jumia.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_jumia (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'scrapy_jumia.pipelines.ScrapyAmazonPipeline': 300,
}
