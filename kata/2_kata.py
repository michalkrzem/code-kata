# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python


def wave(people):
    """
    Create Wave effect from simple text
    :param people: list
    :return: real_wave: list
    """
    real_wave = []

    for index, letter in enumerate(people):
        if letter != ' ' and letter.isalpha():
            real_wave.append(f"{people[:index]}{people[index].upper()}{people[index + 1:]}")

    return real_wave
