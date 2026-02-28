from fastmcp import FastMCP
import random
import os
import json


mcp = FastMCP(name='Remote server')


@mcp.tool
def add_numbers(a: float, b: float)->float:
    """Add the given 2 numbers"""
    return a+b

@mcp.tool
def generate_number(min_val:int, max_val:int)->int:
    """Generate a random number between 2 numbers"""
    return random.randint(min_val, max_val)  # includes both min_val and max_val


@mcp.resource('info://server')
def resource_info() -> str:
    """Get information about this server"""
    info = {
        "name":"Simple Calculator service",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add_numbers", "generate_number"],
        "author": "Muhammad Azfar"
    }

# Start the server
if __name__ == "__main__":
    # 0.0.0.0 means we will adopt any ip address
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    # mcp.run()