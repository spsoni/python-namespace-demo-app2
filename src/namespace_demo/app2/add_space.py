def add_space(name: str):
    spaced_name = ''
    for character in name:
        spaced_name += f'{character} '

    return spaced_name.strip()
