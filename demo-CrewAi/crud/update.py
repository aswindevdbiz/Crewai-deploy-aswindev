from bson import ObjectId
from ..models.tools import Tool
from ..models.agents import Agent
from ..models.tasks import Task
from ..models.crews import Crew
from ..models.projects import Project
from ..utils.mongodb import open_connection, close_connection

class CrudUpdate:
    @staticmethod
    async def update_tool(tool_id: str, tool: Tool):
        try:
            db = open_connection()
            collection = db["Tool Structure"]

            # Check if the tool name is being changed to an existing name
            updated_tool_name = tool.get("name", None)
            if updated_tool_name:
                existing_tool = collection.find_one({"name": updated_tool_name})
                if existing_tool and str(existing_tool["_id"]) != tool_id:
                    return {"status": False, "data": [{"error": "Tool with the same name already exists."}]}

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
            db = open_connection()
            collection = db["Agent"]

            # Check if the agent role is being changed to an existing role
            updated_agent_role = agent.get("role", None)
            if updated_agent_role:
                existing_agent = collection.find_one({"role": updated_agent_role})
                if existing_agent and str(existing_agent["_id"]) != agent_id:
                    return {"status": False, "data": [{"error": "Agent with the same role already exists."}]}

            # Check if all the tools exist in the Tool Structure collection
            tool_collection = db["Tool Structure"]
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

            # Check if the task title is being changed to an existing title
            updated_task_title = task.get("title", None)
            if updated_task_title:
                existing_task = task_collection.find_one({"title": updated_task_title})
                if existing_task and str(existing_task["_id"]) != task_id:
                    return {"status": False, "data": [{"error": "Task with the same title already exists."}]}

            # Check if all the agents exist in the Agent collection
            agent_collection = db["Agent"]
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
            db = open_connection()
            collection = db["Crew"]

            # Check if the crew name is being changed to an existing name
            updated_crew_name = crew.get("name", None)
            if updated_crew_name:
                existing_crew = collection.find_one({"name": updated_crew_name})
                if existing_crew and str(existing_crew["_id"]) != crew_id:
                    return {"status": False, "data": [{"error": "Crew with the same name already exists."}]}

            # Check if all the tasks exist in the Task collection
            task_collection = db["Task"]
            task_ids = [ObjectId(task_id) for task_id in crew["tasks"]]
            task_docs = task_collection.find({"_id": {"$in": task_ids}})
            if len(list(task_docs)) != len(task_ids):
                return {"status": False, "data": [{"error": "One or more tasks not found in the Task collection."}]}

            # Check if all the agents exist in the Agent collection
            agent_collection = db["Agent"]
            agent_ids = [ObjectId(agent_id) for agent_id in crew["agents"]]
            agent_docs = agent_collection.find({"_id": {"$in": agent_ids}})
            if len(list(agent_docs)) != len(agent_ids):
                return {"status": False, "data": [{"error": "One or more agents not found in the Agent collection."}]}

            # Update the crew in the database
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

    @staticmethod
    async def update_project(project_id: str, project: Project):
        try:
            db = open_connection()
            collection = db["Project"]

            # Check if the project name is being changed to an existing name
            updated_project_name = project.get("name", None)
            if updated_project_name:
                existing_project = collection.find_one({"name": updated_project_name})
                if existing_project and str(existing_project["_id"]) != project_id:
                    return {"status": False, "data": [{"error": "Project with the same name already exists."}]}

            # Check if all the crews exist in the Crew collection
            crew_collection = db["Crew"]
            crew_ids = [ObjectId(crew_id) for crew_id in project["crews"]]
            crew_docs = crew_collection.find({"_id": {"$in": crew_ids}})
            if len(list(crew_docs)) != len(crew_ids):
                return {"status": False, "data": [{"error": "One or more crews not found in the Crew collection."}]}

            # Update the project in the database
            project_to_be_updated = collection.find_one_and_update(
                {"_id": ObjectId(project_id)},
                {"$set": project},
                upsert=False
            )
            if project_to_be_updated == None:
                return {"status":False, "data": [{"message":"Could'nt find the match"}]}
            else:
                return {"status": True, "data": [{"message": "Project updated successfully."}]}
        except Exception as e:
            return {"status": False, "data": {"error": str(e)}}
        finally:
            close_connection()          