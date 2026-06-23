def translate(text):
    vowels = "aeiou"
    result = []

    for word in text.split():
        index = 0

        # Rule 1
        if word[0] in vowels or word.startswith(("xr", "yt")):
            result.append(word + "ay")
            continue

        # szukamy początku "rdzenia"
        while True:
            # Rule 3 (qu)
            if word[index:index+2] == "qu":
                index += 2
                break

            # Rule 4 (y jako samogłoska)
            if word[index] == "y" and index != 0:
                break

            if word[index] in vowels:
                break

            index += 1

        result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)