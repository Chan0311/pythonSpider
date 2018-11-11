import requests
import json
from lxml import etree

start_urls = 'https://www.zhihu.com/api/v4/questions/34243513/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset=0'
head = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Upgrade-Insecure-Requests':'1',
  'Host':'www.zhihu.com'
}

r=requests.get(start_urls,headers=head)
print(r.status_code)
page=json.loads(r.text)
#print(page)
content=page['data']
for img in content:
    txt=img['content']
    html=etree.HTML(txt)
    #print(html)
    pic_urs=html.xpath('//img/@data-original')
    for pic_url in pic_urs:
      print(pic_url)