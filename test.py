#!/usr/bin/env python

from pysitemap import SiteMap
from datetime import datetime

site = SiteMap(domain='http://example.com')
site.add(loc='http://example.com/webhp', lastmod=datetime.now(), changefreq='weekly')

print site.to_string()
