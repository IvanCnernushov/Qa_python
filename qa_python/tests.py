from main import BooksCollector
import pytest

class TestBooksCollector:

    # 1. Тест добавления новой книги
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Розз')
        
        assert 'Розз' in collector.get_books_genre()
        assert collector.get_book_genre('Розз') == ''

    # 2. Тест ограничения по длине названия книги
    def test_book_name_length_validation(self):
        collector = BooksCollector()
        too_long_title = 'F' * 41
        
        collector.add_new_book(too_long_title)
        
        assert too_long_title not in collector.get_books_genre()

    # 3. Тест установки жанра книги
    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тайна перевала Дятлова')
        collector.set_book_genre('Тайна перевала Дятлова', 'Фантастика')
        
        assert collector.get_book_genre('Тайна перевала Дятлова') == 'Фантастика'

    # 4. Тест установки недопустимого жанра
    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        
        collector.add_new_book('Мото Мото')
        collector.set_book_genre('Мото Мото', 'Неизвестный жанр')
        
        assert collector.get_book_genre('Мото Мото') == ''

    # 5. Тест получения книг определенного жанра
    def test_get_books_by_genre(self):
        collector = BooksCollector()
        
        collector.add_new_book('Рассомаха')
        collector.set_book_genre('Рассомаха', 'Фантастика')

        collector.add_new_book('Люди в черном')
        collector.set_book_genre('Люди в черном', 'Фантастика')

        collector.add_new_book('Кто?')
        collector.set_book_genre('Кто?', 'Детективы')

        collector.add_new_book('Правда')  # Книга без жанра

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

    # 6. Тест получения жанра книги по её имени
    def test_get_book_genre_by_name(self):
        collector = BooksCollector()
        
        collector.add_new_book('Приключения Вовки')
        collector.set_book_genre('Приключения Вовки', 'Комедии') 

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Опера')
        collector.set_book_genre('Опера', 'Детективы')

        assert collector.get_book_genre('Приключения Вовки') == 'Комедии'
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'
        assert collector.get_book_genre('Опера') == 'Детективы'
    
        assert collector.get_book_genre('Несуществующая книга') is None

    # 7. Тест получения детских книг
    def test_get_books_for_children(self):
        collector = BooksCollector()
        
    
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы') 

        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', 'Фантастика') 

        collector.add_new_book('Комедийная книга')
        collector.set_book_genre('Комедийная книга', 'Комедии')

        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', 'Ужасы') 

        collector.add_new_book('Детективная книга')
        collector.set_book_genre('Детективная книга', 'Детективы') 

        collector.add_new_book('Книга без жанра')

        children_books = collector.get_books_for_children()
        
        assert 'Колобок' in children_books
        assert 'Маленький принц' in children_books
        assert 'Комедийная книга' in children_books
        
        assert 'Страшная книга' not in children_books
        assert 'Детективная книга' not in children_books
        
        assert 'Книга без жанра' not in children_books

    # 8. Тест получения полного словаря книг с жанрами
    def test_get_full_books_genre_dictionary(self):
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
    def test_add_to_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Гарри Поттер')
        
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Гарри Поттер')
        
        assert len(collector.get_list_of_favorites_books()) == 2
        assert 'Война и мир' in collector.get_list_of_favorites_books()
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    # 10. Тест удаления из избранного
    def test_remove_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Гарри Поттер')

        # Удаляем одну книгу из избранного
        collector.delete_book_from_favorites('Война и мир')
        
        assert 'Война и мир' not in collector.get_list_of_favorites_books()
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    # 11. Тест получения списка избранных книг
    def test_get_favorites_list(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        favorites = collector.get_list_of_favorites_books()
        
        assert isinstance(favorites, list)
        assert len(favorites) == 1
        assert 'Гарри Поттер' in favorites
        assert 'Война и мир' not in favorites
