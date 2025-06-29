## KING JERY
```
apt update && apt upgrade -y
```
```
git clone https://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@github.com/naelku/jery
```
```
cd jery && screen -S jery
```
```
bash installnode.sh && apt install python3.10-venv
```
```
python3 -m venv jery && source jery/bin/activate
```
```
pip3 install -r requirements.txt
```
```
cp sample.env .env && nano .env
```
```
python3 -m PyroUbot
```
