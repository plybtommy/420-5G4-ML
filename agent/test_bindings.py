import sys
import os

# Add the build directory to sys.path to import the compiled module
sys.path.append(os.path.join(os.getcwd(), "build"))

try:
    import bibliotheque_py as lib_mod
    print("Successfully imported bibliotheque_py")
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def test():
    # Initialize Library and FileManager
    library = lib_mod.Library()
    # Using relative path to data based on build dir location
    # Using path relative to project root /agent/
    file_manager = lib_mod.FileManager("data/books.txt", "data/users.txt")
    
    print("Loading data...")
    if not file_manager.load_library_data(library):
        print("Failed to load library data")
        return

    print("Testing get_all_books multiple times...")
    for i in range(3):
        books = library.get_all_books()
        if books:
            print(f"Call {i+1}: Found {len(books)} books. First book title: {books[0].title}")
        else:
            print(f"Call {i+1}: No books found.")

    print("Test completed successfully without crashing!")

if __name__ == "__main__":
    test()
