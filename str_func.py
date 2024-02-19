def uppercase_string(input_string):

    """Эта ффункция принимает строку и возвращает
    строку с заглавными буквами"""
    return input_string.upper()


def capitalize_words(input_string):

    """Эта функция принимает строку input_string
     и использует метод capitalize() для преобразования
      первой буквы каждого слова в строке в заглавную."""

    return ' '.join(word.capitalize() for word in input_string.split())

