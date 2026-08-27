"""Command-line runner for Day 1's lexical retrieval baseline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ai_practice.retrieval import Document, LexicalIndex


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOCUMENTS = REPOSITORY_ROOT / "data" / "sample_documents.json"


def load_documents(path: Path) -> list[Document]:
    with path.open(encoding="utf-8") as source:
        records = json.load(source)
    return [Document(**record) for record in records]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True, help="Text to retrieve relevant documents for")
    parser.add_argument("--limit", type=int, default=3, help="Number of results to show")
    parser.add_argument(
        "--documents",
        type=Path,
        default=DEFAULT_DOCUMENTS,
        help="Path to a JSON document collection",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    index = LexicalIndex(load_documents(args.documents))
    results = index.search(args.query, args.limit)

    print(f"Query: {args.query}")
    for rank, result in enumerate(results, start=1):
        print(f"{rank}. [{result.document.id}] {result.document.title} (score={result.score:.3f})")
        print(f"   {result.document.text}")


if __name__ == "__main__":
    main()
