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
all functions have docstrings so supported IDEs like Code and PyCharm can give documentation on how to use them.

Due to how the API works, agents are returned as a dict 

## Missing features
I'm going to be serious I've only added functions for each api call we've used so far, I will likely add them all at a later date but for now it's just what we got.
## Existing features
Anyway here's what we have right now.
### get_agents()
Grabs a list of agents, works just like the API documentation gives with little to no changes.
Defaults to "page=1" and "amount=50"
```python
# Returns as list of dicts (each agent is a dict)
agentsList1 = atera.get_agents(page=1, amount=50)
```
### get_agents_all()
Returns all agents it can find, by looping through each page it can find.
It WILL print which page it's on and how many pages there are. so be aware of that.
```python
# Returns as list of dicts, just like get_agents()
agentsList = atera.get_agents_all()
```
### get_agent()
Just grabs a single agent via it's Atera AgentID.
```python
# Returns as a single dict.
agent = atera.get_agent("<AgentID>")
```
