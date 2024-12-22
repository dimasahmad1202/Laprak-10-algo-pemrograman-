def count_domain_messages():
    # Meminta nama file dari pengguna
    file_name = input("Masukkan nama file: ")
    
    try:
        # Membuka file untuk dibaca
        with open(file_name, 'r') as file:
            domain_counts = {}
            
            for line in file:
                # Memproses baris yang dimulai dengan "From "
                if line.startswith("From "):
                    words = line.split()
                    if len(words) > 1:
                        # Mendapatkan alamat email dari baris
                        email = words[1]
                        # Memisahkan domain dari alamat email
                        domain = email.split('@')[-1]
                        # Menambah hitungan domain ke dalam dictionary
                        domain_counts[domain] = domain_counts.get(domain, 0) + 1
            
            # Menampilkan hasil dalam bentuk dictionary
            print(domain_counts)
    
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan. Pastikan file tersebut ada.")

# Memanggil fungsi
count_domain_messages()