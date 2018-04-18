#!/bin/sh

python manage.py loaddata akun/fixtures/User.json;
python manage.py loaddata akun/fixtures/ProfilPengguna.json;
python manage.py loaddata akun/fixtures/Devisi.json;
python manage.py loaddata blog/fixtures/Kategori.json;
python manage.py loaddata blog/fixtures/Tag.json;
python manage.py loaddata blog/fixtures/Artikel.json;
python manage.py loaddata blog/fixtures/Video.json;
python manage.py loaddata sites/fixtures/ProfilOrganisasi.json;
python manage.py loaddata sites/fixtures/SosialMedia.json;
python manage.py loaddata sites/fixtures/Galeri.json;
python manage.py loaddata sites/fixtures/Klien.json;