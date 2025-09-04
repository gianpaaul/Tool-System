# Tool System

An application developed using **Python** with **Tkinter** for the graphical interface and **MySQL** for database management, designed to optimize sales and inventory management in a tool store. This system uses parallel algorithms to improve data processing efficiency and enhance performance when handling large volumes of sales data. 

---

## Table of Contents  
- [Project Description](#project-description)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributions](#contributions)  
- [License](#license)  
- [Contact](#contact)  

---

## Project Description  
This personal project aims to develop a **Sales Registration and Management System** for a tool store. The system is designed to efficiently handle large volumes of sales data through the use of parallel algorithms, specifically multiprocessing and multithreading. It uses **MySQL** as the database, managed through **XAMPP**, and is equipped with an intuitive graphical user interface (GUI) created using **Tkinter** and **customtkinter**.

The system allows users to:
- Manage and query products and sales.
- Sort products based on various criteria like sales number, product name, and code.
- Generate detailed sales reports for decision-making.
- Optimize data processing and improve performance with parallel operations.

---

## Features  
- ✔️ **Product Management**: Add, query, and sort products by various criteria (e.g., sales number, name, code).  
- ✔️ **Sales Management**: Query and generate sales reports.  
- ✔️ **Graphical User Interface (GUI)**: Developed with Tkinter and customtkinter for an intuitive user experience.  
- ✔️ **Parallel Data Processing**: Utilizes multiprocessing and multithreading techniques to optimize performance in data handling and sorting.  
- ✔️ **Performance Analysis**: Compares execution times between sequential and parallel operations to ensure optimal performance.  

---

## Prerequisites  
1. **Read the attached PDF file: "Read before compiling the project".** 
2. **Python**: Ensure Python 3.x is installed on your machine. You can download it from [https://www.python.org/](https://www.python.org/).  
3. **MySQL**: You need MySQL, managed via XAMPP. Download and install XAMPP from [https://www.apachefriends.org/](https://www.apachefriends.org/).  
4. **Tkinter**: Tkinter should come pre-installed with Python, but you can ensure it's installed by running `pip install tk`.  
5. **XAMPP**: Download and install XAMPP from [https://www.apachefriends.org/](https://www.apachefriends.org/).

---

## Installation  
Follow these steps to install and run the project on your local machine:

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/gianpaaul/tool-store-sales-management.git

Open the Project folder

3. **Configure the Database in XAMPP:**
   3.1 Start **XAMPP** and activate the **Apache** and **MySQL** modules.
   3.2 Open **phpMyAdmin** from the **XAMPP** control panel.
   3.3 Create a database named **ferreteria**.
   3.4 Import the provided **ferreteria.sql** file:
   3.5 Navigate to the Import tab.
   3.6 Select the **ferreteria.sql** file from the cloned repository.
   3.7 Click Go to complete the import.
        
4. **Final Configuration:**
   4.1 Open the **connection.py** file in your project folder.
   4.2 Verify and adjust the database connection credentials:
   ```
   Host: localhost  
   User: root  
   Password: (leave empty by default unless configured otherwise)  
   ```
        
5. **Run the Project**
   
   5.1 Run the Python script main.py to start the application:

---
## Contributions
Contributions are welcome! Here's how you can contribute:
1. **Fork the repository.**
2. **Create your branch:**
    ```bash
    git checkout -b feature/NewFeature
3. **Make your changes and commit:**
    ```bash
    git commit -m 'Add new feature'
4. **Push to your branch:**
    ```bash
    git push origin feature/NewFeature
5. **Open a pull request.**
---
## Contact
 GitHub: (https://github.com/gianpaaul)

---
## License
This project is protected under GR copyrights. Modifications are allowed exclusively for improvement purposes under the terms described in the license file. See LICENSE for more details.
