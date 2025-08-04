---
layout: article
title: Delta-rs vs PySpark
date: 2025-02-15
tags: computer-science, database, datalake
category: computer-science
---

### 背景
- 以下の条件を満たすデータレイクを考える。
  - 対象データは表データ。数は200万ほど。今後も増える予定で、各テーブルの行数列数は小規模から大規模まで様々。
    - 素のCSVファイルから整形されたデータを格納する。整形方法は定まっていない。より洗練された整形手法が実装されれば、それがオリジナルのCSVファイルに適用される。
  - 少人数 (5人)がテーブルのread, write, updateを行える。read数の方がwrite数より多い
  - 出来るだけオープンソースで。クラウドは最終手段。
- 整形されたデータをCSVとして保存しておくのもいいが、以下がネック
  - 整形手法が定まっていないため、整形手法毎でデータを保存したい。データのversioningが欲しい。
  - 複数人がwriteやupdateを行うためACIDトランザクション機能が欲しい。
  - テーブルによってはデータサイズがGB級になるため、出来るだけ削減したい。
- 上記を踏まえて、CSVではなく[Delta Table](https://github.com/delta-io/delta)で保存してPySparkを通じてアクセスするようにした。
  - Delta Tableはdata versioning, ACID transaction, parquet fileをサポートしている

### PySparkの問題点
- とにかく読み込み速度が遅い。Pandasよりは早いが、Polarsよりは遅い。SQLクエリの実行速度はこれらのモジュールより早いが、読み込み速度が遅いため合計すると殆ど違いがない。
- 一挙に別々のテーブルを読み込むと、後半になるにつれて読み出し速度が遅くなって終いにはハングしてしまう。致命的。

### Delta-rsへの移行
- [Delta-rs](https://github.com/delta-io/delta-rs)はPySparkより機能は劣る (ACID transaction, batch processingはできない) もののRustベースのためか読み出し速度がPolars並みに早いし、いくら読み込んでもハングしないためこちらを暫定的に用いることにした。
  - ACID transactionはないため、使用ユーザー間でルール決めは必要
- PySparkが読み込み可能なDelta TableとDelta-rsが読むDelta Tableのバージョンが異なるため、Delta TableをDelta-rsが読み込める形への変換が必要。

