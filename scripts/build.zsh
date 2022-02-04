#!/bin/zsh
cd /home/josh/reppo/slash-reppo
rm -rf build dist slashReppo.egg-info slashReppo/__pycache__
echo "Removed cached files\n"
echo y | pip uninstall slashReppo
echo "Removed old lib\n"
python setup.py bdist_wheel
echo "Built lib\n"
pip install dist/slashReppo-0.0.1-py3-none-any.whl
echo "Installed new lib\n"
