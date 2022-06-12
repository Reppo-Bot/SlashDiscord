#!/bin/zsh
cd /home/josh/github/SlashDiscord
rm -rf build dist
echo "Removed cached files\n"
echo y | pip uninstall SlashDiscord
echo "Removed old lib\n"
python -m build
echo "Built lib\n"
pip install dist/SlashDiscord-*.whl
echo "Installed new lib\n"
