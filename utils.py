def calculate_color_for_breathe(position, hex_color):
    return (position / 256.0) * hex_color

def get_temperature_color(temperature):
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    if temperature < 25:
        return blue

    if temperature >= 25 and temperature < 27:
        return green

    return red
