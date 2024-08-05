# Lab 7 Assignment - Documenting a Python Project with reStructuredText and Sphinx

## Timeline
<table>
  <thead>
      <td style="text-align:left;">Assigned</td>
      <td style="text-align:left;">Monday 9 September 2024</td>
  </thead>
  <tfoot>
      <td style="text-align:left; color: red;">Deadline</td>
      <td style="text-align:left;">Friday 13 September 2024</td>
  </tfoot>
</table>


![Lab 7 Assignment](https://github.com/allegheny-college-cmpsc-104-Fall-2024/lab07/blob/main/graphics/restructuredtext.png)


## Assignment Overview

1. **Complete the TODO tasks in `/writing/reStructuredText.md`**
2. **Document the Calculator Project using Sphinx**:
    - Use Sphinx to generate documentation for the project.

## Project Goals
1. **Understand reStructuredText Syntax**:
   - Learn how to use reStructuredText to format text, create links, and include images.
2. **Generate Documentation with Sphinx**:
   - Learn how to use Sphinx to automatically generate documentation from reStructuredText files.
3. **Enhance Technical Writing Skills**:
   - Improve your ability to write technical documentation that is clear, accurate, and easy to understand.

## Tools
- A computer
- Internet connection
- A GitHub account

## Learning Outcomes
These assignment learning outcomes contribute to the following course learning outcomes described in the course syllabus:

1. Describe and explain processes such as software installation or design for a variety of technical and non-technical audiences ranging from inexperienced to expert.
2. Use professional-grade integrated development environments (IDEs), command-line tools, and version control systems to compose, edit, and deploy well-structured, web-ready documents and industry-standard documentation tools.
4. Identify and apply appropriate conventions of a variety of technical communities, tools, and computer languages to produce industry-consistent diagrams, summaries, and descriptions of technical topics or processes.

## Instructions

### Part 1: reStructedText 
- Follow the instructions and complete the sections marked as TODO in the `reStructuredText.md` file.

### Part 2: Documenting the Calculator Project
  - Navigate to the sphinx directory and Open calculator/main.py.
  - Edit the `calculator.rst` file located in `sphinx/source/calculator.rst` to include detailed documentation for each function in the calculator module.
  - Run Sphinx to generate the documentation: `make html`

### _Notes_: 
- Within `writing/reStructedText.md`, you will find tasks awaiting your completion. As you work, please ensure to remove all markers indicating pending work.
- Ensure you have installed the Sphinx Read the Docs theme by running: `pip install sphinx-rtd-theme`.

## Resources
- reStructuredText Documentation: https://docutils.sourceforge.io/rst.html
- Sphinx Documentation: https://www.sphinx-doc.org/en/master/

## Deliverables
Please submit your work by pushing it to your GitHub Classroom repository.
- You will modify the files `writing/reStructedText.md` and `sphinx/source/calculator.rst` to respond questions in the document.
- You will use Sphinx to generate HTML documentation for the Calculator project.

## Project Assessment
- **Completion of Part 1 (30%)**: Successfully completing Part 1 will contribute 30% towards the assessment.
- **Completion of Parts 2 (60%)**: The quality of the writing in `sphinx/source/calculator.rst` will be assessed, focusing on clarity, structure, and reStructuredText syntax according to the assignment guidelines.
    - Clarity and Coherence (10%): Writing is clear and explanations are well-understood.
    - Structure and Organization (10%): The documentation is well-structured and organized.
    - reStructedText Syntax (40%): Demonstrates a deep understanding and uses multiple reStructuredText constructs.
- **Achieve GatorGrader Compliance (10%)**: Successfully meets the criteria set by GatorGrader.

## Gator Grade
### GatorGrade Checks for Immediate Feedback

To provide immediate feedback on your submissions, we're utilizing GatorGrade. Upon submission, if there's a thick red X, it indicates missing components. This X will turn into a green check mark once your submission is complete. For details on what's missing, click on the red X.

To meet the lab assignment's baseline writing and commit requirements, you can use the department's `GatorGrade` tool. Ensure Python3 is installed on your computer (check with `python --version`). If Python is not installed, please follow these guides:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [Setting Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Installing `GatorGrade`:

- [Install](https://pipx.pypa.io/stable/) [pipx](https://pipx.pypa.io/stable/) if you haven't already (`pip install pipx`).
- Install `GatorGrade` using pipx (`pipx install gatorgrade`).
- Running `GatorGrade`:
 `gatorgrade --config config/gatorgrade.yml`

Good luck!