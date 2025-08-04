---
layout: article # Using our custom category layout
title: computer science/計算機科学
permalink: /articles/computer-science/
category_name: computer-science # Custom variable to filter posts
---

{% assign filtered_posts = site.posts | where_exp:"post","post.categories contains page.category_name" %}
{% for post in filtered_posts %}
  {% include article_list_item.html post=post %}
{% endfor %}