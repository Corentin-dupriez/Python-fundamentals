def search_for_person(name: str, book: dict) -> str:
    if name in book.keys():
        return f'{name} -> {book[name]}'
    return f'Contact {name} does not exist.'


phonebook = {}
searches = None

while True:
    command = input()
    if command.isdigit():
        searches = int(command)
        break
    person, number = command.split('-')
    phonebook[person] = number

for attempt in range(searches):
    person_to_search = input()
    print(search_for_person(person_to_search, phonebook))
