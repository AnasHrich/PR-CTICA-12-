import json

def write_json_file(data):
    with open('books.json', 'w') as f:
        json.dump(data, f, indent=4)

def create_book(title, cover, year, pages):
    return {
        "title": title,
        "cover": cover,
        "year": year,
        "pages": pages
    }

def main():
    books = [
        create_book("Book 1", "cover1.jpg", 2018, 200),
        create_book("Book 2", "cover2.jpg", 2016, 300),
        create_book("Book 3", "cover3.jpg", 2017, 400),
        create_book("Book 4", "cover4.jpg", 2014, 500)
    ]
    data = {
        "books": books
    }
    write_json_file(data)
    print(json.dumps(data, indent=4))

if __name__ == '__main__':
    main()