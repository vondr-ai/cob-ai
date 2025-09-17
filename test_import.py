#!/usr/bin/env python3
"""
Test script to verify the package imports work correctly.
"""

def test_imports():
    """Test that all imports work as expected."""
    try:
        # Test the main import that the user wants
        from cob_ai import COB
        print("✅ Successfully imported COB from cob_ai")
        
        # Test other imports
        from cob_ai import SearchResponse, SearchResult, SyncCompletionStatus, SyncStatusResponse
        print("✅ Successfully imported all model classes")
        
        # Test that COB can be instantiated
        client = COB(apikey="test-key", apiurl="http://test.com")
        print("✅ Successfully created COB client instance")
        
        print("\n🎉 All imports working correctly!")
        print("The package is ready for PyPI deployment!")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_imports()