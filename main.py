def sanitize_string(*, string_value: str, exclude: str = 'nNmM', max_result_length: int = 100) -> list[str]:
    if max_result_length < 1:
        raise ValueError('max_result_length cannot be less than 1')

    result_list = []
    if not string_value:
        return result_list

    exclude = set(exclude)
    string_value_length = len(string_value)
    position = 0

    while position < string_value_length:
        if string_value[position] not in exclude:
            result_list.append(string_value[position])
            if len(result_list) == max_result_length:
                break
        position += 1

    return result_list
