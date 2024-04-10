from fastapi import FastAPI
from dotenv import load_dotenv
from .crud.create import CrudCreator
from .crud.read import CrudReader
from .crud.update import CrudUpdate

app = FastAPI()
load_dotenv()


""".........................TOOLS.........................."""

# Create Tool
@app.post("/tool")
async def create_new_tool(tool: dict):
    crudcreator = CrudCreator()
    return await crudcreator.create_tool(tool)

#Get Tools
@app.get("/tools")
async def read_tools(filter_dict: dict = None):
    crudreader = CrudReader()
    return await crudreader.get_tools(filter_dict)

#Update Tool
@app.post("/tool/{tool_id}")
async def update_tool(tool_id: str, tool: dict):
    crudupdate = CrudUpdate()
    return await crudupdate.update_tool(tool_id, tool)

""".........................AGENTS.........................."""

# Create Agent
@app.post("/agent")
async def create_new_agent(agent: dict):
    crudcreator = CrudCreator()
    return await crudcreator.create_agent(agent)

#Get Agents
@app.get("/agents")
async def read_agents(filter_dict: dict = None):
    crudreader = CrudReader()
    return await crudreader.get_agents(filter_dict)

#Update Agent
@app.post("/agent/{agent_id}")
async def update_agent(agent_id: str, agent: dict):
    crudupdate = CrudUpdate()
    return await crudupdate.update_agent(agent_id, agent)

""".........................TASKS.........................."""

#Create Task
@app.post("/task")
async def create_new_task(task: dict):
    crudcreator = CrudCreator()
    return await crudcreator.create_task(task)

#Get Tasks
@app.get("/tasks")
async def read_tasks(filter_dict: dict = None):
    crudreader = CrudReader()
    return await crudreader.get_tasks(filter_dict)

#Update Task
@app.post("/task/{task_id}")
async def update_task(task_id: str, task: dict):
    crudupdate = CrudUpdate()
    return await crudupdate.update_task(task_id,task)

""".........................CREWS.........................."""

#Create Crew
@app.post("/crew")
async def create_new_crew(crew: dict):
    crudcreator = CrudCreator()
    return await crudcreator.create_crew(crew)

#Get Crews
@app.get("/crews")
async def read_crews(filter_dict: dict = None):
    crudreader = CrudReader()
    return await crudreader.get_crews(filter_dict)

#Update Crew
@app.post("/crew/{crew_id}")
async def update_crew(crew_id: str, crew: dict):
    crudupdate = CrudUpdate()
    return await crudupdate.update_crew(crew_id,crew)

   