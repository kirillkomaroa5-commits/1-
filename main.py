import json
from datetime import datetime

def load_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book():
    books = load_books()
    author = input("Введите автора: ").strip()
    title = input("Введите название: ").strip()

    # Проверка на дубликаты
    if any(book['author'] == author and book['title'] == title for book in books):
        print("Книга с таким автором и названием уже существует!")
        return

    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    date = input("Введите дату прочтения (YYYY-MM-DD) или нажмите Enter для текущей даты: ").strip()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    new_book = {
        'author': author,
        'title': title,
        'rating': rating,
        'date': date
    }

    books.append(new_book)
    save_books(books)
    print("Книга успешно добавлена!")

def show_all_books():
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
    print("\n--- Список всех книг ---")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} — {book['author']} (Оценка: {book['rating']}, Дата: {book['date']})")
    print()

def show_average_rating():
    books = load_books()
    if not books:
        print("Нет данных для расчёта средней оценки.")
        return
    total_rating = sum(book['rating'] for book in books)
    average = total_rating / len(books)
    print(f"Средняя оценка всех книг: {average:.2f}")

def show_author_stats():
    books = load_books()
    if not books:
        print("Нет данных для статистики.")
        return
    author_count = {}
    for book in books:
        author = book['author']
        author_count[author] = author_count.get(author, 0) + 1
    print("\n--- Статистика по авторам ---")
    for author, count in author_count.items():
        print(f"{author}: {count} книг")
    print()

def delete_book():
    books = load_books()
    if not books:
        print("Список книг пуст, удалять нечего.")
        return
    show_all_books()
    try:
        choice = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= choice < len(books):
            removed_book = books.pop(choice)
            save_books(books)
            print(f"Книга '{removed_book['title']}' успешно удалена.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Пожалуйста, введите корректный номер.")

def main():
    while True:
        print("\n--- Трекер прочитанных книг ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == '1':
            add_book()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_average_rating()
        elif choice == '4':
            show_author_stats()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
