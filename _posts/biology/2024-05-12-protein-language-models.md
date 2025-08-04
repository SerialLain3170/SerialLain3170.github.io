---
layout: article
title: Protein Language Models
date: 2024-05-12
tags: biology, protein language models
category: biology
---

## 概要
- タンパク質は20種類のアミノ酸配列によって構成される。この一次元の配列がタンパク質の3D構造と機能を決定し、配列の順番も重要である。配列の一部が集合体になり、その集合体同氏が結合して、というのを繰り返して最終的な構造を形成する。また、最初の配列が全ての機能を実現する。これらから、言語との共通性が見られ、タンパク質の言語モデルという考えが出てきた。

## 手法
- 自然言語の言語モデルのように、TransformerベースのEncoder, Decoderそしてスケーリングによって性能が上昇していくという流れを汲んでいる。
- スケーリングによるタンパク質言語モデルとしてMeta発の[ESM-2](https://www.science.org/doi/10.1126/science.ade2574)がある。AlphaFold2と比べてパラメータ数が多いながらも精度は低いため、タンパク質構造に特化したモデルほど良い性能は出ないものの、言語モデルと同じように解けるはずという目論見はある程度成功している。

## 参考資料
- [a review on protein language models](https://www.apoorva-srinivasan.com/plms/)
