NODES = {
    "builder": {"owner": "builder_agent", "input": "story", "output": "code", "success": "code produced", "failure": "stop and report"},
    "security_scan": {"owner": "security_agent", "input": "code", "output": "scan_result", "success": "no critical findings", "failure": "block tester and report"},
    "tester": {"owner": "test_agent", "input": "code plus scan_result", "output": "test_result", "success": "checks pass", "failure": "return findings"},
}

def run(scan_passes):
    trace = ["builder", "security_scan"]
    if not scan_passes:
        return trace + ["halt: scan failed; tester not run"]
    return trace + ["tester"]

if __name__ == "__main__":
    for name, contract in NODES.items():
        print(name, contract)
    print("Success simulation:", run(scan_passes=True))
    print("Failure simulation:", run(scan_passes=False))

