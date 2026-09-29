import unittest
from scope_nonspillover import scoped_nonspillover, broken_shared_store
class ScopeTest(unittest.TestCase):
    def test_safe(self): self.assertTrue(scoped_nonspillover())
    def test_broken_control_is_detected(self): self.assertFalse(broken_shared_store())
if __name__ == '__main__': unittest.main()
