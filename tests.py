from main import BooksCollector
import pytest

class TestBooksCollector:

    # 1. Тест добавления новой книги
    def test_add_new_book_adds_book_with_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Розз')
        
        assert 'Розз' in collector.get_books_genre()
        assert collector.get_book_genre('Розз') == ''

    # 2. Тест ограничения по длине названия книги с параметризацией
    @pytest.mark.parametrize('book_name, should_be_added', [
        ('A', True),           
        ('F' * 40, True),      
        ('F' * 41, False),     
        ('', False),           
    ])
    def test_add_new_book_name_length_validation(self, book_name, should_be_added):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        
        if should_be_added:
            assert book_name in collector.get_books_genre()
        else:
            assert book_name not in collector.get_books_genre()

    # 3. Тест установки жанра книги
    def test_set_book_genre_sets_genre_for_existing_book(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тайна перевала Дятлова')
        collector.set_book_genre('Тайна перевала Дятлова', 'Фантастика')
        
        assert collector.get_book_genre('Тайна перевала Дятлова') == 'Фантастика'

    # 4. Тест установки недопустимого жанра с параметризацией
    @pytest.mark.parametrize('genre, expected_result', [
        ('Фантастика', 'Фантастика'),      
        ('Ужасы', 'Ужасы'),                
        ('Неизвестный жанр', ''),          
        ('', ''),                          
    ])
    def test_set_book_genre_with_different_genres(self, genre, expected_result):
        collector = BooksCollector()
        
        collector.add_new_book('Мото Мото')
        collector.set_book_genre('Мото Мото', genre)
        
        assert collector.get_book_genre('Мото Мото') == expected_result

    # 5. Тест получения книг определенного жанра
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        
        collector.add_new_book('Рассомаха')
        collector.set_book_genre('Рассомаха', 'Фантастика')

        collector.add_new_book('Люди в черном')
        collector.set_book_genre('Люди в черном', 'Фантастика')

        collector.add_new_book('Кто?')
        collector.set_book_genre('Кто?', 'Детективы')

        collector.add_new_book('Правда')  

        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy_books) == 2
        assert 'Рассомаха' in fantasy_books
        assert 'Люди в черном' in fantasy_books

        detective_books = collector.get_books_with_specific_genre('Детективы')
        assert len(detective_books) == 1
        assert 'Кто?' in detective_books

        # Тест с несуществующим жанром
        unknown_books = collector.get_books_with_specific_genre('Неизвестный жанр')
        assert len(unknown_books) == 0

    # 6. Тест получения жанра книги по её имени с параметризацией
    @pytest.mark.parametrize('book_name, genre, expected_genre', [
        ('Приключения Вовки', 'Комедии', 'Комедии'),
        ('Гарри Поттер', 'Фантастика', 'Фантастика'),
        ('Опера', 'Детективы', 'Детективы'),
        ('Книга без жанра', '', ''),
    ])
    def test_get_book_genre_returns_correct_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        
        collector.add_new_book(book_name)
        if genre:
            collector.set_book_genre(book_name, genre)
        
        assert collector.get_book_genre(book_name) == expected_genre

    def test_get_book_genre_returns_none_for_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    # 7. Тест получения детских книг с параметризацией
    @pytest.mark.parametrize('book_name, genre, should_be_in_children', [
        ('Колобок', 'Мультфильмы', True),
        ('Маленький принц', 'Фантастика', True),
        ('Комедийная книга', 'Комедии', True),
        ('Страшная книга', 'Ужасы', False),
        ('Детективная книга', 'Детективы', False),
        ('Книга без жанра', '', False),
    ])
    def test_get_books_for_children_filters_appropriate_genres(self, book_name, genre, should_be_in_children):
        collector = BooksCollector()
        
        collector.add_new_book(book_name)
        if genre:
            collector.set_book_genre(book_name, genre)

        children_books = collector.get_books_for_children()
        
        if should_be_in_children:
            assert book_name in children_books
        else:
            assert book_name not in children_books

    # 8. Тест получения полного словаря книг с жанрами
    def test_get_books_genre_returns_complete_dictionary(self):
        collector = BooksCollector()

        test_books = {
            'Приключения Вовки': 'Комедии',
            'Гарри Поттер': 'Фантастика',
            'Опера': 'Детективы',
            'Без жанра': '',
            'Колобок': 'Мультфильмы'
        }

        for book, genre in test_books.items():
            collector.add_new_book(book)
            if genre: 
                collector.set_book_genre(book, genre)

        books_dict = collector.get_books_genre()

        assert isinstance(books_dict, dict)
        assert len(books_dict) == len(test_books)
        
        for book in test_books.keys():
            assert book in books_dict

    # 9. Тест добавления в избранное
    def test_add_book_in_favorites_adds_book_to_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Гарри Поттер')
        
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Гарри Поттер')
        
        assert len(collector.get_list_of_favorites_books()) == 2
        assert 'Война и мир' in collector.get_list_of_favorites_books()
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    # 10. Тест удаления из избранного
    def test_delete_book_from_favorites_removes_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Война и мир')
        
        assert 'Война и мир' not in collector.get_list_of_favorites_books()
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    # 11. Тест получения списка избранных книг
    def test_get_list_of_favorites_books_returns_favorites_list(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        favorites = collector.get_list_of_favorites_books()
        
        assert isinstance(favorites, list)
        assert len(favorites) == 1
        assert 'Гарри Поттер' in favorites
        assert 'Война и мир' not in favorites
