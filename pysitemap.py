# -*- coding: utf-8 -*-


def format_iso8601(obj, timezone):
	updated = '%Y-%m-%dT%H:%M:%S' + timezone
	return obj.strftime(updated)

class SiteMap(object):
	def __init__(self, *args, **kwargs):
		self.timezone = kwargs.get('timezone', 'Z')
		domain = kwargs.get('domain', None)
		self._out = [
			'<?xml version="1.0" encoding="UTF-8"?>',
			'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
		]
		if domain:
			self.add(loc=domain, priority=1)

	def add(self, *args, **kwargs):
		assert 'loc' in kwargs, 'loc is required'
		assert len(kwargs['loc']) <= 2048, 'exceeded the maximum number of characters'
		out = ['\t<url>']
		out.append('\t\t<loc>%s</loc>' % kwargs['loc'])
		if 'lastmod' in kwargs:
			out.append('\t\t<lastmod>%s</lastmod>' % format_iso8601(kwargs['lastmod'], self.timezone))
		if 'changefreq' in kwargs:
			assert kwargs['changefreq'] in ['always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'], 'changefreq not correct'
			out.append('\t\t<changefreq>%s</changefreq>' % kwargs['changefreq'])
		if 'priority' in kwargs:
			assert 0.0 <= kwargs['priority'] <= 1.0, 'priority out of range'
		out.append('\t\t<priority>%s</priority>' % float(kwargs['priority'] if 'priority' in kwargs else 0.5))
		out.append('\t</url>')
		self._out.append("\n".join(out))

	def to_string(self):
		self._out.append('</urlset>')
		return "\n".join(self._out)