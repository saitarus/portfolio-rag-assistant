# -*- coding: utf-8 -*-
"""
Local RAG Engine & Proposal Drafter
同義語展開・キーワードスコアリングに基づくナレッジベース照会と自動ドラフト生成
"""

import os
import json
import re
from typing import List, Dict, Any, Optional

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "data", "knowledge_base.json")

SYNONYMS = {
    'スクレイピング': ['scraping', 'crawler', 'playwright', 'selenium', '収集', '抽出', 'クローリング'],
    '文字起こし': ['whisper', '音声', '字幕', 'srt', 'ass', 'demucs', '文字おこし'],
    '自動化': ['automation', '自動化', 'パイプライン', '定期実行', 'バッチ'],
    'web': ['web', 'javascript', 'frontend', 'spa', 'html', 'css', 'react', 'vue'],
    'firebase': ['firebase', 'firestore', 'auth', 'baas'],
    '金融': ['fx', '為替', 'mql', 'ea', 'アルゴリズム', 'backtest', '株式'],
    'python': ['python', 'パイソン']
}


class PortfolioRAG:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or DEFAULT_DB_PATH
        self.records = self._load_data()

    def _load_data(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.db_path):
            return []
        with open(self.db_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def expand_query(self, query: str) -> List[str]:
        """クエリから同義語・関連語を展開"""
        lower = query.lower().strip()
        tokens = re.split(r'[\s,、。]+', lower)
        expanded = set(tokens)

        # 部分一致でもシノニム辞書を走査
        for key, syn_list in SYNONYMS.items():
            if key in lower or any(syn in lower for syn in syn_list):
                expanded.add(key)
                expanded.update(syn_list)

        return [t for t in expanded if t]

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """キーワード適合度に基づくスコアリング検索"""
        expanded_keywords = self.expand_query(query)
        scored = []

        for item in self.records:
            score = 0
            text_corpus = f"{item['title']} {item['category']} {' '.join(item.get('tags', []))} {item['summary']} {item['details']}".lower()

            for kw in expanded_keywords:
                if kw in item.get('tags', []):
                    score += 5
                if kw in item['title'].lower():
                    score += 3
                if kw in text_corpus:
                    score += 1

            if score > 0:
                scored.append({"item": item, "score": score})

        scored.sort(key=lambda x: x["score"], reverse=True)
        return [s["item"] for s in scored[:top_k]]

    def generate_proposal_draft(self, client_inquiry: str) -> str:
        """クライアントの相談文に対して、合致する実績を引用した提案ドラフトを自動生成"""
        matches = self.search(client_inquiry, top_k=2)
        if not matches:
            return "ご相談内容に合致する実績が見つかりませんでした。"

        lines = [
            "【ご提案ドラフト】",
            "ご相談いただき誠にありがとうございます。",
            f"「{client_inquiry}」のご要件につきまして、類似の課題を解決した以下の実装実績がございます。\n"
        ]

        for idx, m in enumerate(matches, 1):
            lines.append(f"■ 実績 {idx}: {m['title']}（{m['category']}）")
            lines.append(f"  - 概要: {m['summary']}")
            lines.append(f"  - 技術詳細: {m['details']}\n")

        lines.append("要件定義から実装・検証・安全な本番運用まで、責任を持って一気通貫で対応いたします。")
        lines.append("ご都合の良い日程にて、詳細をヒアリングさせていただけますと幸いです。")

        return "\n".join(lines)
