Cara jalanlan kan file:
masuk terminal ke project -> face-recognition

atau cd ~/project/Web

cara ganti jaringan:
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Lalu Ketik nama Wifi (SSID)
dan password

Contoh:
network={
   ssid="Test Wifi Network"
   psk="SecretPassWord"
}

save ctrl+x -> y - > enter

cara jalanin server:
gunicorn --bind 0.0.0.0:5000 wsgi:app 

Cara Masukan training model
cd ~/project/face-recognition/dataset/
mkdir husen
mkdir ihsan
mkdir indra
dan masukan foto teman anda, bisa di dapat dari facebook yang penting foto selfie/closeup.
Setelah selesai menyimpan foto di masing masing direktori, selanjutnya kita akan melakukan encoding ke file pickle 
dengan script face-encoding.py yang telah kita buat. Jalan perintah berikut di direktori project anda.

cd ~/project/face-recognition/

python3 face-encoding.py --dataset dataset --encodings encodings.pickle --detection-method hog

Tunggu hingga proses encoding selesai. Setelah selesai anda akan menemukan file baru di direktori anda dengan 
nama encodings.pickle.

Contoh struktur direktori yang sudah jadi adalah seperti di bawah ini.

(cv) pi@raspberrypi:~/project/face-recognition $ tree
.
├── dataset
│   ├── Husen
│   │   ├── 001.jpg
│   │   ├── 002.jpg
│   │   ├── 003.jpg
│   │   ├── 004.jpg
│   │   ├── 005.jpg
│   │   ├── 006.jpg
│   │   ├── 007.jpg
│   │   └── 008.jpeg
│   ├── Ihsan
│   │   ├── 001.jpg
│   │   ├── 002.jpg
│   │   ├── 003.jpg
│   │   ├── 004.jpg
│   │   └── 005.jpg
│   └── Indra
│       ├── 001.jpg
│       ├── 002.jpg
│       ├── 003.jpg
│       ├── 004.jpg
│       ├── 005.jpg
│       ├── 006.jpg
│       └── 007.jpg
├── encodings.pickle
├── face-encoding.py
├── face-recognition-video.py
└── haarcascade_frontalface_default.xml


Lalu jalankan dengan perintah :

python3 face-recognition-video.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle

Exit:
Ke Terminal, Lalu Ctrl+C

server:
gunicorn main:app

agar bisa dibuka web nya dijaringan wifi yang sama:

http://ip-raspberrypi:5000/

contoh:
http://192.168.1.10:5000/

Jika error maka jalankan dulu:
gunicorn --bind 0.0.0.0:5000 wsgi:app

Terima Kasih.

CV.JADI DUIT INDONESIA (https://jadiduit.org)