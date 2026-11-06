#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "library.h"
#include "book.h"
#include "user.h"
#include "filemanager.h"

namespace py = pybind11;

PYBIND11_MODULE(bibliotheque_py, m) {
    m.doc() = "Python bindings for the Library Management System";

    py::class_<Book>(m, "Book")
        .def(py::init<>())
        .def(py::init<std::string, std::string, std::string>())
        .def_property_readonly("title", &Book::getTitle)
        .def_property_readonly("author", &Book::getAuthor)
        .def_property_readonly("isbn", &Book::getISBN)
        .def_property_readonly("is_available", &Book::getAvailability)
        .def_property_readonly("borrower_id", &Book::getBorrowerId)
        .def("check_out", &Book::checkOut)
        .def("return_book", &Book::returnBook)
        .def("to_string", &Book::toString);

    py::class_<User>(m, "User")
        .def(py::init<>())
        .def(py::init<std::string, std::string>())
        .def_property_readonly("name", &User::getName)
        .def_property_readonly("user_id", &User::getUserId)
        .def_property_readonly("borrowed_books", &User::getBorrowedBooks)
        .def("borrow_book", &User::borrowBook)
        .def("return_book", &User::returnBook)
        .def("to_string", &User::toString);

    py::class_<Library>(m, "Library")
        .def(py::init<>())
        .def("add_book", &Library::addBook)
        .def("remove_book", &Library::removeBook)
        .def("find_book_by_isbn", &Library::findBookByISBN, py::return_value_policy::reference_internal)
        .def("search_books_by_title", &Library::searchBooksByTitle, py::return_value_policy::reference_internal)
        .def("search_books_by_author", &Library::searchBooksByAuthor, py::return_value_policy::reference_internal)
        .def("get_available_books", &Library::getAvailableBooks, py::return_value_policy::reference_internal)
        .def("get_all_books", &Library::getAllBooks, py::return_value_policy::reference_internal)
        .def("add_user", &Library::addUser)
        .def("find_user_by_id", &Library::findUserById, py::return_value_policy::reference_internal)
        .def("get_all_users", &Library::getAllUsers, py::return_value_policy::reference_internal)
        .def("check_out_book", &Library::checkOutBook)
        .def("return_book", &Library::returnBook)
        .def("get_total_books", &Library::getTotalBooks)
        .def("get_available_book_count", &Library::getAvailableBookCount)
        .def("get_checked_out_book_count", &Library::getCheckedOutBookCount);

    py::class_<FileManager>(m, "FileManager")
        .def(py::init<const std::string&, const std::string&>())
        .def("save_library_data", &FileManager::saveLibraryData)
        .def("load_library_data", &FileManager::loadLibraryData)
        .def("file_exists", &FileManager::fileExists)
        .def("create_backup", &FileManager::createBackup);
}
