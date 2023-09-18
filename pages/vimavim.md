title : VIM basics
author: zvevqx
published: 2025-11-22
cat: linux
desc: ws

...


👾 MOST OF THIS PAGE IS DIRECT OUTPUT OF CHATGPT 3.5

# Vim Editor

Vim is a powerful and popular text editor that runs in the command-line interface. It is known for its efficient and customizable editing features that allow users to edit text with speed and precision.

# Main Vim Operations


| Operation               | Shortcut                  | Description                                        |
|-------------------------|---------------------------|----------------------------------------------------|
| **Navigation**          |                           |                                                    |
| Move left               | `h`                       | Move the cursor left.                             |
| Move down               | `j`                       | Move the cursor down.                             |
| Move up                 | `k`                       | Move the cursor up.                               |
| Move right              | `l`                       | Move the cursor right.                            |
| Move forward one word   | `w`                       | Move forward one word.                            |
| Move backward one word  | `b`                       | Move backward one word.                           |
| Move to end of line     | `$`                       | Move to the end of the current line.              |
| Move to beginning       | `0`                       | Move to the beginning of the current line.        |
| Move to end of file     | `G`                       | Move to the end of the file.                      |
| Move to beginning of file | `gg`                    | Move to the beginning of the file.                |
| Move to specific line   | `<line_number>G`           | Move to a specific line number.                   |
| Move to matching bracket| `%`                       | Move to the matching parenthesis, bracket, or brace.|
| Move to paragraph start | `{`                       | Move to the beginning of the current paragraph.   |
| Move to paragraph end   | `}`                       | Move to the end of the current paragraph.         |
| Move half a page up     | `Ctrl+u`                  | Move half a page up.                              |
| Move half a page down   | `Ctrl+d`                  | Move half a page down.                            |
| **Editing**             |                           |                                                    |
| Insert before cursor    | `i`                       | Insert text before the cursor.                    |
| Insert at line start    | `I`                       | Insert text at the beginning of the current line. |
| Append after cursor     | `a`                       | Append text after the cursor.                     |
| Append at line end      | `A`                       | Append text at the end of the current line.       |
| Open line below cursor  | `o`                       | Open a new line below the current line and enter insert mode. |
| Open line above cursor  | `O`                       | Open a new line above the current line and enter insert mode. |
| Delete character        | `x`                       | Delete the character under the cursor.            |
| Delete current line     | `dd`                      | Delete the current line.                          |
| Yank (copy) current line| `yy`                     | Yank (copy) the current line.                     |
| Paste after cursor      | `p`                       | Paste the yanked text after the cursor.           |
| Paste before cursor     | `P`                       | Paste the yanked text before the cursor.          |
| Undo                    | `u`                       | Undo the last change.                             |
| Redo                    | `Ctrl+r`                  | Redo the last change.                             |
| **Search and Replace**  |                           |                                                    |
| Search forward          | `/search_term`             | Search forward for "search_term."                |
| Search backward         | `?search_term`             | Search backward for "search_term."               |
| Move to next search result | `n`                   | Move to the next search result.                  |
| Move to previous search result | `N`               | Move to the previous search result.              |
| Replace on current line | `:s/search_term/replacement`| Replace "search_term" with "replacement" on the current line. |
| Global replace         | `:%s/search_term/replacement/g` | Replace "search_term" with "replacement" globally in the file. |
| Turn off search highlighting | `:noh`             | Turn off search result highlighting.             |
| **Saving and Quitting** |                         |                                                    |
| Save                    | `:w`                      | Save the current file.                           |
| Save as                 | `:w filename`              | Save the current file as "filename."             |
| Quit                    | `:q`                      | Quit Vim.                                          |
| Quit without saving     | `:q!`                     | Quit Vim without saving changes.                  |
| Save and quit           | `:wq`                     | Save changes and quit Vim.                        |
| **Visual Mode**         |                           |                                                    |
| Enter visual mode       | `v`                       | Enter visual mode to select text.                |
| Enter visual line mode  | `V`                       | Enter visual line mode to select lines.          |
| Enter visual block mode | `Ctrl+v`                  | Enter visual block mode to select rectangular blocks of text. |


## some more advance mouvments 

# Page and Line Movement Shortcuts in Vim

Vim provides a rich set of keyboard shortcuts for efficient page and line movement within a text document. Below is a table of these shortcuts:

| Shortcut               | Description                                       |
|------------------------|---------------------------------------------------|
| **Page Movement**      |                                                   |
| Page down              | `Ctrl+f` or `Space`                               |
| Page up                | `Ctrl+b` or `Ctrl+u`                             |
| Half a page down       | `Ctrl+d`                                          |
| Half a page up         | `Ctrl+u`                                          |
| Go to next page        | `Ctrl+d` or `Ctrl+f`                             |
| Go to previous page    | `Ctrl+u` or `Ctrl+b`                             |
| **Line Movement**      |                                                   |
| Move to beginning of line | `0` or `^`                                       |
| Move to end of line    | `$`                                               |
| Move to next line      | `j` or `↓`                                       |
| Move to previous line  | `k` or `↑`                                       |
| Move down by `n` lines | `n` + `j` or `n` + `↓`                           |
| Move up by `n` lines   | `n` + `k` or `n` + `↑`                           |
| Move to specific line  | `:<line_number>` or `G` + `g` + `:<line_number>` |
| **Scrolling**          |                                                   |
| Scroll the screen up   | `Ctrl+y`                                          |
| Scroll the screen down | `Ctrl+e`                                          |
| Center the screen      | `Ctrl+l`                                          |
| Move to the top        | `H`                                               |
| Move to the middle     | `M`                                               |
| Move to the bottom     | `L`                                               |
| **Jumping**            |                                                   |
| Jump to beginning of file | `gg`                                          |
| Jump to end of file    | `G`                                               |
| Jump to line in the middle | `M` + `G`                                      |
| Jump to last edit      | `'` + `.`                                         |

