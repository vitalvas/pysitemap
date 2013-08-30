PySitemap
=========

A Python library for generating a sitemap



Latest Version
--------------
The latest version of this project can be found at : http://github.com/vitalvas/pysitemap.


Installation
------------
* Option 1 : Install via pip ::

	pip install pysitemap

* Option 2 : If you have downloaded the source ::

	python setup.py install


Documentation
-------------
How to use? ::

	from pysitemap import SiteMap
	from datetime import datetime

	site = SiteMap()
	site.add(
		loc='http://example.com/webhp', 
		lastmod=datetime.now(), 
		changefreq='weekly')

	print site.to_string()


Reporting Bugs
--------------
Please report the bugs at github issue tracker.
https://github.com/vitalvas/pysitemap/issues


Author
------
VitalVas <source@vitalvas.com>
Vitaliy Vasilenko

* http://github.com/vitalvas
* http://www.vitalvas.com
