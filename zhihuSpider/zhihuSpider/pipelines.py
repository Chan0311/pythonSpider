# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ZhihuspiderImagePipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self,item,info):
        for pic_url in item['pic_urls']:
            yield Request(pic_url,headers={'Host':'pic3.zhimg.com'},meta={'item':item})

    def file_path(self,request,response=None,info=None):
        #item=request.meta['item']
        image_guide=request.url.split('/')[-1]
        filename='full/{0}'.format(image_guide)
        return filename