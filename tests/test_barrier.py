"""Unit tests for BarrierSync."""
import unittest
from agent_barrier_sync.barrier import BarrierSync

class TestBarrierSync(unittest.TestCase):
    def test_barrier_release(self):
        b = BarrierSync("M1", {"a1", "a2"})
        self.assertFalse(b.arrive("a1"))
        self.assertFalse(b.is_released())
        self.assertTrue(b.arrive("a2"))
        self.assertTrue(b.is_released())
        self.assertIsNotNone(b.get_manifest())

    def test_unexpected_agent_rejected(self):
        b = BarrierSync("M2", {"a1"})
        with self.assertRaises(ValueError):
            b.arrive("unknown_agent")

if __name__ == "__main__":
    unittest.main()
