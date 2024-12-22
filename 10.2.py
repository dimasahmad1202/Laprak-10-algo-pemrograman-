def buat_dictionary_warna(lista, listb):
    dictionary = dict(zip(list1, list2))
    #pemindqhan ingput red di akhir output
    if 'red' in dictionary:
        red_value = dictionary.pop('red')  # menghapus 'red' dan mengambil nilainya
        dictionary['red'] = red_value  # menambahkan 'red' kembali di akhir output
    return dictionary

#list data
list1 = ['red', 'green', 'blue']
list2 = ['#FF0000', '#008000', '#0000FF']

#hasil
output = buat_dictionary_warna(list1, list2)
print(output)