from google import genai
import subprocess
import requests

# 1. Setup Client
client = genai.Client(api_key="AIzaSyB_ijmRo4PtbkX36eVgUMWAGA1vsvnVvXM")
MODEL_ID = "gemini-2.5-flash" 

# 2. Define the local function
def execute_command(command: str):
    """Executes a shell command and returns the output."""
    try:
        print(f"--- Executing: {command} ---")
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout or "Success (no output)"
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"
    
def getBitcoinPrice():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    
    try:
        # 1. Attempt the network request
        response = requests.get(url, timeout=10)
        
        # 2. Raise an error if the HTTP status is not 200 (OK)
        # This catches 404 (Not Found) or 500 (Server Error)
        response.raise_for_status()
        
        # 3. Parse JSON
        data = response.json()
        
        # 4. Access the specific value
        price = data['bitcoin']['usd']
        print(f"Current Bitcoin Price: ${price}")
        return price

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the internet or the server.")
    except KeyError:
        print("Error: The API response format has changed.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

# 3. Define the Tool
# The SDK can often derive the declaration from the function's docstring automatically

def run_agent():
    instructions = (
        "You are a assistant, which can generate answer to anyhting like general LLM."
        "You have access to your exixting knowledge from whihc u can answer simple questions"
        "also u have access to couple of tools like 'execute_command' which can execute any shell command and return the output, and 'getBitcoinPrice' which can fetch the current price of Bitcoin. "
        "You are a coding assistant that creates local files via shell commands. "
        "Always use 'cat << 'EOF' > filename' for multi-line files to avoid escape character issues. "
        "Verify file creation with 'ls'"
        "You need to create all required html css and js files to build the project, after completion open html file in local host in browser, will show the expected output. "
    )

    user_query = input("What would you like me to build? (e.g., 'Create a basic Tic Tac Toe game with HTML/CSS/JS'): ")

    
    # Initialize Chat
    chat = client.chats.create(
        model=MODEL_ID,
        config={
            'tools': [execute_command, getBitcoinPrice],
            'system_instruction': instructions 
        }
    )

    # Initial request
    response = chat.send_message(user_query)

    # 4. The Execution Loop (The "Brain")
    # We loop as long as Gemini wants to call a tool

    while response.candidates[0].content.parts[0].function_call:
        # Loop through parts to find the function call
        for part in response.candidates[0].content.parts:
            if part.function_call:
                call = part.function_call
                if call.name == "execute_command":
                    tool_output = execute_command(call.args['command'])
                elif call.name == "getBitcoinPrice":
                    tool_output = getBitcoinPrice()
            
            # Send the result back to Gemini
            response = chat.send_message(
                genai.types.Part.from_function_response(
                    name=call.name,
                    response={'result': tool_output}
                )
            )
    
    print("\n--- Agent Finished ---")
    print(response.text)

if __name__ == "__main__":
    run_agent()