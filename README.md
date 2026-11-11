# Portfolio RAG Assistant 🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![CI](https://github.com/saitarus/portfolio-rag-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/saitarus/portfolio-rag-assistant/actions)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-green.svg)](https://www.python.org/)

**同義語展開・キーワードスコアリングに基づく、軽量ローカル RAG（検索・抽出）＆ 提案ドラフト生成エンジン**

A lightweight, dependency-free local Retrieval-Augmented Generation (RAG) assistant that matches project requirements against portfolio assets and drafts tailored proposals.

---

## 🌟 主な特徴 (Features)

1. **ゼロ依存の高速ローカル検索 (Zero External Dependencies)**
   - 重厚なベクトルDBや外部APIキーを一切必要とせず、標準ライブラリのみで高速に動作。
   - オフライン環境やプライベートネットワークでも安全に利用可能。
2. **日英バイリンガル同義語展開 (Synonym Expansion)**
   - 「スクレイピング」→「Playwright, Selenium, クローリング, 抽出」などの表記揺れや専門用語を自動展開。
   - 自然言語の相談文から本質的な技術キーワードを的確にキャッチ。
3. **スコアリングベースの関連度ランキング**
   - タイトル一致（3pt）、技術タグ一致（5pt）、本文コンテキスト一致（1pt）による多層重み付け検索。
4. **自動提案ドラフト生成 (Automated Proposal Drafting)**
   - クライアントからの問い合わせ文に対して、最も適合する過去実績・技術詳細を自動抽出し、受注確度の高い提案文の初稿を即座に出力。

---

## 📁 ディレクトリ構成 (Architecture)

```text
portfolio-rag-assistant/
├── data/
│   └── knowledge_base.json   # ナレッジベース（プロジェクト実績・技術資産）
├── tests/
│   └── test_rag.py           # 単体テスト (同義語展開・検索・生成)
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI
├── rag_engine.py             # RAG コアロジック (検索・スコアリング・提案生成)
├── cli.py                    # 実行用 CLI ツール
├── requirements.txt          # テスト用パッケージ
├── .gitignore                # 除外設定
├── LICENSE                   # MIT ライセンス
└── README.md                 # 本ドキュメント
```

---

## 🚀 クイックスタート (Quick Start)

### 1. リポジトリのクローン

```bash
git clone https://github.com/saitarus/portfolio-rag-assistant.git
cd portfolio-rag-assistant
```

### 2. 検索モード（関連プロジェクトの照会）

```bash
# クエリに関連する実績を検索
python cli.py "音声の文字起こしと字幕を作りたい" --mode search
```

### 3. 提案文生成モード（クライアント相談からのドラフト作成）

```bash
# 相談文から提案ドラフトを自動生成
python cli.py "PythonでWebデータを収集してスプレッドシートに自動反映したい" --mode proposal
```

---

## 📄 ライセンス (License)

本プロジェクトは [MIT License](LICENSE) のもとで公開されています。
