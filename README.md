# pYtera
Python module for interfacing with the Atera API in a simple way with a terrible name.
## How does it do
The entire thing is just a class so the design is very human.
```python
atera = Atera.AteraAPI("<YOUR_ATERA_API_KEY>")
```
and then run it's defs with things like
```python
atera.get_agents(page=5)
```
all functions have docstring so supported IDEs like Code and PyCharm can give documentation on how to use them.

Due to how the API works, agents are returned as a dict 

## Missing features
I'm going to be serious I've only added functions for each api call we've used so far, I will likely add them all at a later date but for now it's just what we got.
