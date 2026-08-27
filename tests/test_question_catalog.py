import json
from pathlib import Path
import re
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "llm-fundamentals": ("LLM", 66),
    "prompting": ("PROMPT", 30),
    "rag": ("RAG", 37),
    "agents": ("AGENT", 45),
    "system-design": ("DESIGN", 46),
    "coding": ("CODE", 22),
}


class QuestionCatalogTests(unittest.TestCase):
    def test_catalog_contains_every_expected_question_once(self) -> None:
        all_ids: list[str] = []

        for slug, (prefix, count) in EXPECTED.items():
            content = (REPOSITORY_ROOT / "questions" / f"{slug}.md").read_text()
            ids = re.findall(r"^### ([A-Z]+-\d{3})$", content, flags=re.MULTILINE)
            expected_ids = [f"{prefix}-{index:03d}" for index in range(1, count + 1)]
            self.assertEqual(ids, expected_ids, slug)
            all_ids.extend(ids)

        self.assertEqual(len(all_ids), 246)
        self.assertEqual(len(set(all_ids)), len(all_ids))

    def test_manifest_matches_catalog(self) -> None:
        manifest = json.loads(
            (REPOSITORY_ROOT / "questions" / "source-manifest.json").read_text()
        )

        self.assertEqual(manifest["total_questions"], 246)
        self.assertEqual(set(manifest["sections"]), set(EXPECTED))
        for slug, (prefix, count) in EXPECTED.items():
            self.assertEqual(manifest["sections"][slug]["prefix"], prefix)
            self.assertEqual(manifest["sections"][slug]["count"], count)


if __name__ == "__main__":
    unittest.main()
