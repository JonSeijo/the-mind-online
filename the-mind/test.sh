#!/bin/bash

python -m unittest -v
if [[ $1 == all ]]; then
    pyre check
fi