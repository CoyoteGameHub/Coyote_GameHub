KST Content Management and Website Rebuild
===========================================

About this Project
------------------

The aim of the project is to develop a central application distribution system for Javascript games.  Along with it, we will include a game/app ranking system, a user authentication system to allow user permissions to games, and an admin section to override “purchases” of games.  The end result will be a beta website that will run various various web applications/games after a user signs up and purchases an item.  The user then will be able to play/access the game no matter what machine they are, purchase more games, and to leave reviews.   

This codebase utilizes the [**Django**](https://docs.djangoproject.com/en/1.9/) webframework, with built-in support for the [**Django Templating Language (DTL)**](https://docs.djangoproject.com/en/1.9/topics/templates/) HTML templating engine. Website data is stored in a [**PostgreSQL**](http://www.postgresql.org/docs/) database. Manipulation of the database is done through the Django's built-in wrapper. Database migrations are done using [**Django Migrations**](https://docs.djangoproject.com/en/1.9/topics/migrations/).

For easier styling, we will be using [**Bootstrap**](http://bootstrapdocs.com/v3.0.3/docs/css/), the most popular responsive, mobile friendly front-end framework available.  To ensure visual cohesion, developers are encouraged to use available templates already created and implemented.  Developers are advised to stick to the coding conventions and practices that are already used to ensure the project is extensible for all future developers.

Developers
----------

* Lawrence Thai *lthai423* [lthai@kellyspace.com](mailto:lthai@kellyspace.com)

Getting Involved
----------------

[Get in contact with the CoyoteGameHub Webmaster](mailto:lthai@kellyspace.com) to get added to the GitHub team. If added, you will get write access to the repository.

Requirements
------------

* Linux or Mac OS X (using Homebrew to install *python* and *pip*)
* python 3.4.x
* python-virtualenv 12.1.x
* git 2.4.x
* pip 6.1.x
* postgresql 9.4.x
* (the remaining requirements will be installed below using *pip*)

**Note:** Pay close attention to the package names for your distro of Linux...

* For example, on Ubuntu Server you'd use ```python3 virtualenv git python3-pip postgresql```.
* On Manjaro (an Arch-derivative), you'd use ```python python-virtualenv git python-pip postgresql```.

Setting Up
----------

### Mac OSX via Command Line

Check Back Soon

Ongoing Work
------------

* Always begin your day by pulling the latest revisions from GitHub

* To run the site locally after install, run the following command "python manage.py runserver"


Developer notes
---------------




Contributions
	
	README was templated from a modified version of CSUSB CSE Club's Website Project README.