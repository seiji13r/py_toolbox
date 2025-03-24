
sudo apt update
sudo apt install build-essential linux-headers-$(uname -r) -y

sudo su
apt install gcc make



sudo mkdir -p /media/cdrom
sudo mount /dev/cdrom /media/cdrom
sudo /media/cdrom/VBoxLinuxAdditions.run
reboot


modinfo vboxguest
sudo usermod --append --groups vboxsf -- "$USER"
cat /etc/group | grep "$USER"

https://gist.github.com/magnetikonline/1e7e2dbd1b288fecf090f1ef12f0c80b
https://www.linuxtechi.com/install-virtualbox-guest-additions-on-ubuntu/

