. server-venv/bin/activate
nohup python3 -u Main.py &
nohup python3 -u UpdateDB.py &
tail -f nohup.out
