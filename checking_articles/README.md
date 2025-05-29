# Article Comparison Tool

A Python application built with Tkinter that helps users analyze and compare two articles. This tool provides functionality to find common words between articles and identify unique words in each article.

## Features

- Input two articles using text widgets
- Find and display common words between the articles
- Search for unique words in a specific article by title
- Display word count statistics
- User-friendly graphical interface

## File Description

### article_comparison.py
The main application file that implements:
- Text input widgets for two articles
- Button to find common words
- Button to find unique words with article title input
- Results display area
- Word processing and comparison logic

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Usage

1. Run the application:
```bash
python article_comparison.py
```

2. Enter the text of two articles in the provided text areas
3. Use the "Find Common Words" button to see words that appear in both articles
4. Use the "Find Unique Words" button and enter an article title to see words unique to that article

## How it Works

- The application processes the input texts by:
  - Removing punctuation
  - Converting to lowercase
  - Splitting into individual words
  - Performing set operations for comparison
  - Displaying results in a formatted way

## Author

- Erfan Kalantari (@erfanklt) 