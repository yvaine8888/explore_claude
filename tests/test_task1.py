def test_empty_title_shows_error(client):
    r = client.post("/books/new", data={
        "title": "",
        "author": "Susanna Clarke",
        "summary": "A gentle narrator lives in a vast House...",
        "status": "in_progress",
        "progress": "Page 84",
        "tags": "surreal, mystery, fantasy"
    })

    assert r.status_code == 200
    assert b"Title cannot be empty." in r.data

def test_empty_author_shows_error(client):
    r = client.post("/books/new", data={
        "title": "Piranesi",
        "author": "",
        "summary": "A gentle narrator lives in a vast House...",
        "status": "in_progress",
        "progress": "Page 84",
        "tags": "surreal, mystery, fantasy"
    })

    assert r.status_code == 200
    assert b"Author cannot be empty." in r.data

def test_empty_progress_shows_error(client):
    r = client.post("/books/new", data={
        "title": "Piranesi",
        "author": "Susanna Clarke",
        "summary": "A gentle narrator lives in a vast House...",
        "status": "in_progress",
        "progress": "",
        "tags": "surreal, mystery, fantasy"
    })

    assert r.status_code == 200
    assert b"Please enter your progress (e.g. Page 50 or Chapter 25)." in r.data