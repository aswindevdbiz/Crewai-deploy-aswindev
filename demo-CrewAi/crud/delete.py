from bson import ObjectId
from utils.mongodb import open_connection, close_connection

class CrudDelete:
    @staticmethod
    async def delete_tool(tool_id: str):
        try:
            db = open_connection()
            collection = db["Tool Structure"]

            # Soft delete the tool by setting isactive to False
            tool_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(tool_id)},
                {"$set": {"active": False}},
                upsert=False
            )
            if tool_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Tool deleted successfully."}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()

    @staticmethod
    async def delete_agent(agent_id: str):
        try:
            db = open_connection()
            collection = db["Agent"]

            # Soft delete the agent by setting isactive to False
            agent_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(agent_id)},
                {"$set": {"active": False}},
                upsert=False
            )
            if agent_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Agent deleted successfully."}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()            

    @staticmethod
    async def delete_task(task_id: str):
        try:
            db =open_connection()
            collection = db["Task"]

            # Soft delete the task by setting isactive to False
            task_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(task_id)},
                {"$set": {"active": False}},
                upsert=False
            )
            if task_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Task deleted successfully."}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()             

    @staticmethod
    async def delete_crew(crew_id: str):
        try:
            db = open_connection()
            collection = db["Crew"]

            # Soft delete the crew by setting isactive to False
            crew_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(crew_id)},
                {"$set": {"active": False}},
                upsert=False
            )
            if crew_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Crew deleted successfully."}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()          