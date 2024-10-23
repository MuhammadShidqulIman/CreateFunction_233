def convert_temperature(value, unit):
    if unit == 'C':
        # Mengubah dari Celcius ke Fahrenheit
        return (value * 9/5) + 32
    elif unit == 'F':
        # Mengubah dari Fahrenheit ke Celcius
        return (value - 32) * 5/9
    else:
        return "Satuan tidak valid"

temp_in_fahrenheit = convert_temperature(25, 'C')  # Konversi 25°C ke Fahrenheit
temp_in_celcius= convert_temperature(77, 'F')  # Konversi 77°F ke Celcius
print(F"100'C adalah {temp_in_fahrenheit}'F")
print(F"233'F adalah {temp_in_fahrenheit}'C")