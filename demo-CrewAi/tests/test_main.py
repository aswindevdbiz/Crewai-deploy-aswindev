# from fastapi.encoders import jsonable_encoder
# from fastapi.testclient import TestClient
# import pytest
# from main import app
# from models.agents import Agent
# from models.crews import Crew
# from models.projects import Project
# from models.tasks import Task
# from models.tools import Tool

# client = TestClient(app)

#  ##################################CREATE####################################
# # def test_create_new_tool(): 
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg") 
# #     response = client.post("/tool", json=jsonable_encoder(tool)) 
# #     assert response.status_code == 200 
# #     assert response.json()["status"] == True 
# #     assert "insert id" in response.json()["data"][0]

# # def test_create_new_agent():
# #     # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a new agent with the temporary tool ID
# #     agent = Agent(role="Developer", goal="Develop a new feature", backstory="Joined the team recently", tools=[str(tool_id)], verbose=False, image="test_image.jpg")
# #     response = client.post("/agent", json=jsonable_encoder(agent))

# #     print(response.json())
# #     assert response.status_code == 200 
# #     assert response.json()["status"] == True 
# #     assert "insert id" in response.json()["data"][0]

# # def test_create_new_task():
# #      # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary Agent
# #     agent = Agent(role="Developer", goal="Develop a new feature", backstory="Joined the team recently", tools=[str(tool_id)], verbose=False, image="test_image.jpg")
# #     response = client.post("/agent", json=jsonable_encoder(agent))
# #     agent_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary task
# #     task = Task(title="Task A", description="Description of Task A",outcome="Outcome of Task A", backstory="Backstory of Task A", agents=[str(agent_id)],tasks=[], image="test_image.jpg")
# #     response = client.post("/task", json=jsonable_encoder(task))
# #     task_id = response.json()["data"][0]["insert id"]

# #     task = Task(title="Task B", description="Description of Task A",outcome="Outcome of Task B", backstory="Backstory of Task B", agents=[str(agent_id)], tasks=[str(task_id)], image="test_image.jpg")
# #     response = client.post("/task", json=jsonable_encoder(task))

# #     print(response.json())
# #     assert response.status_code == 200 
# #     assert response.json()["status"] == True 
# #     assert "insert id" in response.json()["data"][0]

# # def test_create_new_crew():
# #      # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary Agent
# #     agent = Agent(role="Developer", goal="Develop a new feature", backstory="Joined the team recently", tools=[str(tool_id)], verbose=False, image="test_image.jpg")
# #     response = client.post("/agent", json=jsonable_encoder(agent))
# #     agent_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary task
# #     task = Task(title="Task A", description="Description of Task A",outcome="Outcome of Task A", backstory="Backstory of Task A", agents=[str(agent_id)],tasks=[], image="test_image.jpg")
# #     response = client.post("/task", json=jsonable_encoder(task))
# #     task_id = response.json()["data"][0]["insert id"]

# #     crew = Crew(name="Crew A",description="Description of Crew A",tasks=[str(task_id)],agents=[str(agent_id)],image="test_image.jpg")
# #     response = client.post("/crew", json=jsonable_encoder(crew))
# #     print(response.json())
# #     assert response.status_code == 200 
# #     assert response.json()["status"] == True 
# #     assert "insert id" in response.json()["data"][0]


# # def test_create_new_project():
# #     # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary Agent
# #     agent = Agent(role="Developer", goal="Develop a new feature", backstory="Joined the team recently", tools=[str(tool_id)], verbose=False, image="test_image.jpg")
# #     response = client.post("/agent", json=jsonable_encoder(agent))
# #     agent_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary task
# #     task = Task(title="Task A", description="Description of Task A",outcome="Outcome of Task A", backstory="Backstory of Task A", agents=[str(agent_id)],tasks=[], image="test_image.jpg")
# #     response = client.post("/task", json=jsonable_encoder(task))
# #     task_id = response.json()["data"][0]["insert id"]

# #     #Create a temporary crew
# #     crew = Crew(name="Crew A",description="Description of Crew A",tasks=[str(task_id)],agents=[str(agent_id)],image="test_image.jpg")
# #     response = client.post("/crew", json=jsonable_encoder(crew))
# #     crew_id = response.json()["data"][0]["insert id"]

