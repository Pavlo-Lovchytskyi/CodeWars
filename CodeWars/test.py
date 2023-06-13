from datetime import datetime, date


class Note:
    def __init__(self):
        self.notes = []
        self.dates = None

    def add_note(self, note_text, tags):
        note = {'text': note_text, 'tags': tags}
        self.notes.append(note)
        self.dates = datetime.now()
        print(f"Заметка - {self.notes} - сохранена.")
        print(f'Время заметки: {self.dates}')

    def search_notes(self, keyword):
        found_notes = []
        for note in self.notes:
            if keyword in note['text'] or keyword in note['tags']:
                found_notes.append(note)
        if found_notes:
            print("Найдены заметки:")
            for note in found_notes:
                print(note['text'])
        else:
            print("Заметки не найдены.")

    def edit_note(self, note_index, new_text):
        if note_index < len(self.notes):
            self.notes[note_index]['text'] = new_text
            print("Заметка отредактирована.")
        else:
            print("Неверный индекс заметки.")

    def delete_note(self, note_index):
        if note_index < len(self.notes):
            del self.notes[note_index]
            print("Заметка удалена.")
        else:
            print("Неверный индекс заметки.")

    def sort_notes_by_tag(self, tag):
        sorted_notes = []
        for note in self.notes:
            if tag in note['tags']:
                sorted_notes.append(note)
        if sorted_notes:
            sorted_notes.sort(key=lambda x: x['text'])
            print(f"Отсортированные заметки: {sorted_notes}")
            for note in sorted_notes:
                print(note['text'])
        else:
            print("Заметки с указанным тегом не найдены.")


# Пример использования
assistant = Note()

assistant.add_note("Встреча с клиентом в понедельник", ["работа", "встреча"])
assistant.add_note("Купить продукты в магазине", ["покупки"])
assistant.add_note("Изучить новый язык программирования",
                   ["учеба", "программирование"])

assistant.search_notes("Купить")

assistant.edit_note(0, "Встреча с клиентом во вторник")

assistant.sort_notes_by_tag("работа")

assistant.delete_note(1)
