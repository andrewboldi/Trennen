# Learn

- This directory contains all the machine learning files
- v0 was a failure since point clouds suck for machine learning representation

# General Metholodgy
1. Convert to xyz. Xyz is the best way to express molecules right now.
2. Find how to represent molecules.
	- One idea is to have the number of protons and neutrons at the nuclei. (distance between atoms already tells us electron information)
	- In the nucelus, maybe we should randomize positioon of nucleons? (we'll start by assuming they are all at the center)

# Oprtical Rotation
          _________
         |  black  | 
 Input ->|   box   | -> output
         |         | 
          _________

          _________
         |  black  | 
 inchi ->|   box   | -> direction +/-
         |         | 
          _________

          _________      _________
         |         |    |  black  | 
 inchi ->|   xyz   | -> |   box   | -> direction +/-
         |         |    |         | 
          _________      _________
	  

File Format:
- proton count.
