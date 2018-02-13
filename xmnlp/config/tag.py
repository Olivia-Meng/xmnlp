# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

# -------------------------------------------#
# author: sean lee                           #
# email: xmlee97@gmail.com                   #
#--------------------------------------------#

"""MIT License
Copyright (c) 2018 Sean
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import sys
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')

# reference [汉语词性对照表[北大标准/中科院标准]](http://blog.csdn.net/kevin_darkelf/article/details/39520881)
tag_dict = {
    'Ag'   : '形语素 (形容词性语素。形容词代码为a，语素代码ｇ前面置以A)',
    'a'    : '形容词 (取英语形容词adjective的第1个字母)',
    'ad'   : '副形词 (直接作状语的形容词。形容词代码a和副词代码d并在一起)',
    'an'   : '名形词 (具有名词功能的形容词。形容词代码a和名词代码n并在一起)',
    'b'    : '区别词 (取汉字“别”的声母)',
    'c'    : '连词 (取英语连词 conjunction的第1个字母)',
    'dg'   : '副语素 (副词性语素。副词代码为 d，语素代码ｇ前面置以D)',
    'd'    : '副词 (取adverb的第2个字母，因其第1个字母已用于形容词)',
    'e'    : '叹词 (取英语叹词 exclamation的第1个字母)',
    'f'    : '方位词 (取汉字“方”)',
    'g'    : '语素 (绝大多数语素都能作为合成词的“词根”，取汉字“根”的声母)',
    'h'    : '前接成分 (取英语head的第1个字母)',
    'i'    : '成语 (取英语成语 idiom的第1个字母)',
    'j'    : '简称略语 (取汉字“简”的声母)',
    'k'    : '后接成分',
    'l'    : '习用语 (习用语尚未成为成语，有点“临时性”，取“临”的声母)',
    'm'    : '数词 (取英语 numeral的第3个字母，n，u已有他用)',
    'Ng'   : '名语素 (名词性语素。名词代码为n，语素代码ｇ前面置以N)',
    'n'    : '名词 (取英语名词noun的第1个字母)',
    'nr'   : '人名 (名词代码n和“人(ren)”的声母并在一起)',
    'ns'   : '地名 (名词代码n和处所词代码s并在一起)',
    'nt'   : '机构团体 (“团”的声母为 t，名词代码n和t并在一起)',
    'nz'   : '其他专名 (“专”的声母的第 1个字母为z，名词代码n和z并在一起)',
    'o'    : '拟声词 (取英语拟声词onomatopoeia的第1个字母)',
    'p'    : '介词 (取英语介词prepositional的第1个字母)',
    'q'    : '量词 (取英语 quantity的第1个字母)',
    'r'    : '代词 (取英语代词pronoun的第2个字母,因p已用于介词)',
    's'    : '处所词 (取英语space的第1个字母)',
    'tg'   : '时语素 (时间词性语素。时间词代码为t,在语素的代码g前面置以T)',
    't'    : '时间词 (取英语time的第1个字母)',
    'u'    : '助词 (取英语助词 auxiliary)',
    'vg'   : '动语素 (动词性语素。动词代码为v。在语素的代码g前面置以V)',
    'v'    : '动词 (取英语动词 verb的第一个字母)',
    'vd'   : '副动词 (直接作状语的动词。动词和副词的代码并在一起)',
    'vn'   : '名动词 (指具有名词功能的动词。动词和名词的代码并在一起)',
    'w'    : '标点符号',
    'x'    : '非语素字 (非语素字只是一个符号，字母 x通常用于代表未知数、符号)',
    'y'    : '语气词 (取汉字“语”的声母)',
    'z'    : '状态词 (取汉字“状”的声母的前一个字母)',
    'un'   : '未知词 (不可识别词及用户自定义词组)'
} 