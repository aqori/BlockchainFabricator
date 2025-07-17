# test_blockchainfabricator.py
"""
Tests for BlockchainFabricator module.
"""

import unittest
from blockchainfabricator import BlockchainFabricator

class TestBlockchainFabricator(unittest.TestCase):
    """Test cases for BlockchainFabricator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainFabricator()
        self.assertIsInstance(instance, BlockchainFabricator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainFabricator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
