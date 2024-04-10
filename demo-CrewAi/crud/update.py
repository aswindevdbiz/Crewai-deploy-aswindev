from bson import ObjectId
from ..models.tools import Tool
from ..models.agents import Agent
from ..models.tasks import Task
from ..models.crews import Crew
from ..utils.mongodb import open_connection, close_connection

class CrudUpdate:
    @staticmethod
    async def update_tool(tool_id: str, tool: Tool):
        try:
            db = open_connection()
            collection = db["Tool Structure"]

            # Update the tool in the database
            tool_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(tool_id)},
                {"$set": tool},
                upsert=False
            )
            if tool_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Tool updated successfully."}]}
        except Exception as e:
            return {"status": False, "data": {"error": str(e)}}
        finally:
            close_connection()

    @staticmethod
    async def update_agent(agent_id: str, agent: Agent):
        try:
            db =open_connection()
            collection = db["Agent"]
            tool_collection = db["Tool Structure"]

            # Check if all the tools exist in the Tool Structure collection
            tool_ids = [ObjectId(tool_id) for tool_id in agent["tools"]]
            tool_docs = tool_collection.find({"_id": {"$in": tool_ids}})
            if len(list(tool_docs)) != len(tool_ids):
                return {"status": False, "data": [{"error": "One or more tools not found in the Tool Structure collection."}]}
            
            # Update the agent in the database
            agent_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(agent_id)},
                {"$set": agent},
                upsert=False
            )
            if agent_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Agent updated successfully."}]}

        except Exception as e:
            return {"status": False, "data": {"error": str(e)}}  
        finally:
            close_connection()      

     
    @staticmethod
    async def update_task(task_id: str, task: Task):
        try:
            db = open_connection()
            task_collection = db["Task"]
            agent_collection = db["Agent"]

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

            # Update the task in the database
            task_to_be_updated = task_collection.find_one_and_update(
                {"_id": ObjectId(task_id)},
                {"$set": task},
                upsert=False
            )
            if task_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Task updated successfully."}]}

        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()

    @staticmethod
    async def update_crew(crew_id: str, crew: Crew):
        try:
            db =open_connection()
            collection = db["Crew"]
            task_collection = db["Task"]

            # Check if all the tasks exist in the Task collection
            task_ids = [ObjectId(task_id) for task_id in crew["tasks"]]
            task_docs = task_collection.find({"_id": {"$in": task_ids}})
            if len(list(task_docs)) != len(task_ids):
                return {"status": False, "data": [{"error": "One or more tasks not found in the Task collection."}]}

            # Update the agent in the database
            crew_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(crew_id)},
                {"$set": crew},
                upsert=False
            )
            if crew_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Crew updated successfully."}]}

        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}  
        finally:
            close_connection()         