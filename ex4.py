import numpy as np

rand_char_list = []

for i in range(1,7):
    rand_char = chr(np.random.randint(65,90))
    rand_char_list.append(rand_char)

rand_char_str = "".join(rand_char_list)

code = str(input("Enter the mssg in CAPS: "))

if len(code) <3:
    extracted_data = code[0]
    code = code[1:]
    enc_code = code.__add__(extracted_data)
    print(f"Your encripted data is: ",{enc_code})
else:
    extracted_data = code[0]
    code = code[1:]
    code = code.__add__(extracted_data)
    enc_code = (f"{rand_char_str[0:3]}{code}{rand_char_str[3:6]}")
    print(f"Your encripted data is: ",{enc_code})

if len(code) <3:
    ext_data = enc_code[-1]
    enc_code = enc_code[:-1]
    dec_data = (f"{ext_data}{enc_code}")
    print(f"Your decripted data is: ",{dec_data})
else:
    dec_code_1 = enc_code[3:-3]
    dec_data_extr_data = dec_code_1[-1]
    dec_data = (f"{dec_data_extr_data}{dec_code_1[:-1]}")
    print(f"Your decripted data is: ",{dec_data})
