Summarizer 3000
=======

What is it?
----------

Our project, The Summarizer 3000, is a tool for quickly rewriting and summarizing 
content from wikipedia. The Summarizer 3000 is a tool that will make writing short summary paragraphs easy. The tool helps you by providing a seed paragraph from Wikipedia about the relevant topic. As the user makes changes to the seed paragraph, the similarity to the original is calculated by the tool. The user can continue to make the document their own until it is suﬃcently unique. The tool helps you crank out information gathered from the web in your own writing style.



Core algorithm
--------
The core algorithm is the similarity calculation. We compute the similarity
between your changes and the original wikipedia document. When you've rewritten
the content in your own words, the similarity score will reflect that.


Where is it?
------
You can see the core algorithm in action here: https://guarded-beach-7472.herokuapp.com/ or if you are interested in hosting the project yourself simply run the following command from the project's flask directory. `python writing_tool.py`.


Current issues
---------
1. If the fetched page is not unique in wikipedia, it causes an error. 
2. The similarity computation needs to be improved.
3. The tools list needs to be seperated into a selector and a workspace.
4. Add find replace tool?


Author: Patrick Rock
