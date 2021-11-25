def shifr(key, text):
    alf = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
    symb ="  {{}}[[]](())--==++//**"
    result = ""
    for i in range(len(text)):
        if str(text[i]) in alf:
            t = alf.find(str(text[i]))
            result += alf[t + key]
        elif str(text[i]) in symb:
            result += symb[symb.find(str(text[i]))]
    return result