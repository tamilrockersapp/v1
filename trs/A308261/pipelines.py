# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import json
from scrapy.exceptions import DropItem


class A308261Pipeline(object):
    #filename = 'scrapedata.json'
    magnetLink =''
    
    def __init__(self):
        self.ids_seen = set()
    
    #def open_spider(self, spider):
        #self.file = open(self.filename, 'w')

    #def close_spider(self, spider):
        #self.file.close()

    def process_item(self, item, spider):
        #self.magnetLink = item['magnetLink']
        if 'magnetLink' in item:
            self.magnetLink = item['magnetLink']
            if self.magnetLink in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.ids_seen.add(item['magnetLink'])
                #line = json.dumps(dict(item)) + "\n"
                #self.file.write(line)
                item["Thumbnail"]=item["Thumbnail"].split(" ")[0]
                return item 
        else:
                raise DropItem("magnetLink not found: %s" % item)  
            

        
               
    
    
