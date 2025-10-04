# 1. Тест добавления новой книги
# 2. Тест ограничения по длине названия книги с параметризацией
# 3. Тест установки жанра книги
# 4. Тест установки недопустимого жанра с параметризацией
# 5. Тест получения книг определенного жанра
# 6. Тест получения жанра книги по её имени с параметризацией
# 7. Тест получения детских книг с параметризацией
# 8. Тест получения полного словаря книг с жанрами
# 9. Тест добавления в избранное
# 10. Тест удаления из избранного
# 11. Тест получения списка избранных книг
collected 11 items

tests.py::TestBooksCollector::test_add_new_book_adds_book_with_empty_genre PASSED [  3%]
tests.py::TestBooksCollector::test_add_new_book_name_length_validation[A-True] PASSED [  7%]
tests.py::TestBooksCollector::test_add_new_book_name_length_validation[FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF-True] PASSED [ 11%]
tests.py::TestBooksCollector::test_add_new_book_name_length_validation[FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF-False] PASSED [ 15%]
tests.py::TestBooksCollector::test_add_new_book_name_length_validation[-False] PASSED [ 19%]
tests.py::TestBooksCollector::test_set_book_genre_sets_genre_for_existing_book PASSED [ 23%]
tests.py::TestBooksCollector::test_set_book_genre_with_different_genres[\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 26%]
tests.py::TestBooksCollector::test_set_book_genre_with_different_genres[\u0423\u0436\u0430\u0441\u044b-\u0423\u0436\u0430\u0441\u044b] PASSED [ 30%]
tests.py::TestBooksCollector::test_set_book_genre_with_different_genres[\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0439 \u0436\u0430\u043d\u0440-] PASSED [ 34%]
tests.py::TestBooksCollector::test_set_book_genre_with_different_genres[-] PASSED [ 38%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_returns_correct_books PASSED [ 42%]
tests.py::TestBooksCollector::test_get_book_genre_returns_correct_genre[\u041f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0412\u043e\u0432\u043a\u0438-\u041a\u043e\u043c\u0435\u0434\u0438\u0438-\u041a\u043e\u043c\u0435\u0434\u0438\u0438] PASSED [ 46%]
tests.py::TestBooksCollector::test_get_book_genre_returns_correct_genre[\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 50%]
tests.py::TestBooksCollector::test_get_book_genre_returns_correct_genre[\u041e\u043f\u0435\u0440\u0430-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 53%]
tests.py::TestBooksCollector::test_get_book_genre_returns_correct_genre[\u041a\u043d\u0438\u0433\u0430 \u0431\u0435\u0437 \u0436\u0430\u043d\u0440\u0430--] PASSED [ 57%]
tests.py::TestBooksCollector::test_get_book_genre_returns_none_for_nonexistent_book PASSED [ 61%]
tests.py::TestBooksCollector::test_get_books_for_children_filters_appropriate_genres[\u041a\u043e\u043b\u043e\u0431\u043e\u043a-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b-True] PASSED [ 65%]
tests.py::TestBooksCollector::test_get_books_for_children_filters_appropriate_genres[\u041c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0439 \u043f\u0440\u0438\u043d\u0446-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430-True] PASSED [ 69%]
tests.py::TestBooksCollector::test_get_books_for_children_filters_appropriate_genres[\u041a\u043e\u043c\u0435\u0434\u0438\u0439\u043d\u0430\u044f \u043a\u043d\u0438\u0433\u0430-\u041a\u043e\u043c\u0435\u0434\u0438\u0438-True] PASSED [ 73%]
tests.py::TestBooksCollector::test_get_books_for_children_filters_appropriate_genres[\u0421\u0442\u0440\u0430\u0448\u043d\u0430\u044f \u043a\u043d\u0438\u0433\u0430-\u0423\u0436\u0430\u0441\u044b-False] PASSED [ 76%]
tests.py::TestBooksCollector::test_get_books_for_children_filters_appropriate_genres[\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u043a\u043d\u0438\u0433\u0430-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b-False] PASSED [ 80%]
tests.py::TestBooksCollector::test_get_books_for_children_filters_appropriate_genres[\u041a\u043d\u0438\u0433\u0430 \u0431\u0435\u0437 \u0436\u0430\u043d\u0440\u0430--False] PASSED [ 84%]
tests.py::TestBooksCollector::test_get_books_genre_returns_complete_dictionary PASSED [ 88%]
tests.py::TestBooksCollector::test_add_book_in_favorites_adds_book_to_favorites PASSED [ 92%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_removes_book_from_favorites PASSED [ 96%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_returns_favorites_list PASSED [100%]

