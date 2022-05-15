cycle_continuation = 'yes'
while cycle_continuation == 'yes':
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encrypt_key = int(input("Enter encryption key: "))
    encrypt_msg = input("Enter Message: ")
    service_type = input("Enter encrypt or decrypt: ").lower()
    list_encrypt_msg= list(encrypt_msg)
    encrypt_message = []
    decrypt_message = []

    if service_type == "encrypt":
        for i in list_encrypt_msg:
            if i not in alphabet:
                encrypt_message.append(i)
            else:
                value = alphabet.index(i) + encrypt_key
                if value >= len(alphabet):
                    value = value - len(alphabet)
                encrypt_message.append(alphabet[value])
            encrypted_result = ''.join(encrypt_message)
        print(encrypted_result)


    elif service_type == "decrypt":
        for i in list_encrypt_msg:
            if i not in alphabet:
                decrypt_message.append(i)
            else:
                value = alphabet.index(i) - encrypt_key
                decrypt_message.append(alphabet[value])
            encrypted_result = ''.join(decrypt_message)
        print(encrypted_result)

    else:
      print(f"Your request cannot be processed")
    cycle_continuation = input("Would you like to continue playing? \'yes'\ or \'no'\: ").lower()
