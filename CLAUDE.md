# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project
A book tracker web app built with Flask (Python) because I am more used to flask and python. Each book record has three fields: **title**, **author**, **summary** that is displayed. Book records can be added on, has filters, tags, and status. Allows user to keep track of books while they read (completed, in progress, and recommendations).

## Coding constraints

These are hard rules, not preferences:

- **No global state.** Pass state explicitly (Flask app context, function args, instance attributes). No module-level mutable globals.
- **Small, focused functions.** One responsibility per function.
- **Do not add new dependencies without asking.** Confirm before introducing any package not already declared.
- **Do not modify tests to make them pass.** If a test fails, fix the code under test, or ask the user if the test itself is wrong. Never silently adjust assertions or fixtures to suppress failure.

## Working
- Always read the task file before writing code.
- Plan before implementing — ask Claude for a plan first.