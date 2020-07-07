sudo systemctl stop shutdown_button.service
sudo cp shutdown_button.py /usr/local/bin
sudo cp shutdown_button.service /etc/systemd/system
sudo cp *.wav /usr/local/bin
sudo systemctl enable shutdown_button.service
sudo systemctl start shutdown_button.service
