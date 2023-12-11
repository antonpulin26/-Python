# TODO Найдите количество книг, которое можно разместить на дискете

book_weight_byte = 100*50*25*4
book_weight_megabyte = book_weight_byte/(1024*1024)
disk_volume_megabyte = 1.44
count_books = round((disk_volume_megabyte/book_weight_megabyte),)

print("Количество книг, помещающихся на дискету:", count_books)
