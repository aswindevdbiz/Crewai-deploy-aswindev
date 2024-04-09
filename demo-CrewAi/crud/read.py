from utils.mongodb import open_connection, close_connection

class CrudReader:
    @staticmethod
    async def get_tools(filter_dict: dict = None):
        try:
            db = open_connection()
            collection = db["Tool Structure"]
            if filter_dict is None:
                filter_dict = {}

            tools = []
            docs = collection.find(filter_dict, {"_id": 1, "name": 1, "description": 1, "image": 1, "active": 1})
            for doc in docs:
                if doc["active"]:
                    doc["_id"] = str(doc["_id"])
                    tools.append(doc)
            return {"status": True, "tools": tools}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()


    @staticmethod
    async def get_agents(filter_dict: dict = None):
        try:
            db = open_connection()
            collection = db["Agent"]
            if filter_dict is None:
                filter_dict = {}

            agents = []
            docs = collection.find(filter_dict, {"_id": 1, "role": 1, "goal": 1, "backstory": 1, "tools": 1, "verbose": 1, "image": 1, "active": 1})
            for doc in docs:
                if doc["active"]:
                    doc["_id"] = str(doc["_id"])
                    agents.append(doc)
            return {"status": True, "agents": agents}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()

    @staticmethod
    async def get_tasks(filter_dict: dict = None):
        try:
            db = open_connection()
            collection = db["Task"]
            if filter_dict is None:
                filter_dict = {}

            tasks = []
            docs = collection.find(filter_dict, {"_id": 1, "title": 1, "description": 1, "outcome": 1, "agents": 1, "tasks": 1, "active": 1, "image": 1})
            for doc in docs:
                if doc["active"]:
                    doc["_id"] = str(doc["_id"])
                    tasks.append(doc)
            return {"status": True, "tasks": tasks}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()  

    @staticmethod
    async def get_crews(filter_dict: dict = None):
        try:
            db = open_connection()
            collection = db["Crew"]
            if filter_dict is None:
                filter_dict = {}

            crews = []
            docs = collection.find(filter_dict, {"_id": 1, "name": 1, "description": 1, "tasks": 1, "active": 1, "image": 1})
            for doc in docs:
                if doc["active"]:
                    doc["_id"] = str(doc["_id"])
                    crews.append(doc)
            return {"status": True, "crews": crews}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()                 
