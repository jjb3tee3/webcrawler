Web Crawler
==========

A web crawler developed using Scrapy 0.22.0 to get the scripts linked to in the Alexa top websites. Currently this just grabs the src value of ```<script>``` tags in the ```<head>```.


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

*V0.1* - February 4th 2014

- Added simple crawler to grab and store src values from script tags.
- Updated items.py with correct fields.
