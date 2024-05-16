#Reno Ikhmal Maulana, 41823010046
def decode_matrix(matriks, n, m):
    string_terdekripsi = ""
    simbol_di_belakang = ""
    for kolom in range(m):
        for baris in range(n):

            if kolom < len(matriks[baris]):
                karakter = matriks[baris][kolom]
                if karakter.isalnum():
                    if string_terdekripsi and not string_terdekripsi[-1].isalnum():
                        string_terdekripsi = string_terdekripsi[:-1] + ' '
                    string_terdekripsi += karakter
                else:
                    if not string_terdekripsi or not string_terdekripsi[-1].isalnum():
                        simbol_di_belakang += karakter
                    else:
                        string_terdekripsi += karakter
    if not string_terdekripsi[-1].isalnum():
        string_terdekripsi = string_terdekripsi[:-1] + simbol_di_belakang
    else:
        string_terdekripsi += simbol_di_belakang
    string_terdekripsi = ' '.join(string_terdekripsi.split())

    return string_terdekripsi
def main():
    with open('scratch.txt', 'r') as file:
        matriks = [line.strip() for line in file]

    n = len(matriks)
    m = max(len(baris) for baris in matriks)

    pesan_terdekripsi = decode_matrix(matriks, n, m)
    print(pesan_terdekripsi)

main()