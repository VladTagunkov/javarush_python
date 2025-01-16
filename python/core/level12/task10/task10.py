# Запись бинарных данных

# Напишите программу, которая читает изображение input_image.jpg и записывает его в другой файл output_image.jpg.

# Напишите тут ваш код

try:
    with open("input_image.jpg","rb") as input_data:
        input_data_img = input_data.read()
        
    with open("output_image.jpg","wb") as output:
        output.write(input_data_img)
except:
    print("Something was wrong!")