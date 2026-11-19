from concurrent.futures import ThreadPoolExecutor

STORIES = [
    {"id": "CSV-1", "title": "Export meeting data to CSV"},
    {"id": "PDF-1", "title": "Export meeting data to PDF"},
]

def process(story):
    artifacts = []
    for stage in ("design", "code", "test"):
        artifacts.append({"story_id": story["id"], "stage": stage,
                          "artifact": f"{story['title']} - {stage} artifact"})
    return artifacts

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as pool:
        outputs = list(pool.map(process, STORIES))
    trace = sorted((item for group in outputs for item in group),
                   key=lambda item: (item["story_id"], item["stage"]))
    for event in trace:
        print(event)
    assert {item["story_id"] for item in trace} == {"CSV-1", "PDF-1"}

