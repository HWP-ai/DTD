#-*- encoding: utf-8 -*-

####### usage:
#######        cat xml | python validate.py

from lxml import etree
import sys

dtd = etree.DTD(open('experimental/lmpd.dtd'))

root = etree.XML(sys.stdin.read())

v = dtd.validate(root)

print('Validate: %s' % v)

if not v :
    print(dtd.error_log.filter_from_errors()[0])
