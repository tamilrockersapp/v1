from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class PariHindiHdripXMbEsubsHindiDvdRipTItem(PortiaItem):
    magnetLink = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    screenshot5 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    screenshot6 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Thumbnail = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    test = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Category2 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Category3 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    screenshot2 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    screenshot1 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    screenshot4 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    screenshot3 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Category1 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    torrentLink = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )


class IdamPorulAaviHdripXMbTamilTamilItem(PortiaItem):
    screenshot3 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    screenshot4 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    magnetlink = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    screenshot2 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Screenshot1 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    screenshot5 = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    torrentLink = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
