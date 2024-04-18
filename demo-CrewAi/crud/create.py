from bson import ObjectId
from ..models.agents import Agent
from ..models.tools import Tool
from ..models.tasks import Task
from ..models.crews import Crew
from ..models.projects import Project
from ..utils.mongodb import open_connection, close_connection

class CrudCreator:

    @staticmethod
    async def create_tool(tool: Tool):
        try:
            db = open_connection()
            collection = db["Tool Structure"]
            
            # Checking the mandatory fields are there.
            if tool["name"] == "" or tool["description"] == "":
                return {"status": False, "data": [{"error":"name and description is Mandatory."}]}

            # Checking name duplication.
            existing_tool = collection.find_one({"name": tool["name"]})

            if existing_tool:
                return {"status": False, "data": [{"error": "Tool with the same name already exists."}]}

            #Making the tool field to default true.
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

            #Checking whether the mandatory fields are there.
            if agent["role"] == "" or agent["goal"] == "" or agent["backstory"] == "" or agent["tools"] == "":
                return {"status": False, "data": [{"error":"role, goal, backstory, tools is Mandatory."}]}

            # Check if all the tools exist in the Tool Structure collection
            tool_ids = [ObjectId(tool_id) for tool_id in agent["tools"]]
            tool_docs = tool_collection.find({"_id": {"$in": tool_ids}})
            if len(list(tool_docs)) != len(tool_ids):
                return {"status": False, "data": [{"error": "One or more tools not found in the Tool Structure collection."}]}

            # Check for duplicate role in the Agent collection
            existing_agent = collection.find_one({"role": agent["role"]})

            if existing_agent:
                return {"status": False, "data": [{"error": "Agent with the same role already exists."}]}

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
            
            # Check for duplicate title in the Task collection
            existing_task = task_collection.find_one({"title": task["title"]})

            if existing_task:
             return {"status": False, "data": [{"error": "Task with the same title already exists."}]}

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
            agent_collection = db["Agent"]

            crew["active"] = True

            if crew["name"] == "" or crew["description"] == "" or crew["tasks"] == "":
                return {"status": False, "data": [{"error":"name, description, tasks is Mandatory."}]}

            # Check if all the tasks exist in the Task collection
            task_ids = [ObjectId(task_id) for task_id in crew["tasks"]]
            task_docs = task_collection.find({"_id": {"$in": task_ids}})
            if len(list(task_docs)) != len(task_ids):
                return {"status": False, "data": [{"error": "One or more tasks not found in the Task collection."}]}

            # Check if all the agents exist in the Agent collection
            agent_ids = [ObjectId(agent_id) for agent_id in crew["agents"]]
            agent_docs = agent_collection.find({"_id": {"$in": agent_ids}})
            if len(list(agent_docs)) != len(agent_ids):
                return {"status": False, "data": [{"error": "One or more agents not found in the Agent collection."}]}

            # Check for duplicate name in the Crew collection
            existing_crew = collection.find_one({"name": crew["name"]})

            if existing_crew:
                return {"status": False, "data": [{"error": "Crew with the same name already exists."}]}

            crew_id = collection.insert_one(crew).inserted_id
            return {"status": True, "data": [{"insert id": str(crew_id)}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()

    @staticmethod
    async def create_project(project: Project):
        try:
            db = open_connection()
            collection = db["Project"]
            crew_collection = db["Crew"]

            if project["name"] == "" or project["description"] == "" or project["crews"] == "":
                return {"status": False, "data": [{"error":"name, description, crews is Mandatory."}]}

            # Check if all the crews exist in the Crew collection
            crew_ids = [ObjectId(crew_id) for crew_id in project["crews"]]
            crew_docs = crew_collection.find({"_id": {"$in": crew_ids}})
            if len(list(crew_docs)) != len(crew_ids):
                return {"status": False, "data": [{"error": "One or more crews not found in the Crew collection."}]}

            # Check for duplicate name in the Project collection
            existing_project = collection.find_one({"name": project["name"]})

            if existing_project:
                return {"status": False, "data": [{"error": "Project with the same name already exists."}]}

            project_id = collection.insert_one(project).inserted_id
            return {"status": True, "data": [{"insert id": str(project_id)}]}
        except Exception as e:
            return {"status": False, "data": [{"error": str(e)}]}
        finally:
            close_connection()        