# #     project = Project(name="Project A",description="Description of Project A",crews=[str(crew_id)])
# #     response = client.post("/project", json=jsonable_encoder(project))
# #     print(response.json())
# #     assert response.status_code == 200 
# #     assert response.json()["status"] == True 
# #     assert "insert id" in response.json()["data"][0]

# # ##################################READ####################################

# # def test_get_tools():
# #     # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Send a GET request to the /tools endpoint with a filter dictionary
# #     filter_dict = {"_id": tool_id}
# #     response = client.get("/tools", params=filter_dict)

# #     # Check that the response status code is 200
# #     assert response.status_code == 200

# #     # Check that the response data is correct
# #     data = response.json().get("data", [])
# #     if data:
# #         assert data[0]["name"] == "Test Tool"
# #         assert data[0]["description"] == "This is a test tool"
# #         assert data[0]["image"] == "test_image.jpg"
# #         assert data[0]["active"] == True

# # def test_get_agents():
# #     # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary agent
# #     agent = Agent(role="Test Agent", goal="Test goal", backstory="Test backstory", tools=[str(tool_id)], verbose=True, image="test_image.jpg", active=True)
# #     response = client.post("/agent", json=jsonable_encoder(agent))
# #     agent_id = response.json()["data"][0]["insert id"]

# #     # Send a GET request to the /agents endpoint with a filter dictionary
# #     filter_dict = {"_id": agent_id}
# #     response = client.get("/agents", params=filter_dict)

# #     # Check that the response status code is 200
# #     assert response.status_code == 200

# #     # Check that the response data is correct
# #     data = response.json().get("data", [])
# #     if data:
# #         assert data[0]["role"] == "Test Agent"
# #         assert data[0]["goal"] == "Test goal"
# #         assert data[0]["backstory"] == "Test backstory"
# #         assert data[0]["tools"] == [str(tool_id)]
# #         assert data[0]["verbose"] == True
# #         assert data[0]["image"] == "test_image.jpg"
# #         assert data[0]["active"] == True

# # def test_get_tasks():
# #     # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary agent
# #     agent = Agent(role="Test Agent", goal="Test goal", backstory="Test backstory", tools=[str(tool_id)], verbose=True, image="test_image.jpg", active=True)
# #     response = client.post("/agent", json=jsonable_encoder(agent))
# #     agent_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary task
# #     task = Task(title="Task A", description="Description of Task A",outcome="Outcome of Task A", backstory="Backstory of Task A", agents=[str(agent_id)],tasks=[], image="test_image.jpg")
# #     response = client.post("/task", json=jsonable_encoder(task))
# #     task_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary task
# #     task = Task(title="Test Task", description="Test description", outcome="Test outcome", agents=[str(agent_id)], tasks=[str(task_id)], image="test_image.jpg", active=True)
# #     response = client.post("/task", json=jsonable_encoder(task))
# #     task_id = response.json()["data"][0]["insert id"]

# #     # Send a GET request to the /tasks endpoint with a filter dictionary
# #     filter_dict = {"_id": task_id}
# #     response = client.get("/tasks", params=filter_dict)

# #     # Check that the response status code is 200
# #     assert response.status_code == 200

# #     # Check that the response data is correct
# #     data = response.json().get("data", [])
# #     if data:
# #         assert data[0]["title"] == "Test Task"
# #         assert data[0]["description"] == "Test description"
# #         assert data[0]["outcome"] == "Test outcome"
# #         assert data[0]["agents"] == [str(agent_id)]
# #         assert data[0]["tasks"] == [str(task_id)]
# #         assert data[0]["image"] == "test_image.jpg"
# #         assert data[0]["active"] == True

