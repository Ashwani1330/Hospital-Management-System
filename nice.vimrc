syntax on

set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set hidden
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set scrolloff=8

set signcolumn=yes
set colorcolumn=80
highlight ColorColoumn ctermbg=0 guibg=lightgray

autocmd FileType python map <buffer> <F9> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F9> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>
call plug#begin('~/.vim/plugged')

call plug#end()

