def label(colors):
    values = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

    total = 0
    for color in colors[:2]:
        total = total * 10 + values[color]

    total = total * (10 ** values[colors[2]])


    if total == 0:
        return str(total) + ' ohms'
    if total % 1000000000 == 0:
        return str(total // 1000000000) + " gigaohms"
    if total % 1000000 == 0:
        return str(total // 1000000) + " megaohms"
    if total % 1000 == 0:
        return str(total // 1000) + " kiloohms"

    return str(total) + ' ohms'
    
