git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch; bash install-deps;
./install.sh
source ~/.zshrc

# update common package to latest
luarocks install torch
luarocks install nn
luarocks install graph

luarocks install torchnet

luarocks install optnet
luarocks install iterm
