# -*- coding: latin-1 -*-

""" Constants for sets (of characters)

    Copyright (c) 2000, Marc-Andre Lemburg; mailto:mal@lemburg.com
    Copyright (c) 2000-2015, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.
"""
from mx.TextTools.mxTextTools import CharSet

# Simple character strings
a2z = 'abcdefghijklmnopqrstuvwxyz'
A2Z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
umlaute = '����'
Umlaute = '���'
alpha = A2Z + a2z
german_alpha = A2Z + a2z + umlaute + Umlaute
number = '0123456789'
alphanumeric = alpha + number
white = ' \t\v'
newline = '\r\n'
formfeed = '\f'
whitespace = white + newline + formfeed
any = '\000\001\002\003\004\005\006\007\010\011\012\013\014\015\016\017\020\021\022\023\024\025\026\027\030\031\032\033\034\035\036\037 !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\177\200\201\202\203\204\205\206\207\210\211\212\213\214\215\216\217\220\221\222\223\224\225\226\227\230\231\232\233\234\235\236\237\240\241\242\243\244\245\246\247\250\251\252\253\254\255\256\257\260\261\262\263\264\265\266\267\270\271\272\273\274\275\276\277\300\301\302\303\304\305\306\307\310\311\312\313\314\315\316\317\320\321\322\323\324\325\326\327\330\331\332\333\334\335\336\337\340\341\342\343\344\345\346\347\350\351\352\353\354\355\356\357\360\361\362\363\364\365\366\367\370\371\372\373\374\375\376\377'

# Precompiled as sets, e.g. a2z_set = set(a2z)
a2z_set = '\000\000\000\000\000\000\000\000\000\000\000\000\376\377\377\007\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
A2Z_set = '\000\000\000\000\000\000\000\000\376\377\377\007\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
alpha_set = '\000\000\000\000\000\000\000\000\376\377\377\007\376\377\377\007\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
german_alpha_set = '\000\000\000\000\000\000\000\000\376\377\377\007\376\377\377\007\000\000\000\000\000\000\000\000\020\000@\220\020\000@\020'
number_set = '\000\000\000\000\000\000\377\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
alphanumeric_set = '\000\000\000\000\000\000\377\003\376\377\377\007\376\377\377\007\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
white_set = '\000\002\000\000\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
newline_set = '\000$\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
whitespace_set = '\000&\000\000\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'
nonwhitespace_set = '\377\301\377\377\376\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377'
any_set = '\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377'

# Compiled as CharSet instances
a2z_charset = CharSet('a-z')
A2Z_charset = CharSet('A-Z')
umlaute_charset = CharSet('����')
Umlaute_charset = CharSet('���')
alpha_charset = CharSet(A2Z + a2z)
german_alpha_charset = CharSet(A2Z + a2z + umlaute + Umlaute)
number_charset = CharSet('0-9')
alphanumeric_charset = CharSet(alpha + number)
white_charset = CharSet(' \t\v')
newline_charset = CharSet('\r\n')
formfeed_charset = CharSet('\f')
whitespace_charset = CharSet(white + newline + formfeed)
nonwhitespace_charset = CharSet('^' + white + newline + formfeed)
any_charset = CharSet('\000-\377')

# Clean up
del CharSet