# # def test_get_crews():
# #     # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary Agent
# #     agent = Agent(role="Developer", goal="Develop a new feature", backstory="Joined the team recently", tools=[str(tool_id)], verbose=False, image="test_image.jpg")
# #     response = client.post("/agent", json=jsonable_encoder(agent))
# #     agent_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary task
# #     task = Task(title="Task A", description="Description of Task A",outcome="Outcome of Task A", backstory="Backstory of Task A", agents=[str(agent_id)],tasks=[], image="test_image.jpg")
# #     response = client.post("/task", json=jsonable_encoder(task))
# #     task_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary crew
# #     crew = Crew(name="Crew A",description="Description of Crew A",tasks=[str(task_id)],agents=[str(agent_id)],image="test_image.jpg")
# #     response = client.post("/crew", json=jsonable_encoder(crew))
# #     crew_id = response.json()["data"][0]["insert id"]

# #     # Send a GET request to the /crews endpoint with a filter dictionary
# #     filter_dict = {"_id": crew_id}
# #     response = client.get("/crews", params=filter_dict)

# #     # Check that the response status code is 200
# #     assert response.status_code == 200

# #     # Check that the response data is correct
# #     data = response.json().get("data", [])
# #     if data:
# #         assert data[0]["name"] == "Test Crew"
# #         assert data[0]["description"] == "Test description"
# #         assert data[0]["tasks"] == [str(task_id)]
# #         assert data[0]["agents"] == [str(agent_id)]
# #         assert data[0]["image"] == "test_image.jpg"
# #         assert data[0]["active"] == True

# # def test_read_projects():
# #     # Create a temporary tool
# #     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg", active=True)
# #     response = client.post("/tool", json=jsonable_encoder(tool))
# #     tool_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary Agent
# #     agent = Agent(role="Developer", goal="Develop a new feature", backstory="Joined the team recently", tools=[str(tool_id)], verbose=False, image="test_image.jpg")
# #     response = client.post("/agent", json=jsonable_encoder(agent))
# #     agent_id = response.json()["data"][0]["insert id"]

# #     # Create a temporary task
# #     task = Task(title="Task A", description="Description of Task A",outcome="Outcome of Task A", backstory="Backstory of Task A", agents=[str(agent_id)],tasks=[], image="test_image.jpg")
# #     response = client.post("/task", json=jsonable_encoder(task))
# #     task_id = response.json()["data"][0]["insert id"]

# #     #Create a temporary crew
# #     crew = Crew(name="Crew A",description="Description of Crew A",tasks=[str(task_id)],agents=[str(agent_id)],image="test_image.jpg")
# #     response = client.post("/crew", json=jsonable_encoder(crew))
# #     crew_id = response.json()["data"][0]["insert id"]

# #     project = Project(name="Project A",description="Description of Project A",crews=[str(crew_id)])
# #     response = client.post("/project", json=jsonable_encoder(project))
# #     project_id = response.json()["data"][0]["insert id"]
    
# #    # Send a GET request to the /projects endpoint with a filter dictionary
# #     filter_dict = {"_id": project_id}
# #     response = client.get("/crews", params=filter_dict)

# #     # Check that the response status code is 200
# #     assert response.status_code == 200

# #     # Check that the response data is correct
# #     data = response.json().get("data", [])
# #     if data:
# #         assert data[0]["name"] == "Test Crew"
# #         assert data[0]["description"] == "Test description"
# #         assert data[0]["crews"] == [str(crew_id)]
# #         assert data[0]["active"] == True

# # ##################################UPDATE####################################

# def test_update_tool():
#     # Create a temporary tool
#     tool = Tool(name="Test Tool", description="This is a test tool", image="test_image.jpg") 
#     response = client.post("/tool", json=jsonable_encoder(tool)) 
#     tool_id = response.json()["data"][0]["insert id"]

#     # Update the tool
#     updated_tool = Tool(name="Updated Tool", description="This is an updated tool", image="updated_test_image.jpg", active=False)
#     response = client.post(f"/tool/{tool_id}", json=jsonable_encoder(updated_tool))
#     assert response.status_code == 200
#     # assert response.json()["data"][0]["name"] == "Updated Tool"
#     # assert response.json()["data"][0]["description"] == "This is an updated tool"
#     # assert response.json()["data"][0]["image"] == "updated_test_image.jpg"
#     # assert response.json()["data"][0]["active"] == False
#     assert response.json()["status"] == True 
#     assert "Tool updated successfully." in  response.json()["data"][0]["message"]