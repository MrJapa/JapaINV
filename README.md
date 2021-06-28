<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MrJapa/Inventory">
    <img src="images/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Inventory system</h3>

  <p align="center">
    A inventory system designed to fit all of your IT data
    <br />
    <a href="https://github.com/MrJapa?tab=repositories"><strong>Explore my repositories »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MrJapa/Inventory/issues">Report Bug</a>
    ·
    <a href="https://github.com/MrJapa/Inventory/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/MrJapa/Inventory/blob/main/images/example.png)

There are many great inventory systems out there - but almost all of them are licensed.
This program helps you create nice overlook over your IT equipment.
In order to run this program on your SQL Server, you will need to make a lot of changes in the inv.py file, as this is where tables and functions are defined. Layout pictures can be easily replaced as they are included in .png and .psd format.


### Built With

This project became possible due to tkinter and pyodbc's easy and high performing modules.
* [Python](https://www.python.org/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [pyodbc](https://pypi.org/project/pyodbc/)



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

To run this program you need to have the SQL ODBC Driver installed on your pc. The inventory program prompts you for an installation if it is not already installed.
* Microsoft ODBC Driver 17 for SQL Server
  ```sh
  https://go.microsoft.com/fwlink/?linkid=2156851
  ```
* Azure SQL or SQL Server
  ```sh
  https://azure.microsoft.com/en-us/products/azure-sql/database/
  ```
* Database tables that matches program
  ```sh
  Computers, Phones, Hardware etc.
  ```

### Installation

1. Get the latest release here: [Releases](https://github.com/MrJapa/Inventory/releases)

2. Clone the repo
   ```sh
   git clone https://github.com/MrJapa/Inventory.git
   ```
4. Enter your keys in `password.py`
   ```py
    serverkey = "example.database.windows.net"
    databasekey= "database_name"
    uidkey = "user_name"
    passwordkey = "user_password"
   ```



<!-- USAGE EXAMPLES -->
## Usage

_please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact

Jacob Japa - [LinkedIn](https://www.linkedin.com/in/jacobjapa/) - jjv@cracked.to

Project Link: [github.com/MrJapa/Inventory/projects](https://github.com/MrJapa/Inventory/projects/1)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [othneildrew README Template](https://github.com/othneildrew/Best-README-Template)
* [GitHub Pages](https://pages.github.com)
* [Python Discord](https://discord.gg/python)
* [Stack Overflow](https://stackoverflow.com/)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[issues-url]: https://github.com/MrJapa/Inventory/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jacobjapa/
[product-screenshot]: images/example.png
