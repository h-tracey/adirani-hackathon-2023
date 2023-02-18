
cat requirements.txt >> .devcontainer/requirements.txt

pip3 install --no-cache-dir -r .devcontainer/requirements.txt \
  && rm .devcontainer/requirements.txt