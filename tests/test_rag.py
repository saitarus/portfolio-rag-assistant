import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import pytest
from rag_engine import PortfolioRAG


def test_expand_query():
    rag = PortfolioRAG()
    expanded = rag.expand_query("スクレイピング Python")
    assert "playwright" in expanded
    assert "python" in expanded


def test_search_retrieval():
    rag = PortfolioRAG()
    results = rag.search("文字起こし 字幕", top_k=1)
    assert len(results) > 0
    assert "PROJ-002" == results[0]["id"]


def test_generate_proposal():
    rag = PortfolioRAG()
    draft = rag.generate_proposal_draft("Firebaseで会員機能を作りたい")
    assert "PROJ-004" in draft or "Firebase" in draft
    assert "ご提案ドラフト" in draft
