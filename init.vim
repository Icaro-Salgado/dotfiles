""" Misc
set encoding=utf-8
set backspace=indent,eol,start
let mapleader=" "

""" Visual
set number relativenumber
syntax enable
set scrolloff=7


""" Mainly for python
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set fileformat=unix


""" Vim Plug
call plug#begin('~/.vim/plugged')

Plug 'overcache/NeoSolarized'
Plug 'jiangmiao/auto-pairs'
Plug 'preservim/nerdtree'
Plug 'preservim/nerdcommenter'
Plug 'norcalli/nvim-colorizer.lua'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'sirver/ultisnips'

call plug#end()


""" For theming
set termguicolors
colorscheme NeoSolarized


""" Airline
let g:airline_theme='solarized'


""" Colorizer
lua require 'colorizer'.setup()


""" NERDCommenter
nmap <C-_> <Plug>NERDCommenterToggle
vmap <C-_> <Plug>NERDCommenterToggle<CR>gv


""" NERDTree
let NERDTreeQuitOnOpen=1
let g:NERDTreeMinimalUI=1

nmap <F2> :NERDTreeToggle<CR>


""" Tabs
let g:airline#extensions#tabline#enabled=1
let g:airline#extensions#tabline#fnamemode=':t'

nmap <leader>1 :bp<CR>
nmap <leader>2 :bn<CR>
nmap <C-w> :bd<CR>


""" Utilsnips
let g:UltiSnipsSnippetDirectories=[$HOME.'/.config/nvim/utisnips']
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpFowardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"
