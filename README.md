Python Assignment

This repository contains solutions to Python practice problems from HackerRank.
Each problem is implemented as a small module with:

driver.py → Entry point to run the solution

util.py → Core logic

test_*.py → Unit tests for validation

All problems are organized topic-wise for clarity and maintainability.

📂 Categories and Problems
🔹 Basic Data Types and Lists

list_operations

find_the_runner_up

finding_the_percentage

no_idea

word_order

named_tuple

mutations

🔹 Strings and Formatting

string_formatting

text_alignment

merge_the_tools

🔹 Iterators and Itertools

iter_and_iterator

🔹 Math and Numeric Operations

floor_ceil_rint

mean_var_std

min_max

linear_algebra

🔹 Date and Time

calendar_module

time_delta

🔹 Algorithms and Logic Problems

piling_up

🔹 Validation and Filtering

validating_email_filter

🗂 Project Structure
.
├── README.md
├── output.txt
├── scripts/
│   └── hooks/
│       ├── commit-message.py
│       ├── pre-commit.py
│       └── pre-push.py
├── src/
│   ├── calendar_module/
│   ├── find_the_runner_up/
│   ├── finding_the_percentage/
│   ├── floor_ceil_rint/
│   ├── iter_and_iterator/
│   ├── linear_algebra/
│   ├── list_operations/
│   ├── mean_var_std/
│   ├── merge_the_tools/
│   ├── min_max/
│   ├── mutations/
│   ├── named_tuple/
│   ├── no_idea/
│   ├── piling_up/
│   ├── string_formatting/
│   ├── text_alignment/
│   ├── time_delta/
│   ├── validating_email_filter/
│   └── word_order/
└── test/
    ├── calendar_module/
    ├── find_the_runner_up/
    ├── finding_the_percentage/
    ├── floor_ceil_rint/
    ├── iter_and_iterator/
    ├── linear_algebra/
    ├── list_operations/
    ├── mean_var_std/
    ├── merge_the_tools/
    ├── min_max/
    ├── mutations/
    ├── named_tuple/
    ├── no_idea/
    ├── piling_up/
    ├── string_formatting/
    ├── text_alignment/
    ├── time_delta/
    ├── validating_email_filter/
    └── word_order/

📌 Folder Convention
src/<problem_name>/

driver.py → Runs the program

util.py → Contains the implementation logic

test/<problem_name>/

test_<problem_name>.py → Unit tests for the problem

▶ How to Run a Solution
python src/<problem_name>/driver.py


Example:

python src/list_operations/driver.py

🧪 How to Run Tests
python test/<problem_name>/test_<problem_name>.py


Example:

python test/list_operations/test_list_operations.py

📖 About

This repository contains my Python assignments completed during my internship.
It follows clean coding practices, modular design, and includes unit tests for reliability.

🛠 Languages Used

Python (100%)