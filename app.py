from flask import Flask, abort, render_template, request, redirect, url_for


STATUSES = ("completed", "in_progress", "recommendation")

STATUS_LABELS = {
    "completed": "Completed",
    "in_progress": "In progress",
    "recommendation": "Recommendation",
}


def initial_books() -> list[dict]:
    seeds = [
        {
            "title": "The Wind-Up Bird Chronicle",
            "author": "Haruki Murakami",
            "summary": "A quiet man's search for his missing cat unfolds into a surreal journey through memory, war, and the hidden lives just beneath ordinary Tokyo.",
            "status": "completed",
            "tags": "surreal, mystery, literary",
        },
        {
            "title": "Piranesi",
            "author": "Susanna Clarke",
            "summary": "A gentle narrator catalogues the tides and statues of an endless House, slowly piecing together who he is and how he came to live there.",
            "status": "in_progress",
            "progress": "Page 84",
            "tags": "surreal, mystery, fantasy",
        },
        {
            "title": "Educated",
            "author": "Tara Westover",
            "summary": "A memoir of growing up in a survivalist family in rural Idaho and finding a way, against every expectation, into a life shaped by learning.",
            "status": "completed",
            "tags": "memoir, education, coming-of-age",
        },
        {
            "title": "The Left Hand of Darkness",
            "author": "Ursula K. Le Guin",
            "summary": "An envoy from a distant union of worlds tries to befriend a planet whose people are neither men nor women, and discovers what trust really costs.",
            "status": "recommendation",
            "tags": "science-fiction, social-commentary",
        },
    ]
    for index, book in enumerate(seeds, start=1):
        book["id"] = index
    return seeds


def validate_book(form) -> tuple[dict, str | None]:
    fields = {
        "title": form.get("title", "").strip(),
        "author": form.get("author", "").strip(),
        "summary": form.get("summary", "").strip(),
        "status": form.get("status", "").strip(),
        "progress": form.get("progress", "").strip(),
        "tags": form.get("tags", "").strip(),
    }
    for name in ("title", "author", "summary"):
        if not fields[name]:
            return fields, f"{name.capitalize()} cannot be empty."
    if fields["status"] not in STATUSES:
        return fields, "Please choose a status."
    if fields["status"] == "in_progress" and not fields["progress"]:
        return fields, "Please enter your progress (e.g. Page 50 or Chapter 25)."
    if fields["status"] != "in_progress":
        fields["progress"] = ""
    return fields, None


def create_app() -> Flask:
    app = Flask(__name__)
    app.books = initial_books()
    app.next_book_id = max((book["id"] for book in app.books), default=0) + 1

    def find_book(book_id: int) -> dict:
        for book in app.books:
            if book["id"] == book_id:
                return book
        abort(404)

    def render_book_form(*, action_url, heading, submit_label, values, error=None):
        return render_template(
            "new_book.html",
            error=error,
            values=values,
            statuses=STATUSES,
            status_labels=STATUS_LABELS,
            action_url=action_url,
            heading=heading,
            submit_label=submit_label,
        )

    @app.route("/")
    def home():
        search_query = request.args.get("search", "").strip().lower()

        filtered_books = app.books
        if search_query:
            filtered_books = [
                book for book in filtered_books
                if search_query in book.get("title", "").lower()
            ]
            
        return render_template(
            "home.html",
            books=filtered_books,
            status_labels=STATUS_LABELS,
        )

    @app.route("/books/new", methods=["GET", "POST"])
    def new_book():
        action_url = url_for("new_book")
        if request.method == "POST":
            fields, error = validate_book(request.form)
            if error:
                return render_book_form(
                    action_url=action_url,
                    heading="Add a book",
                    submit_label="Add book",
                    values=fields,
                    error=error,
                )
            fields["id"] = app.next_book_id
            app.next_book_id += 1
            app.books.insert(0, fields)
            return redirect(url_for("home"))
        return render_book_form(
            action_url=action_url,
            heading="Add a book",
            submit_label="Add book",
            values={},
        )

    @app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
    def edit_book(book_id: int):
        book = find_book(book_id)
        action_url = url_for("edit_book", book_id=book_id)
        if request.method == "POST":
            fields, error = validate_book(request.form)
            if error:
                return render_book_form(
                    action_url=action_url,
                    heading="Edit book",
                    submit_label="Save changes",
                    values=fields,
                    error=error,
                )
            book.update(fields)
            return redirect(url_for("home"))
        return render_book_form(
            action_url=action_url,
            heading="Edit book",
            submit_label="Save changes",
            values=book,
        )

    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=5000)
