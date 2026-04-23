#!/usr/bin/env bash
set -euo pipefail

sudo apt-get update
sudo apt-get install -y --no-install-recommends \
  ffmpeg \
  libcairo2-dev \
  libpango1.0-dev \
  pkg-config \
  texlive-latex-base \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-plain-generic \
  dvisvgm

python -m pip install --upgrade pip
pip install -r requirements.txt
