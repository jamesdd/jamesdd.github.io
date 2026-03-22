# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = 'Galileo'
enable_jsdelivr = {
    "enabled": True,
    "repo": "jamesdd/jamesdd.github.io@gh-pages"
}

# 站点设置
site_name = "Da_Xian的个人博客"
site_logo = "../src/static/翅膀.jpg"
site_build_date = "2022-06-23T13:51+08:00"
author = "Da_Xian"
email = ""
author_homepage = ""
description = "只坚持一种正义。我的正义。"
key_words = ['Maverick', 'Da_Xian', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
   ]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/jamesdd",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
