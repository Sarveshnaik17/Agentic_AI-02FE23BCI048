import posixpath

FILES = {"/safe/agenda.txt": "Approved agenda"}
SAFE_ROOT = "/safe"

def read_file(requested_path):
    normalized = posixpath.normpath("/" + requested_path.lstrip("/"))
    if normalized != SAFE_ROOT and not normalized.startswith(SAFE_ROOT + "/"):
        return {"error": {"code": "OUT_OF_SCOPE", "message": "Path is outside /safe."}}
    if normalized not in FILES:
        return {"error": {"code": "NOT_FOUND", "message": "File not found."}}
    return {"content": FILES[normalized]}

if __name__ == "__main__":
    print("Allowed:", read_file("/safe/agenda.txt"))
    adversarial = read_file("/safe/../../private/secret.txt")
    print("Adversarial:", adversarial)
    assert adversarial["error"]["code"] == "OUT_OF_SCOPE"

