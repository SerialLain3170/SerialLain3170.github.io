---
layout: article # Using our custom category layout
title: history/歴史
permalink: /articles/history/
category_name: history # Custom variable to filter posts
---

{% assign filtered_posts = site.posts | where_exp:"post","post.categories contains page.category_name" %}
{% for post in filtered_posts %}
  {% include article_list_item.html post=post %}
{% endfor %}