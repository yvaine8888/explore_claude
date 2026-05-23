1. Foundation - Scaffold the repo (Flask app with python) and write the CLAUDE.md. Verify - Requirements has flask and Claude.md with goal.
  - Plan - I'll save the project context and your coding preferences to memory,
  then create a CLAUDE.md that captures these.
  - Changed - I added more to summary and scaffolded myself.
  - Verified - Ran and saw the Claude.md.
  - Learned - I learned what scaffolding was and how to make a claude.md better.
2. Basic UI - Home page that displays each book with title, author, and summary. Style it with pink  and white colors and soft text. Verify - With examples, run the app and see if it is displayed with style.
  - Plan - Changing app.py for seed helper and home route. Render book list in html and add a styles.css with sample books.
  - Changed - Didn't need to change much but needed to clarify a lot about sample books and home.html.
  - Verified - Ran and ui with styled displayed books.
  - Learned - I learned about how different things are connected because it showed different ways for html and style.
3. Adding books - Have a button that directs to another page that allows books to be added with title, author, and summary (can't be empty). Verify - Another page with books to be added.
  - Plan - Changing html for add button and form. Render new books with get and post the form input with error message if empty.
  - Changed - Didn't need to change.
  - Verified - Ran and had ui with add book. Tried empty and did not allow submission.
  - Learned - I learned the different ways you could show errors.
4. Status - In the home page. Have tags of either completed, in progress, or recommendations. In the add html, add buttons to choose sections. Display books with status after author. Verify: Bookscan have status chosen. 
   - Plan - Extend validate_book() to require status in STATUSES; on missing/invalid, return an error. Add a "Status" field rendered as a row of buttons (radio inputs styled as pill buttons). Show the status as a small pill tag.
  - Changed - Got rid of verification because I could do it myself.
  - Verified - Ran and could add status with it displayed.
  - Learned - I learned how claude once read the file, does not pay attention to changes. I changed task.md but it still remembered a previous line.
5. Progress - If in progress, allow user to choose input where they are and display it after summary. For example, page 50 or chapter 25. Verify - It displays progress. 
  - Plan - Add a progress field to the book dict. Only populated when status is in_progress. Change html to match.
  - Changed - Got rid of placeholder for html.
  - Verified - Ran and could add progress if in progress.
  - Learned - I learned that Claude can go beyond because I did not mentio anything about style but it generated one for it.
6. Change - When user clicks on book title in home, go to new page html with fields already filled in, but allow user to change and resubmit it to change previous submission. Verify - User can change the books traits.
  - Plan - Identify books by id. Reuse form tempalte. Make title a link to edit route.
  - Changed - Made a mistake and accidently rewind. But got rid of veriifcation because overcomplicated.
  - Verified - Ran and change previous submission.
  - Learned - I learned that Claude can rewind and its really complicated to undo that.
7. Add tags - In the add.html, allow user to add tags seperated by commas. In the home html, display tags a line after status. Verify - Tags are shown.
  - Did not use Claude since running out of money. Instead use chatgpt to generate code. I asked for input tags field. Added to html myself and changed css.
8. Filtering - Have all status and tags as buttons at the top. When clicked, filter books and display ones with those tags. Allow multiple to be selected and all button that deselects all. Verify - Buttons that filter.
  - Asked chatgpt and seemed too complicated. Skipped.
9. Search - Have a search system at the top that allows user to input a string and search for book titles containing it. Verify - Search function for titles.
  - Asked chatgpt and added to home html, changed app.py to give filtered to template, and added to css.

All of Chatgpt had to add myself because it wasn't connected. That means I learned more about what it needed to generate, what files needed to be changed, and approved changes myself.

Reflection:
The agentic workflow let planned things I couldn't have done in 4 hours. For example, it took what I wanted, broke it down and executed it. This includes when I wanted to allow users to modify book records. The Claude agent saw a problem with doing so and told me. When I approved it, they made a plan: identify books by id, reuse form tempalte, and make title a link. I would not have thought of that but they did this in about a minute. There were times I had to override. When it was adding the modifying feature, I wanted to stop it because it was going beyond and overcomplicating it with the verification. I knew that I could verify myself manually and did not need all those steps. However, when overriding, I accidently rewind the conversation. I had to open a new session, and undo it. Even then, it was still not the same, showing Claude and myself can make mistakes. When doing this, it revealed my knowledge gaps of how things could be done or how Flask apps work. I didn't know that you need to id books to modify or how to render each tag in the home page. Claude had a different way to do the tasks which was more efficient since it understood my app better. Then when I used Chatgpt to add tags, I learned how html could split and render each one. This showed how I didn't fully understand html or Flask apps. I also learned how to create tests for pytest. I haven't created pytests before but today I learned it needed conftest, client and more. Using this, I learned how to use AI correctly like verifying that it did not skip over something or did not account for errors. I learned how to combine AI tools and that AI needs good context in order to keep to what I want and maintain privacy and security. Then, I learned how to create tests to verify functionality. This all could be used to help me code at work, working more efficiently and accurately.