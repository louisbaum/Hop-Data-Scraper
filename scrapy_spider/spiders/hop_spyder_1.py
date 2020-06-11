# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

from scrapy_spider.items import hopitem

class HopSpyder1Spider(scrapy.Spider):
    name = 'hop_spyder_1'
    allowed_domains = ['hopslist.com']
    start_urls = ['http://hopslist.com/hops/']

    def parse(self, response):
        hoplist = response.css('a.title')
        for hop in hoplist:
            next_url = hop.css('a::attr(href)').get()
            yield( Request(next_url,callback = self.parse_hop))
       
        
    def parse_hop(self, response):
        item = hopitem()
        item['name'] = response.css('h1.entry-title::text').get()
        tablevalues = response.css('td').extract()
        splitstring = '<td>(.+?)</td>'
        tablevalues = [re.findall(splitstring,x) for x in tablevalues]
             
        index = tablevalues.index(['Also Known As'])+1
        if len(tablevalues[index])>0:
            item['aka'] = tablevalues[index][0]
        
        index = tablevalues.index(['Characteristics'])+1
        if len(tablevalues[index])>0:
            item['characteristics'] = tablevalues[index][0]
            
        index = tablevalues.index(['Purpose'])+1
        if len(tablevalues[index])>0:
                item['purpose'] = tablevalues[index][0]
        
        index = tablevalues.index(['Alpha Acid Composition'])+1
        if len(tablevalues[index])>0:                
                item['alpha_acid'] = tablevalues[index][0]
        
        index = tablevalues.index(['Beta Acid Composition'])+1
        if len(tablevalues[index])>0:                
                item['beta_acid'] = tablevalues[index][0]
        
        index = tablevalues.index(['Co-Humulone Composition'])+1
        if len(tablevalues[index])>0:                
                item['co_humulone'] = tablevalues[index][0]
        
        index = tablevalues.index(['Country'])+1
        if len(tablevalues[index])>0:                
                item['country'] = tablevalues[index][0]

        index = tablevalues.index(['Myrcene Oil Composition'])+1
        if len(tablevalues[index])>0:                
                item['myrcene'] = tablevalues[index][0]            
            
        index = tablevalues.index(['Humulene Oil Composition'])+1
        if len(tablevalues[index])>0:                
                item['humulene'] = tablevalues[index][0]         
    
        index = tablevalues.index(['Caryophyllene Oil'])+1
        if len(tablevalues[index])>0:                
                item['caryophyllene'] = tablevalues[index][0]
                
        index = tablevalues.index(['Farnesene Oil'])+1
        if len(tablevalues[index])>0:                
                item['farnesene'] = tablevalues[index][0]
        
        index = tablevalues.index(['Substitutes'])+1
        if len(tablevalues[index])>0:                
                item['substitutes'] = re.findall('">(.+?)</a>',tablevalues[index][0])
        return(item)
         
 
        
        
        

    
                             