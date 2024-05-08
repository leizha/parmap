import pandas as pd
import unittest
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from parmap import parmap


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        df = pd.DataFrame(
            {
                "name": ["alice", "ben", "cathy"],
            },
            index=[10, 20, 30],
        )

        def hi(name):
            return "hi " + name

        df["message"] = parmap(df["name"], hi)
        self.assertEqual(df["message"].tolist(), ["hi alice", "hi ben", "hi cathy"])


if __name__ == "__main__":
    unittest.main()
