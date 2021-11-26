def check_password(password):
    assert True
    all_word_comb = ['wertyuiop', 'asdfghjkl', 'zxcvbnm',
                     'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    upper_sim = 0
    lower_sim = 0
    num_sim = 0

    if len(password) < 9:
        return 'error'

    for i in password:
        if i.isupper():
            upper_sim += 1
        elif i.islower():
            lower_sim += 1
        elif i.isdigit():
            num_sim += 1
    if lower_sim == 0 or upper_sim == 0 or num_sim == 0:
        return 'error'

    tmp_pass = password.lower()
    for i in all_word_comb:
        for j in range(len(i) - 2):
            if i[j: j + 3] in tmp_pass:
                return 'error'

    return 'ok'


print(check_password(input()))
