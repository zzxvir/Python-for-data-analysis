Last login: Thu Dec 15 15:51:35 on ttys000
Aaron-no-MacBook-Air:~ AaronChou$ Ipython --pylab
Python 2.7.11 | 64-bit | (default, Jun 11 2016, 03:41:56)
Type "copyright", "credits" or "license" for more information.

IPython 4.1.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
Using matplotlib backend: Qt4Agg

In [1]: import json

In [2]: path = 'usagov_bitly_data2012-03-16-1331923249.txt'

In [3]: records = [json.loads(line) for line in open (path)]

In [4]: time_zones = [rec['tz'] for rec in records if 'tz' in rec]

In [5]: time_zones[:10]
Out[5]:
[u'America/New_York',
 u'America/Denver',
 u'America/New_York',
 u'America/Sao_Paulo',
 u'America/New_York',
 u'America/New_York',
 u'Europe/Warsaw',
 u'',
 u'',
 u'']

/* use a dic to store counts while we iterate through the time zones
   it counts how many times each time zone appears
*/

In [6]: def get_counts(sequence):
   ...:     counts = {}
   ...:     for x in sequence:
   ...:         if x in counts:
   ...:             counts[x] += 1
   ...:         else:
   ...:             counts[x] = 1
   ...:     return counts
   ...:

In [7]: counts = get_counts(time_zones)

In [8]: counts['America/New_York']
Out[8]: 1251

In [9]: len(time_zones)
Out[9]: 3440

In [10]: def top_counts(count_dic, n = 10):
   ....:     value_key_pairs = [(count, tz) for tz, count in count_dic.items()]
   ....:     value_key_pairs.sort()
   ....:     return value_key_pairs[-n:]
   ....:

In [11]: top_counts(counts)
Out[11]:
[(33, u'America/Sao_Paulo'),
 (35, u'Europe/Madrid'),
 (36, u'Pacific/Honolulu'),
 (37, u'Asia/Tokyo'),
 (74, u'Europe/London'),
 (191, u'America/Denver'),
 (382, u'America/Los_Angeles'),
 (400, u'America/Chicago'),
 (521, u''),
 (1251, u'America/New_York')]

 /* use collection.Counter class will make this task a lot easier:

In [12]: from collections import Counter

In [13]: counts = Counter(time_zones)

In [14]: counts.most_common(10)
Out[14]:
[(u'America/New_York', 1251),
 (u'', 521),
 (u'America/Chicago', 400),
 (u'America/Los_Angeles', 382),
 (u'America/Denver', 191),
 (u'Europe/London', 74),
 (u'Asia/Tokyo', 37),
 (u'Pacific/Honolulu', 36),
 (u'Europe/Madrid', 35),
 (u'America/Sao_Paulo', 33)]
