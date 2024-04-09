from bson import ObjectId
from models.tools import Tool
from models.agents import Agent
from models.tasks import Task
from models.crews import Crew
from utils.mongodb import open_connection, close_connection

class CrudCreator:

    @staticmethod
    async def create_tool(tool: Tool):
        try:
            db = open_connection()
            collection = db["Tool Structure"]

            if tool["name"] == "" or tool["description"] == "":
                return {"status": False, "data": [{"error":"name and description is Mandatory."}]}
            
            tool["active"] = True
            tool_id = collection.insert_one(tool).inserted_id
            return {"status": True, "data": [{"insert id": str(tool_id)}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()


    @staticmethod
    async def create_agent(agent: Agent):
        try:
            db = open_connection()
            collection = db["Agent"]
            tool_collection = db["Tool Structure"]
            agent["active"] = True

            if agent["role"] == "" or agent["goal"] == "" or agent["backstory"] == "" or agent["tools"] == "":
               return {"status": False, "data": [{"error":"role, goal, backstory, tools is Mandatory."}]}
            
            # Check if all the tools exist in the Tool Structure collection
            tool_ids = [ObjectId(tool_id) for tool_id in agent["tools"]]
            tool_docs = tool_collection.find({"_id": {"$in": tool_ids}})
            if len(list(tool_docs)) != len(tool_ids):
                return {"status": False, "data": [{"error": "One or more tools not found in the Tool Structure collection."}]}

            agent_id = collection.insert_one(agent).inserted_id
            return {"status": True, "data": [{"insert id": str(agent_id)}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()

    @staticmethod
    async def create_task(task: Task):
        try:
            db = open_connection()
            task_collection = db["Task"]
            agent_collection = db["Agent"]
            task["active"] = True

            if task["title"] == "" or task["description"] == "" or task["outcome"] == "" or task["agents"] == "" or task["tasks"] == "":
               return {"status": False, "data": [{"error":"title, description,outcome, agents, tasks is Mandatory."}]}

            # Check if all the agents exist in the Agent collection
            agent_ids = [ObjectId(agent_id) for agent_id in task["agents"]]
            agent_docs = agent_collection.find({"_id": {"$in": agent_ids}})
            if len(list(agent_docs)) != len(agent_ids):
                return {"status": False, "data": [{"error": "One or more agents not found in the Agent collection."}]}
            
            # Check if all the tasks exist in the Task collection
            task_ids = [ObjectId(task_id) for task_id in task["tasks"]]
            task_docs = task_collection.find({"_id": {"$in": task_ids}})
            if len(list(task_docs)) != len(task_ids):
                return {"status": False, "data": [{"error": "One or more tasks not found in the Task collection."}]}

            task_id = task_collection.insert_one(task).inserted_id
            return {"status": True, "data": [{"insert id": str(task_id)}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()

    @staticmethod
    async def create_crew(crew: Crew):
        try:
            db = open_connection()
            collection = db["Crew"]
            task_collection = db["Task"]
            crew["active"] = True

            if crew["name"] == "" or crew["description"] == "" or crew["tasks"] == "":
                return {"status": False, "data": [{"error":"name, description, tasks is Mandatory."}]}

            # Check if all the tasks exist in the Task collection
            task_ids = [ObjectId(task_id) for task_id in crew["tasks"]]
            task_docs = task_collection.find({"_id": {"$in": task_ids}})
            if len(list(task_docs)) != len(task_ids):
                return {"status": False, "data": [{"error": "One or more tasks not found in the Task collection."}]}

            crew_id = collection.insert_one(crew).inserted_id
            return {"status": True, "data": [{"insert id": str(crew_id)}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()