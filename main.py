def password_check():
    passwords = input('Enter your passwords separated by commas: ').split(',')
    letters = 'abcdefghijklmnopqrstuvwxyz'
    special_characters = '*#+@'
    matching = False

    for password in passwords:
        if ' ' in password or 6 < len(password) or len(password) < 4:
            passwords.remove(password)
            continue

        for i in letters:
            if i in password:
                matching = True
        if not matching:
            passwords.remove(password)
            continue
        matching = False

        for i in letters.upper():
            if i in password:
                matching = True
        if not matching:
            passwords.remove(password)
            continue
        matching = False

        for i in range(10):
            if str(i) in password:
                matching = True
        if not matching:
            passwords.remove(password)
            continue
        matching = False

        for i in special_characters:
            if i in password:
                matching = True
        if not matching:
            passwords.remove(password)

    return passwords


if __name__ == "__main__":
    print(','.join(password_check()))
