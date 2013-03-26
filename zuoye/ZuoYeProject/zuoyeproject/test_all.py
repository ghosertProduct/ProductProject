# coding: utf-8

'''
Created on Mar 26, 2013

@author: jiawzhang
'''

import re
import property

def validate_name(name):
    """
    0. The lenght of the name can't be blank.
    1. The length of the name can't be more than 40.
    2. Only Chinese and 0-9, a-z and "-" are allowed, "-" can't be the first character.
    return errorMessage if there is error, otherwise None.
    """
    if len(name) == 0:
        return property.name_leave_blank
    
    if len(name) > 40:
        return property.name_exceed_forty
    
    alphanumber = ''
    
    # Get rid of Chinese first.
    for s in name:
        if len(s.encode('utf-8')) == 1:
            alphanumber = alphanumber + s
    
    if re.search('(^-|[^a-z0-9-])', alphanumber):
        return property.name_alphnumber_chinese_dash_only
    
    
if __name__ == '__main__':
    name = u's0#张佳伟-sd'
    print 'Validating ' + name
    errorMessage = validate_name(name)
    print errorMessage if errorMessage else 'Pass'
    print
    name = u'-s0张佳伟-sd'
    print 'Validating ' + name
    errorMessage = validate_name(name)
    print errorMessage if errorMessage else 'Pass'
    print
    name = u's0张佳伟-sd'
    print 'Validating ' + name
    errorMessage = validate_name(name)
    print errorMessage if errorMessage else 'Pass'
    print
    name = u''
    print 'Validating ' + name
    errorMessage = validate_name(name)
    print errorMessage if errorMessage else 'Pass'
    print
    name = u'01234567890123456789012345678901234567891'
    print 'Validating ' + name
    errorMessage = validate_name(name)
    print errorMessage if errorMessage else 'Pass'
    
    
    