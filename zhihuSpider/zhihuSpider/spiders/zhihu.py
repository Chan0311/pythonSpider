# -*- coding: utf-8 -*-
import scrapy
import json
import re
from lxml import etree
from zhihuSpider.items import ZhihuspiderItem
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/questions/34243513/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset=0']

    def parse(self, response):
        res=json.loads(response.text)
        data=res['data']
        for temp in data:
            item=ZhihuspiderItem()
            info=temp['content']
            pic_info=etree.HTML(info)
            item['pic_urls']=pic_info.xpath("//img/@data-original")#.extract()
            yield item
        page_num=int(res['paging']['totals'])
        nex_url=res['paging']['next']
        if page_num>int(nex_url.split('=')[-1]):
            yield scrapy.Request(nex_url,callback=self.parse)