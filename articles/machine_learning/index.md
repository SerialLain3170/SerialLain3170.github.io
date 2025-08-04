---
layout: article # Using our custom category layout
title: machine learning/機械学習
permalink: /articles/machine-learning/
category_name: machine-learning # Custom variable to filter posts
---

{% assign filtered_posts = site.posts | where_exp:"post","post.categories contains page.category_name" %}
{% for post in filtered_posts %}
  {% include article_list_item.html post=post %}
{% endfor %}