cd ~/github/SlashDiscord
export $(cat .env)
python -m twine upload dist/* --verbose
unset $(grep -v '^#' .env | sed -E 's/(.*)=.*/\1/' | xargs)
cd -
