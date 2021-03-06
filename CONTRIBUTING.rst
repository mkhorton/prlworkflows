==================
Contribution Guide
==================

Project Goals
-------------

1. Privately store code for projects in progress
2. Provide access to workflows for PRL group use that are not suitable for atomate due to privacy, code quality, or project scope

How to Contribute 
-----------------

1. Clone the repository to your local machine
2. Create a new branch for your addition or changes (``git checkout -b mybranchname``)
3. Write code or make changes and commit them to your branch
4. (Recommended) If you have multiple commits, clean up your commit history (``git rebase -i myfirstcommithash^ HEAD``)
5. Push your branch to the repository (``git push origin mybranchname``)
6. Submit a merge request

After you submit a merge request, other members of the group are able to review your changes and give feedback. Someone with a rank of Master or higher in the project can merge your commits into the master branch.

Style Guidelines
----------------

In general, code style should follow PEP8_ and PEP20_. Specifics are summarized below:

- Code should be indented using spaces, not tabs. One indentation = 4 spaces
- Lines longer than 100 should be manually wrapped, but prefer readability
- Minimize blank lines: 2 around top level classes functions, 1 in nested functions
- Workflows, Fireworks, and Firetasks should follow the same naming scheme as in atomate
- Include docstrings for classes and functions (see code), add comments where needed
- Function and variable names should be descriptive (not 'x' or 'xx') and all lowercase_with_underscores
- Class names should be descriptive CapitalWords

.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _PEP20: https://www.python.org/dev/peps/pep-0020/
