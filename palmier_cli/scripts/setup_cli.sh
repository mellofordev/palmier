#!/bin/bash

echo '#!/usr/bin/env python3' > palmier
cat cli.py >> palmier
chmod +x palmier


mkdir -p ~/.local/bin
mv palmier ~/.local/bin/

echo "palmier cli setup is complete"