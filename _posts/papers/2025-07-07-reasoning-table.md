---
layout: article
title: "Reasoning-Table: Exploring Reinforcement Learning for Table Reasoning​"
date: 2025-07-07
tags: papers, computer-science, llm
category: papers
---

![](https://chatdoc-arxiv.oss-us-west-1.aliyuncs.com/images/arxiv/2506.01710/first_image.jpeg?AWSAccessKeyId=LTAI5t6b2G8eTtEBczAMwjhc&Signature=pOgzt%2F0SRhgcWXJctNFK1C4Cvls%3D&Expires=9223372038615879680)

## 概要
- 公開日: 2025/06/02
- 機関: University of Chinese Academy of Sciences
- [リンク](https://arxiv.org/pdf/2506.01710)

## 手法

- Supervised fine-tuningでreasoning traceを学習し、Reinforcement learningでパフォーマンスを更に向上させる。
- 学習データの用意
  - SFTの学習データは、ClaudeやDeepSeek-R1等の高性能モデルでベンチマークを走らせてreanoning traceを収集。その後、回答が間違っているものや冗長なreasoning traceを持つ推論データをフィルタリング。
  - RLの学習データはreasoning trace内のカラムやセルを参照している部分に、position evidenceを追加。
- Reward designとしては正しいreasoning traceのフォーマットを奨励する項と、推論結果が正解と近いかどうかをルールベースで計算する項で構成される。

## 評価
- SFT + RLがSFT単体やRL単体よりも高いパフォーマンスを保持する。
- ベンチマーク中の全データを使用するより、簡単なデータを排除したベンチマークで学習したモデルの方が性能は高い。ベンチマークの量より質が大事なのでは。
- RLはSFTよりOODへの耐性が高い。

## 備考・所感
- 同時期にTable-R1を冠する論文やTable-based LLMのInference time scalingを報告した論文が登場している。手法としてはReward designがそれぞれ異なっており、評価としては対象ベンチマークの数が異なっている。