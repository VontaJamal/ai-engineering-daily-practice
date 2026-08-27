"""Dependency-free lexical retrieval used as the Day 1 baseline."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import math
import re
from typing import Iterable, Mapping


TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str


@dataclass(frozen=True)
class SearchResult:
    document: Document
    score: float


def tokenize(text: str) -> list[str]:
    """Return lowercase alphanumeric tokens."""

    return TOKEN_PATTERN.findall(text.lower())


def inverse_document_frequencies(documents: Iterable[Document]) -> dict[str, float]:
    """Calculate smoothed inverse document frequencies for a corpus."""

    document_list = list(documents)
    document_frequency: Counter[str] = Counter()
    for document in document_list:
        document_frequency.update(set(tokenize(f"{document.title} {document.text}")))

    document_count = len(document_list)
    return {
        token: math.log((document_count + 1) / (frequency + 1)) + 1
        for token, frequency in document_frequency.items()
    }


def tfidf_vector(text: str, idf: Mapping[str, float]) -> dict[str, float]:
    """Represent text as a sparse TF-IDF vector using a fixed vocabulary."""

    tokens = tokenize(text)
    if not tokens:
        return {}

    counts = Counter(tokens)
    token_count = len(tokens)
    return {
        token: (count / token_count) * idf[token]
        for token, count in counts.items()
        if token in idf
    }


def cosine_similarity(left: Mapping[str, float], right: Mapping[str, float]) -> float:
    """Return cosine similarity for two sparse vectors."""

    if not left or not right:
        return 0.0

    dot_product = sum(value * right.get(token, 0.0) for token, value in left.items())
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return dot_product / (left_norm * right_norm)


class LexicalIndex:
    """A deterministic retrieval baseline that ranks documents by shared terms."""

    def __init__(self, documents: Iterable[Document]) -> None:
        self.documents = tuple(documents)
        if not self.documents:
            raise ValueError("At least one document is required")

        self.idf = inverse_document_frequencies(self.documents)
        self.document_vectors = {
            document.id: tfidf_vector(f"{document.title} {document.text}", self.idf)
            for document in self.documents
        }

    def search(self, query: str, limit: int = 3) -> list[SearchResult]:
        if not query.strip():
            raise ValueError("Query must not be empty")
        if limit < 1:
            raise ValueError("Limit must be at least one")

        query_vector = tfidf_vector(query, self.idf)
        results = [
            SearchResult(
                document=document,
                score=cosine_similarity(query_vector, self.document_vectors[document.id]),
            )
            for document in self.documents
        ]
        return sorted(results, key=lambda result: (-result.score, result.document.id))[:limit]
