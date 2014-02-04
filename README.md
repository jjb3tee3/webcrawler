Web Crawler
==========

A web crawler developed using Scrapy 0.22.0 to get the scripts linked to in the Alexa top websites. Currently this just grabs the src value of <script> tags in the <head>.

This information will be collated anonymously and analysed to determine the most common scripts linked to from CDNs.

Scrapy 0.22.0
=============

Installation process is found <a href="http://doc.scrapy.org/en/latest/intro/install.html">here</a>.

Usage
=====

```
scrapy crawl webcrawler -o items.json -t json
```

Version History
===============

<b>V0.1</b> - February 4th 2014

	o Added simple crawler to grab and store src values from script tags.
	o Updated items.py with correct fields.
