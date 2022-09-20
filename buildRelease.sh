#!/bin/bash
(cd ../../; python2 ./generator.pyc hs_kostalInverter2ndGen utf-8)
markdown2 --extras tables,fenced-code-blocks,strike,target-blank-links doc/log14460.md > release/log14460.html
(cd release; zip -r 14460_hs_kostalInverter2ndGen.hslz *)
