import requests

class BoardApi:

    base_url = "https://api.trello.com/1"
    token = "ATTA9bd19d7ff71d070f361328c8072ed60d18121dc452fff1ab218dd8794dc16a2f22DAD681"
    api_key = "***REMOVED***"

    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        path = f"{self.base_url}/organizations/{org_id}/boards"
        params = {
            "key": self.api_key,
            "token":self.token
                  }

        resp = requests.get(path, params=params)

        return resp.json()
    
    def create_board(self, org_id: str, name, default_lists = True):
        body = {
        "defaultLists": default_lists,
        "name": name,
        "token": self.token,
        "idOrganization": org_id }
        
        path = f"{self.base_url}/boards"
        params = {
            "key": self.api_key,
            "token":self.token
                  }

        resp = requests.post(path, json=body, params=params)

        return resp.json()
    
    def delete_board_by_id(self, board_id: str) -> dict:
        path = f"{self.base_url}/boards/{board_id}"
        params = {
            "key": self.api_key,
            "token":self.token
                  }

        resp = requests.delete(path, params=params)

        return resp.json()