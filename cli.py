# -*- coding: utf-8 -*-
"""
Portfolio RAG Assistant CLI
ナレッジベース照会および提案文生成コマンドラインツール
"""

import sys
import argparse
from rag_engine import PortfolioRAG


def main():
    parser = argparse.ArgumentParser(description="Portfolio RAG Assistant")
    parser.add_argument("query", nargs="?", default="", help="Search query or client requirement")
    parser.add_argument("--mode", choices=["search", "proposal"], default="search", help="Execution mode")
    parser.add_argument("--top-k", type=int, default=3, help="Number of results to retrieve")
    args = parser.parse_args()

    rag = PortfolioRAG()

    if not args.query:
        print("Usage: python cli.py \"クエリ\" [--mode search|proposal]")
        sys.exit(1)

    if args.mode == "search":
        print(f"--- 検索結果 (クエリ: {args.query}) ---")
        results = rag.search(args.query, top_k=args.top_k)
        for idx, item in enumerate(results, 1):
            print(f"[{idx}] {item['title']} ({item['category']})")
            print(f"    タグ: {', '.join(item.get('tags', []))}")
            print(f"    概要: {item['summary']}\n")
    elif args.mode == "proposal":
        draft = rag.generate_proposal_draft(args.query)
        print(draft)


if __name__ == "__main__":
    main()
