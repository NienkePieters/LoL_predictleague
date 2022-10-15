# LOL_predictleague
- Description: This project was created as a final project of the Le Wagon project. It is a tool for early identification of promising e-sports players (League of Legends), consisting of a Deep Learning model (Recurrent Neural Network) and Streamlit as front-end.
- Data Source: https://oracleselixir.com/
- Type: RNN model

```bash
git remote add origin git@github.com:NienkePieters/LOL_predictleague.git
git push -u origin master
git push -u origin --tags
```

# Install

Go to `https://github.com/NienkePieters/LOL_predictleague` to see the project, manage issues,
setup your ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:NienkePieters/LOL_predictleague.git
cd LOL_predictleague
pip install -r requirements.txt
make clean install test                # install and test
```
