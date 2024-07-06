def entry_validate(entry):
    errors = {}

    if not entry.author:
        errors['author'] = 'Автор обязательное поле'
    elif len(entry.author) > 100:
        errors['author'] = "Длина поля не может быть больше 100"

    if not entry.email:
        errors["email"] = 'Эмейл обязательное поле'
    elif len(entry.email) > 254:
        errors['email'] = 'Длина поля не может быть больше 254'

    if not entry.text:
        errors['text'] = 'Текст обязательное поле'
    elif len(entry.text) > 1500:
        errors['text'] = "Длина поля не может быть больше 1500"

    return errors