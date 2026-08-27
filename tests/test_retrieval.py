import math
import unittest

from ai_practice.retrieval import Document, LexicalIndex, cosine_similarity, tokenize


DOCUMENTS = [
    Document(
        id="embeddings",
        title="Embeddings and vector search",
        text="Embeddings represent meaning as numeric vectors for similarity search.",
    ),
    Document(
        id="caching",
        title="Caching",
        text="Caching can reduce repeated model cost and latency.",
    ),
    Document(
        id="agents",
        title="Agents and tools",
        text="An agent chooses bounded actions and calls tools.",
    ),
]


class TokenizeTests(unittest.TestCase):
    def test_normalizes_case_and_punctuation(self) -> None:
        self.assertEqual(tokenize("Vector-Search, VECTOR!"), ["vector", "search", "vector"])


class CosineSimilarityTests(unittest.TestCase):
    def test_identical_vectors_have_similarity_one(self) -> None:
        vector = {"a": 1.0, "b": 2.0}
        self.assertTrue(math.isclose(cosine_similarity(vector, vector), 1.0))

    def test_orthogonal_vectors_have_similarity_zero(self) -> None:
        self.assertEqual(cosine_similarity({"a": 1.0}, {"b": 1.0}), 0.0)


class LexicalIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.index = LexicalIndex(DOCUMENTS)

    def test_ranks_document_with_matching_terms_first(self) -> None:
        results = self.index.search("vector search embeddings")
        self.assertEqual(results[0].document.id, "embeddings")
        self.assertGreater(results[0].score, results[1].score)

    def test_exposes_lexical_limitation_on_paraphrase(self) -> None:
        results = self.index.search("Locate conceptually equivalent snippets")
        self.assertTrue(all(result.score == 0.0 for result in results))
        self.assertNotEqual(results[0].document.id, "embeddings")

    def test_rejects_empty_query(self) -> None:
        with self.assertRaisesRegex(ValueError, "Query must not be empty"):
            self.index.search("   ")

    def test_rejects_non_positive_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "Limit must be at least one"):
            self.index.search("vector", limit=0)


if __name__ == "__main__":
    unittest.main()
