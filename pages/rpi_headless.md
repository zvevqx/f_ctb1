title : Raspberry pi headless setup 2023
author: zvevqx
published: 2023-09-23
cat: linux
desc: base commands to setup a rasbperrypi headless as rasbian 2023

...

main source 
[https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/](https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/)


# Flashing the SD card

## the cli way on linux 

*you will need:*

    - sdcard (8go min)
    - sdcard reader

*findind your sd card on the system*


use the `lsblk` command to get the path to your sd card  


on Unix system (`linux`,`osx`) it sould look like : `/dev/sdX`   
if not sure execute `lsblk` with and without the sdcard inserted and compare 

### download os
download the proper version from Raspberry pi website  [link to website](https://www.raspberrypi.com/software/operating-systems/)

### burn it to the sd card with the `dd` command 
🚨 this operation need `sudo` privileges ... be carefull 
 
`sudo dd if=PATH/TO/YOUR/IMAGEFILE.img  of=PATH/TO/YOUR/SDCARD status=progress oflag=sync`

and wait 

 ***done🤞***

## The Gui way 

download and install `rpi-imager` software on your computer and follow allong
 
for linux  
`sudo apt install rpi-imager`

link [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)


---

# Enable `ssh`

create an ampty file on the `bootfs` partition of the sd card 

cli
` touch /PATH/TO/THE/PARTITION/ssh`

---

# Create user and password 

Use `OpenSSL` to encrypt a password:
    `echo 'raspi_users_password' | openssl passwd -6 -stdin` 

Create a file named `userconf` in the root directory of the SD card’s boot partition

` touch /PATH/TO/THE/PARTITION/userconf`

Add a line of text to the new file in the following format: `username:encrypted_password`
 where username is the username you want to use to log in to the Rpi, and encrypted_password is the string generated with OpenSSL.

example 
    `julien:we342swe4422e@343w44@4453@3456`


    



