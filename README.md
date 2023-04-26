# pYtera
Python module for interfacing with the Atera API in a simple way with a terrible name.
## How does it do
The entire thing is just a class so the design is very human.
```python
import Atera
atera = Atera.AteraAPI("<YOUR_ATERA_API_KEY>")
```
and then run it's defs with things like
```python
atera.get_agents(page=5)
```
all functions have docstrings so supported IDEs like VSCode and PyCharm can give documentation on how to use them.

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
It WILL print which page it's on and how many pages there are, unless you set echo=False
```python
# Returns as list of dicts, just like get_agents()
agentsList = atera.get_agents_all(echo=False)
```
### get_agent()
Just grabs a single agent via it's Atera AgentID or computer name.
It tells the difference based off if it's an int or str
```python
# Returns as a single dict, or a list of dicts if more than one computer has that name.
agent_id = atera.get_agent(14395)
agent_name = atera.get_agent("My_Computer")
```
### get_ticket()
Grabs 1 ticket by it's number
```python
# Returns as a single dict.
ticket = atera.get_ticket(28402)
```
### get_tickets()
Works like get_agents() but with tickets.
you can include the ```statustype``` arg if you want, which will only grab tickets with that status.
```python
# Returns as a list of dicts
tickets_5 = atera.get_tickets(page=5, amount 45)
tickets_1 = atera.get_tickets()
tickets_closed = atera.gettickets(statustype="Closed")
```
### get_tickets_all()
For the insane, a method to pull EVERY ticket in Atera.
I'd recommend against it, but I'm not you.
```python
TooManyTickets = atera.get_tickets_all()
