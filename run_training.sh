#!/bin/bash
#source activate ai
python -m rasa_nlu.train -c nlu_config.yml -d nlu_data/nlu_data.md --path projects --verbose
