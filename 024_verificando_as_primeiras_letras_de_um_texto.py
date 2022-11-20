cidade = str(input('Digite o nome da cidade:'))

if (cidade[:5].lower() == 'santo') or (cidade[:2].lower() == 'st') or (cidade[:3].lower() == 'sto') or (cidade[:4].lower() == 'sto.') or (cidade[:3].lower() == 'st.'):
    print('O nome da cidade começa com Santo!')
else:
    print('O nome da cidade ou não começa com "santo" ou você não sabe escrever.')
