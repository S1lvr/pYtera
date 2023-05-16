import requests
import urllib3
import json


class AteraAPI(object):
    """
    Initial Class for using Atera API
    """

    def __init__(self, key: str):
        """
        Init for AteraAPI
        :param key: Atera API Key
        """
        self._api_key = key
        self.api_uri = "https://app.atera.com/api/v3/"

    def get(self, endpoint: str):
        """
        Uses "GET" method from REST API to make a request to Atera\n
        See https://app.atera.com/apidocs for more info
        Args:
            endpoint: the section of URL that goes after '/v3/' in the atera api documentation

        Returns: whatever you asked for.

        """
        http = urllib3.PoolManager()
        url = self.api_uri + endpoint
        headers = {'X-API-KEY': self._api_key}
        response = http.request('GET', url, headers=headers)
        res = response.data.decode('utf-8')
        return json.loads(res)

    def post(self, endpoint: str, data: dict):
        """
        CREATE SOMETHING, used for Tickets mostly.\n
        See https://app.atera.com/apidocs for more info
        Check
        Args:
            endpoint: the section of URL that goes after '/v3/' in the atera api documentation
            data: what to post, please include as json

        Returns:

        """
        http = urllib3.PoolManager()
        url = self.api_uri + endpoint
        headers = {'Content-Type': 'application/json', 'X-API-KEY': self._api_key}
        encoded_data = json.dumps(data).encode('utf-8')
        response = http.request('POST', url, headers=headers, body=encoded_data)
        data = response.data.decode('utf-8')

    def put(self, endpoint: str, data):
        """
        Kind of useless? Post does the same thing in Atera's API\n
        See https://app.atera.com/apidocs for more info
        Args:
            endpoint:
            data:
        """
        headers = {'X-Api-Key': self._api_key, 'Content-Type': 'application/json'}
        url = self.api_uri + endpoint
        requests.put(url, headers=headers, data=json.dumps(data))

    def delete(self, endpoint: str):
        """
        Sends delete command. Probably never use.\n
        See https://app.atera.com/apidocs for more info
        Args:
            endpoint:
        """
        headers = {'X-Api-Key': self._api_key}
        url = self.api_uri + endpoint
        requests.delete(url, headers=headers)

    def get_customerlist(self, page=1, amount=50):
        """
        Get list of Customers
        :return: Customers as list of dicts
        """
        return self.get(f"customers?page={page}&itemsInPage={amount}")

    def get_customerlist_all(self):
        """
        grabs literally all customers
        :return: list of dicts
        """
        custs = self.get_customerlist()
        output = [custs['items']]
        i = 1
        print("grabbed first page")
        while int(custs['page']) < int(custs['totalPages']):
            i += 1

            custs = self.get_customerlist(page=i)
            output.append(custs['items'])
        return [item for sublist in output for item in sublist]

    def get_agents(self, page=1, amount=50):
        """
        Get list of agents
        :param page: Page #, defaults to 1
        :param amount: Number per page, defaults to 50
        :return: Returns list of agents as json
        """
        return self.get(f"agents?page={page}&itemsInPage={amount}")

    def get_agents_all(self, echo=True):
        """
                Grabs all agents, looping through pages
                :return: agents as dict
                """
        agents = self.get_agents(page=1, amount=50)
        if echo:
            print(f"Attempt 1 to pull page {agents['page']} of {agents['totalPages']}")
        output = [agents['items']]
        i = 1
        while int(agents['page']) < int(agents['totalPages']):
            i += 1
            agents = self.get_agents(page=i, amount=50)
            if echo:
                print(f"Attempt {i} to pull page {agents['page']} of {agents['totalPages']}")
            output.append(agents['items'])
        return [item for sublist in output for item in sublist]

    def get_agent(self, agentid):
        """
        Grabs specific agent info
        :param agentid: AgentID of computer or Computer Name.\nAn int will be treated as AgentID, a str will be treated as computer name.
        :return: Agent Info as Dict
        """
        if type(agentid) == int:
            return self.get(f"agents/{agentid}")
        if type(agentid) == str:
            return self.get(f"agents/machine/{agentid}")

    def get_ticket(self, ticketId):
        """
        Returns specific ticket.
        :param ticketId: The ID of the ticket
        :return: Ticket as Dict
        """
        return self.get(f"tickets/{ticketId}")

    def get_tickets(self, statustype=None, page=1, amount=50):
        """
        Get list of agents
        :param statustype: The type of status of the ticket
        :param page: Page #, defaults to 1
        :param amount: Number per page, defaults to 50
        :return: Returns list of agents as json
        """
        if statustype:
            return self._get(f"tickets?page={page}&itemsInPage={amount}&ticketStatus={statustype}")
        else:
            return self._get(f"tickets?page={page}&itemsInPage={amount}")

    def get_tickets_all(self, status, echo=False):
        """
        Grabs all tickets, looping through pages\nI don't recommend this one as much.\nYou're better off just making a loop with get_tickets()
        :return: tickets as list of dict
        """
        if status:
            tickets = self.get_tickets(status)
        else:
            tickets = self.get_tickets(None)
        if echo:
            print(f"Attempt 1 to pull page {tickets['page']} of {tickets['totalPages']}")
        output = [tickets['items']]
        i = 1
        while int(tickets['page']) < int(tickets['totalPages']):
            i += 1
            if status:
                tickets = self.get_tickets(status, page=i)
            else:
                tickets = self.get_tickets(page=i)
            if echo:
                print(f"Attempt {i} to pull page {tickets['page']} of {tickets['totalPages']}")
            output.append(tickets['items'])
        return [item for sublist in output for item in sublist]
