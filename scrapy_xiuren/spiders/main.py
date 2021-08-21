from scrapy.spiders import Spider
from scrapy_xiuren.items import pageDataItem


class downloadspider(Spider):
    name = 'main'
    start_urls = ['https://www.jpxgmn.top/Micat/']

    def parse(self, response):
        yield from response.follow_all(xpath='//li[@class="related_box"]/a', callback=self.parse_page)
        next = response.xpath(
            '//div[@class="pagination"]//a[text()="下一页"]/@href').get()
        if next is not None:
            yield response.follow(next, callback=self.parse)

    # 处理每一个写真首页面,同时获取写真其他的所有页面,给parse_nextpage()函数继续处理
    def parse_page(self, response):
        item = pageDataItem()
        item['url'] = response.url
        item['title'] = response.xpath(
            '//h1[@class="article-title"]/text()').get()
        item['star'] = response.xpath(
            '//span[@class="item item-2"]/a/text()').get()
        pages = response.xpath(
            '//div[@class="pagination"][1]/ul/a/@href')[1:-1]
        item['page_nums'] = len(pages) + 1
        item['organization'] = response.xpath(
            '//div[@class="toptip"]/a[2]/text()').get()
        item['image_urls'] = []
        item['desc'] = response.xpath(
            '//div[@class="article-meta"]/span[4]//text()').getall()[1]
        for page in pages:
            # 将item作为数据传给self.parse_nextpage,使这个函数只需要获取图片的url,
            # 此时item['image_urls'],item['photo_page_url']还没有值
            yield response.follow(page, callback=self.parse_nextpage, meta=item)
        item['photo_page_url'] = response.url
        photo_urls = response.xpath(
            '//img[@onload="size(this)"]/@src').getall()
        for url in photo_urls:
            item['image_urls'].append(response.urljoin(url))
        yield item

    # 获取图片的url,赋值给item['image_urls'],返回一个item给item pipeline处理,他会处理下载
    def parse_nextpage(self, response):
        item = response.meta
        item['photo_page_url'] = response.url
        photo_urls = response.xpath(
            '//img[@onload="size(this)"]/@src').getall()
        for url in photo_urls:
            item['image_urls'].append(response.urljoin(url))
        # 一个item包含这个页面所有图片的url
        yield item
