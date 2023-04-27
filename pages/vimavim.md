title : VIM basics
author: zvevqx
published: 2025-11-22
cat: linux
desc: ws

...
# Vim Editor

Vim is a powerful and popular text editor that runs in the command-line interface. It is known for its efficient and customizable editing features that allow users to edit text with speed and precision.

## Basic Vim Commands

Here are some of the basic Vim commands you should know:

* `i`: Enters insert mode, allowing you to insert text.
* `Esc`: Exits insert mode and returns to command mode.
* `:w`: Writes the file to disk.
* `:q`: Quits Vim.
* `:q!`: Quits Vim without saving changes.
* `:wq`: Writes the file to disk and quits Vim.
* `yy`: Copies the current line to the clipboard.
* `dd`: Deletes the current line.
* `p`: Pastes the clipboard contents after the cursor.
* `/`: Searches for a pattern in the text.
* `n`: Jumps to the next occurrence of the pattern.
* `N`: Jumps to the previous occurrence of the pattern.

## Advanced Vim Commands

Here are some of the advanced Vim commands you can use to improve your editing workflow:

* `u`: Undoes the last change.
* `Ctrl + r`: Redoes the last change.
* `o`: Inserts a new line below the cursor and enters insert mode.
* `O`: Inserts a new line above the cursor and enters insert mode.
* `:s/pattern/replacement/g`: Replaces all occurrences of a pattern with a replacement string.
* `:%s/pattern/replacement/g`: Replaces all occurrences of a pattern with a replacement string in the entire file.
* `:w !sudo tee %`: Writes the current file with sudo privileges.

## Vim Cheat Sheet

Here's a cheat sheet of common Vim commands:

| Command | Description |
| --- | --- |
| `i` | Enter insert mode |
| `Esc` | Exit insert mode |
| `:w` | Write file |
| `:q` | Quit Vim |
| `:q!` | Quit Vim without saving |
| `:wq` | Write file and quit |
| `yy` | Copy current line |
| `dd` | Delete current line |
| `p` | Paste clipboard contents after cursor |
| `/pattern` | Search for pattern |
| `n` | Jump to next occurrence of pattern |
| `N` | Jump to previous occurrence of pattern |
| `u` | Undo last change |
| `Ctrl + r` | Redo last change |
| `o` | Insert new line below cursor |
| `O` | Insert new line above cursor |
| `:s/pattern/replacement/g` | Replace all occurrences of pattern with replacement |
| `:%s/pattern/replacement/g` | Replace all occurrences of pattern with replacement in entire file |
| `:w !sudo tee %` | Write file with sudo privileges |

Use this cheat sheet as a reference as you become more familiar with Vim. With practice, you'll be able to use Vim to edit text with speed and efficiency.

