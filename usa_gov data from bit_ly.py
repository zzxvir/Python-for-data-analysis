Last login: Thu Dec 15 15:35:23 on ttys000
Aaron-no-MacBook-Air:~ AaronChou$ Ipython --pylab
Python 2.7.11 | 64-bit | (default, Jun 11 2016, 03:41:56)
Type "copyright", "credits" or "license" for more information.

IPython 4.1.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
Using matplotlib backend: Qt4Agg

In [1]: import json  // JSON stands for JaveScript Object Notation

In [2]: path = "usagov_bitly_data2012-03-16-1331923249.txt"


/* convert JSON string into a Python dictionary object.
   json module and its loads function invoke on each line in the sample
   file i downloaded
*/

/* This is a list comprehension, which is a concise way of applying
   an operation(like json.loads) to a collection of strings or other objects.
*/
In [3]: records = [json.loads(line) for line in open(path)]

In [4]: records[0] // Python starts with 0, not 1 (like R)
Out[4]:
{u'a': u'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11',
 u'al': u'en-US,en;q=0.8',
 u'c': u'US',
 u'cy': u'Danvers',
 u'g': u'A6qOVH',
 u'gr': u'MA',
 u'h': u'wfLQtf',
 u'hc': 1331822918,
 u'hh': u'1.usa.gov',
 u'l': u'orofrog',
 u'll': [42.576698, -70.954903],
 u'nk': 1,
 u'r': u'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf',
 u't': 1331923247,
 u'tz': u'America/New_York',
 u'u': u'http://www.ncbi.nlm.nih.gov/pubmed/22415991'}

In [5]: records[0]['tz']
Out[5]: u'America/New_York' //u stands for unicode.


In [6]: print records[0]['tz']
America/New_York     // notice that IPython shows the time zone string object representation here rather than its print equivalent.
