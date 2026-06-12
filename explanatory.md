# Beginner Explanatory Guide: Exercise 2: Navigating a Codebase

> **Task Type**: Product Task  
> **Domain/Focus**: Codebase Navigation, Python Fundamentals

---

## 1. The Goal (In-Depth Beginner Explanation)

### The Core Problem
In software development, understanding how to navigate a codebase is crucial for effective collaboration and productivity. This task focuses on familiarizing yourself with a mini project, specifically a Command Line Interface (CLI) task manager, which is a simplified application that helps users manage their tasks. The core problem this exercise addresses is the need for developers to quickly orient themselves within a new codebase, which can often be overwhelming due to the sheer volume of files and complexity of the code.

Currently, the task manager application has a few functionalities, such as adding tasks and marking them as complete. However, it also contains a bug where it does not check for duplicate task titles when adding new tasks. Understanding how to navigate the codebase will allow you to identify such issues and contribute to fixing them. This skill is essential for maintaining the quality of the software and ensuring that users have a seamless experience when managing their tasks.

### Jargon Buster (Key Terms Explained)
* **Codebase**: A codebase is the collection of source code used to build a particular software application. It includes all the files and directories that contain the code, documentation, and resources needed to run the application. For example, in our task manager, the codebase includes files like `taskManager.py` and `test_tasks.py`.

* **CLI (Command Line Interface)**: A CLI is a way for users to interact with a computer program by typing commands into a console or terminal. Unlike graphical user interfaces (GUIs), which use visual elements like buttons and icons, CLIs require users to know specific commands. In our task manager, users can add tasks or mark them as complete using text commands.

* **Bug**: A bug is an error or flaw in software that causes it to produce incorrect or unexpected results. In our task manager, the bug is that it allows users to add tasks with the same title, which can lead to confusion and mismanagement of tasks.

* **Test Case**: A test case is a set of conditions or variables under which a tester will determine whether a system or software application is working correctly. In our task manager, the test case checks if a task is successfully added to the task list.

### Expected Outcome
After completing this exercise, you should be able to navigate the codebase of the task manager confidently. You will understand how many source files and test files exist, what programming language is used, and the structure of the application. Specifically, you will be able to identify the classes in `taskManager.py`, understand their functionalities, and recognize the existing bug related to duplicate task titles. 

**Before vs. After**:
- **Before**: You may feel lost in the codebase, unsure of where to find information or how the application works.
- **After**: You will have a clear understanding of the project's structure, the purpose of each file, and how to locate and address issues like the duplicate title bug.

---

## 2. Related Coding Concepts & Syntax (50% Theory, 50% Practice)

### Concept 1: Classes and Objects in Python
#### 📘 Theoretical Overview (50%)
* **Why it exists**: Classes and objects are fundamental concepts in object-oriented programming (OOP). A class is a blueprint for creating objects, which are instances of that class. This structure allows developers to model real-world entities and their behaviors in code. Without classes, code would be less organized and harder to manage, especially in larger applications.

* **Key Mechanisms**: In Python, a class is defined using the `class` keyword, followed by the class name. Inside a class, you can define attributes (variables) and methods (functions) that describe the properties and behaviors of the objects created from that class. For example, the `Task` class in our task manager has attributes like `title` and `priority`, and methods like `complete()` that define what a task can do.

#### 💻 Syntax & Practical Examples (50%)
* **Language Syntax**:
  ```python
  class ClassName:
      def __init__(self, parameters):
          # Constructor method to initialize attributes
          self.attribute = parameters

      def method_name(self):
          # Method to define behavior
          pass
  ```

* **Real-World Application**:
  ```python
  class Task:
      def __init__(self, title, priority='medium'):
          self.title = title
          self.priority = priority
          self.done = False

      def complete(self):
          self.done = True
  ```

In this example, the `Task` class has a constructor that initializes the task's title and priority, and a method `complete()` that marks the task as done.

---

## 3. Step-by-Step Logic & Walkthrough

1. **Step 1: Locate and Analyze the Target File**
   * Navigate to the `sample_project/src/` directory and open the `taskManager.py` file. This file contains the main logic for the task manager application.
   * Focus on the first 20 lines of code to identify the classes defined within it. You will find the `Task` and `TaskManager` classes.

2. **Step 2: Input Verification & Validation**
   * Check the `add` method in the `TaskManager` class. Notice the comment indicating a bug: "BUG: Doesn't check for duplicate titles." This is an important aspect to consider when adding new tasks.

3. **Step 3: Core Implementation / Modification**
   * To fix the bug, you will need to modify the `add` method to include a check for existing task titles before appending a new task. This ensures that no two tasks can have the same title.

4. **Step 4: Output Verification & Testing**
   * After making the changes, run the tests in `test_tasks.py` to verify that the application behaves as expected. You can use the command `pytest` in the terminal to execute the tests and check for any failures.

---

## 4. Detailed Walkthrough of Test Cases

### Test Case 1: Standard / Success Case
* **Description**: This test checks if a task can be successfully added to the task manager.
* **Inputs**:
  ```json
  {
    "title": "Write tests",
    "priority": "medium"
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `add` method is called with the title "Write tests".
  2. The method checks if a task with the same title already exists (this is where the bug fix will be implemented).
  3. Since there are no existing tasks, a new `Task` object is created and added to the `tasks` list.
  4. The length of the `tasks` list is now 1, indicating that the task was successfully added.
* **Expected Output**: The output should confirm that the task manager now contains one task.

### Test Case 2: Edge Case / Validation Fail
* **Description**: This test checks the behavior when attempting to add a task with a duplicate title.
* **Inputs**:
  ```json
  {
    "title": "Write tests",
    "priority": "medium"
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `add` method is called again with the same title "Write tests".
  2. The method checks for existing tasks and finds that a task with the same title already exists.
  3. The method does not add the new task and returns an error message or simply does nothing.
* **Expected Output**: The output should indicate that the task was not added due to a duplicate title, maintaining the integrity of the task list.