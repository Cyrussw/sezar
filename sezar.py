def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def sezar():
    while True:
        print("Sezar Şifreleme ve Şifre Çözme Programı")
        print("1) Oluştur")
        print("2) Çöz")
        print("3) Çıkış")

        choice = input("Seçiminiz (1/2/3): ")

        if choice == '1':
            text = input("Metni girin: ")
            shift = 3
            encrypted_text = encrypt(text, shift)
            print("Şifreli metin: " + encrypted_text)
        elif choice == '2':
            text = input("Şifreli metni girin: ")
            shift = 3
            decrypted_text = decrypt(text, shift)
            print("Çözülmüş metin: " + decrypted_text)
        elif choice == '3':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


sezar()
