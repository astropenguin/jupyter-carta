echo -n 'Install CARTA ... '

wget -q https://github.com/CARTAvis/carta/releases/download/v1.3.1/CARTA-v1.3.1-remote.tgz
tar xf CARTA-v1.3.1-remote.tgz
rm CARTA-v1.3.1-remote.tgz
mv CARTA-v1.3.1-remote carta
rm carta/carta-backend/lib/libstdc++.so.6

echo 'done!'

echo -n 'Install ngrok ... '

wget -q https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip -q ngrok-stable-linux-amd64.zip
rm ngrok-stable-linux-amd64.zip
mv ngrok carta/ngrok

echo 'Done!'
