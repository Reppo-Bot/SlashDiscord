#!/bin/zsh
cd /home/josh/reppo/slash-reppo
rm -rf build dist
echo "Removed cached files\n"
echo y | pip uninstall SlashDiscord
echo "Removed old lib\n"
python -m build
echo "Built lib\n"
pip install dist/SlashDiscord-0.1.1-py3-none-any.whl
echo "Installed new lib\n"
