from fastapi import FastAPI, File, UploadFile
from secrets import token_hex
from dotenv import load_dotenv
from crud.create import CrudCreator
from crud.read import CrudReader
from crud.update import CrudUpdate
from crud.delete import CrudDelete

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

#Delete Tool
@app.delete("/tool/{tool_id}")
async def delete_tool(tool_id: str):
    cruddelete = CrudDelete()
    return await cruddelete.delete_tool(tool_id)

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

#Delete Agent
@app.delete("/agent/{agent_id}")
async def delete_agent(agent_id: str):
    cruddelete = CrudDelete()
    return await cruddelete.delete_agent(agent_id)

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

#Delete Task
@app.delete("/task/{task_id}")
async def delete_task(task_id: str):
    cruddelete = CrudDelete()
    return await cruddelete.delete_task(task_id)

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

#Delete Crew
@app.delete("/crew/{crew_id}")
async def delete_crew(crew_id: str):
    cruddelete = CrudDelete()
    return await cruddelete.delete_crew(crew_id)



# @app.post("/upload")
# async def upload(file:UploadFile = File(...)):
#     file_ext = file.filename.split(".").pop()  #Eg :- png, jpeg
#     file_name = token_hex(10)
#     file_path = f"{file_name}.{file_ext}"
#     with open(file_path,"wb") as f:
#         content = await file.read()
#         f.write(content)
#     return {"success":True, "file_path": file_path, "message": "File uploaded successfully"}    