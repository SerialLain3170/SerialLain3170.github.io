---
layout: article # Using our custom category layout
title: lifehack/ライフハック
permalink: /articles/lifehack/
category_name: lifehack # Custom variable to filter posts
---

{% assign filtered_posts = site.posts | where_exp:"post","post.categories contains page.category_name" %}
{% for post in filtered_posts %}
  {% include article_list_item.html post=post %}
{% endfor %}