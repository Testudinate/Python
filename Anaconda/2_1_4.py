https://stepik.org/lesson/58180/step/4?thread=solutions&unit=35865

Task:

Количество столбцов

Прочитайте изображение из файла img.png и выведите количество столбцов этого изображения на стандартный вывод.

В примере входа указана ссылка на файл. Это сделано для вашего удобства. Вы можете скачать этот файл, сохранить как img.png и протестировать решение на своем компьютере.
Sample Input:
https://stepik.org/media/attachments/lesson/58180/img.png
Sample Output:
419

Code:

from skimage.io import imread, imshow, imsave
#img = imread("https://stepik.org/media/attachments/lesson/58180/img.png")
img = imread('img.png')
print(img.shape[1])
