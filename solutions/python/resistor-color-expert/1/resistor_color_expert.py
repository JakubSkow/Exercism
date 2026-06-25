def resistor_label(colors):
    values = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    total = 0
    
    if len(colors) == 4:
        for color in colors[:2]:
            total = total * 10 + values[color]
        total = total * (10 ** values[colors[2]])
    elif len(colors) == 5:
        for color in colors[:3]:
            total = total * 10 + values[color]
        total = total * (10 ** values[colors[3]])
    else:
        total = values[colors[0]]
    
    
    
    if total == 0:
        result = str(total) + ' ohms'
    elif total >= 1000000000:
        if (total / 1000000000).is_integer():
            result = str(total // 1000000000) + " gigaohms"
        else:
            result = str(total / 1000000000) + " gigaohms"
    elif total >= 1000000:
        if (total / 1000000).is_integer():
            result = str(total // 1000000) + " megaohms"
        else:
            result = str(total / 1000000) + " megaohms"
    elif total >= 1000:
        if (total / 1000).is_integer():
            result = str(total // 1000) + " kiloohms"
        else:
            result = str(total / 1000) + " kiloohms"
    else:
        result = str(total) + ' ohms'
    
    tolerance = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}
    if len(colors) == 4:
        return result + ' ±' + str(tolerance[colors[3]]) + '%'
    elif len(colors) == 5:
        return result + ' ±' + str(tolerance[colors[4]]) + '%'
    else:
        return result
