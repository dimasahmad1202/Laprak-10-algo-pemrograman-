#program membaca file dan menghitung jumlah pesan berdasarkan gmail
def process_email_logs(file_name):
    try:
        with open(file_name, 'r') as file:
            email_counts = {}
            for line in file:
                # memproses baris yang dimulai dengan "From "
                if line.startswith("From "):
                  #pemecahanbaris menjadi kata-kata
                    words = line.split()
            # Email biasanya berada di posisi kedua
                    email = words[1]
          # Hitung jumlah pesan berdasarkanemail
                    if email in email_counts:
                        email_counts[email] += 1
                    else:
                        email_counts[email] = 1
            return email_counts
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return {}

# Fungsi untuk mencetak histogram email dalam dictionary menggunakan fungsi counts
def main():
    # Meminta input nama file dari pengguna
    file_name = input("Masukkan nama file : ")
    email_counts = process_email_logs(file_name)
    print(email_counts)

# pemanggilan fungsi utama
if __name__ == "__main__":
    main()