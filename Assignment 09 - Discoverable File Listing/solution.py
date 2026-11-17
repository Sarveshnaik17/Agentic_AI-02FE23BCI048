CAPABILITIES = {"list_files": lambda: {"files": ["agenda.txt", "minutes.md"]}}

class Server:
    def manifest(self):
        return sorted(CAPABILITIES)

    def call(self, name, **arguments):
        if name not in CAPABILITIES:
            return {"error": "unknown capability"}
        return CAPABILITIES[name](**arguments)

class MCPClient:
    def __init__(self, server):
        self.server = server
        self.discovered = server.manifest()

    def invoke(self, name, **arguments):
        if name not in self.discovered:
            return {"error": "capability not discovered"}
        return self.server.call(name, **arguments)

if __name__ == "__main__":
    client = MCPClient(Server())
    print("Discovered:", client.discovered)
    print("Result:", client.invoke(client.discovered[0]))

