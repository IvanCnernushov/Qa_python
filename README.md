# 1. Тест добавления новой книги
# 2. Тест ограничения по длине названия книги
# 3. Тест установки жанра книги
# 4. Тест установки недопустимого жанра
# 5. Тест получения книг определенного жанра
# 6. Тест получения жанра книги по её имени
# 7. Тест получения детских книг
# 8. Тест получения полного словаря книг с жанрами
# 9. Тест добавления в избранное
# 10. Тест удаления из избранного
# 11. Тест получения списка избранных книг
collected 11 items

tests.py::TestBooksCollector::test_add_new_book PASSED                   [  9%]
tests.py::TestBooksCollector::test_book_name_length_validation PASSED    [ 18%]
tests.py::TestBooksCollector::test_set_book_genre_valid PASSED           [ 27%]
tests.py::TestBooksCollector::test_set_book_genre_invalid PASSED         [ 36%]
tests.py::TestBooksCollector::test_get_books_by_genre PASSED             [ 45%]
tests.py::TestBooksCollector::test_get_book_genre_by_name PASSED         [ 54%]
tests.py::TestBooksCollector::test_get_books_for_children PASSED         [ 63%]
tests.py::TestBooksCollector::test_get_full_books_genre_dictionary PASSED [ 72%]
tests.py::TestBooksCollector::test_add_to_favorites PASSED               [ 81%]
tests.py::TestBooksCollector::test_remove_from_favorites PASSED          [ 90%]
tests.py::TestBooksCollector::test_get_favorites_list PASSED             [100%]
