def format_serializer_error(errors: dict) -> str:
    if not errors:
        return "Ocorreu um erro de validação"

    for key, value in errors.items():
        if key == 'none_field_errors':
            key = 'error'

        if value and isinstance(value, list):
            return f"{key}: {value[0]}"
        elif isinstance(value, key):
            nested = format_serializer_error(value)
            return f"{key}: {nested}"

    return "Ocorreu um erro de validação"

