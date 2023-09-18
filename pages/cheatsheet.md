title : Cheatsheet all
author: zvevqx
published: 2025-11-22
cat: linux
desc: ws

...

👾 MOST OF THIS PAGE IS DIRECT OUTPUT OF CHATGPT 3.5

# Cheatsheet

## Bash Commands

| Command | Description |
| --- | --- |
| `cd [dir]` | change directory |
| `ls` | list directory contents |
| `pwd` | print working directory |
| `mkdir [dir]` | create a new directory |
| `rm [file]` | remove a file |
| `rm -r [dir]` | remove a directory and its contents |
| `cp [source] [destination]` | copy a file or directory |
| `mv [source] [destination]` | move or rename a file or directory |
| `cat [file]` | display the contents of a file |
| `grep [pattern] [file]` | search for a pattern in a file |

## Git Commands

| Command | Description |
| --- | --- |
| `git init` | initialize a new Git repository |
| `git add [file]` | add a file to the staging area |
| `git commit -m "[message]"` | commit changes with a message |
| `git status` | show the status of the repository |
| `git log` | show the commit history |
| `git push` | push changes to a remote repository |
| `git pull` | pull changes from a remote repository |

## SSH Commands

| Command | Description |
| --- | --- |
| `ssh [user]@[host]` | connect to a remote host via SSH |
| `scp [file] [user]@[host]:[destination]` | copy a file to a remote host |
| `ssh-keygen` | generate an SSH key pair |
| `ssh-copy-id [user]@[host]` | copy your SSH public key to a remote host |

## Python Commands and Tools

| Command | Description |
| --- | --- |
| `python` | start the Python interpreter |
| `pip install [package]` | install a Python package |
| `venv` | create and manage Python virtual environments |

### Python Virtual Environments

| Command | Description |
| --- | --- |
| `python3 -m venv [venv-name]` | create a new virtual environment |
| `source [venv-name]/bin/activate` | activate the virtual environment |
| `deactivate` | deactivate the virtual environment |

## FFmpeg Commands

| Command | Description |
| --- | --- |
| `ffmpeg -i [input] [output]` | convert a video or audio file |
| `ffmpeg -i [input] -ss [time] -t [duration] [output]` | trim a video or audio file |
| `ffmpeg -i [input] -vn -acodec [codec] [output]` | extract audio from a video file |
| `ffmpeg -f concat -safe 0 -i [list.txt] -c copy [output]` | concatenate multiple video or audio files |

## ImageMagick Commands

| Command | Description |
| --- | --- |
| `convert [input] [output]` | convert an image format |
| `mogrify -resize [size] [input]` | resize an image |
| `montage [input1] [input2] -geometry [geometry] [output]` | create a montage of images |

## Arduino Commands

| Command | Description |
| --- | --- |
| `arduino-cli board list` | list available boards |
| `arduino-cli compile --fqbn [board] [sketch]` | compile a sketch |
| `arduino-cli upload -p [port] --fqbn [board
