# Disclaimer

''WARNING'': This is alpha software. It is primarily being developed to test the ability of AI Development tools in creating, modifying, and maintaining an entire project. There is no guarantee this project works as described, or that it will not cause damage to your system. You should almost certainly not use it until this message is removed from the readme. 

# Resumate

Resumate is a comprehensive job search platform developed using Django for the backend, Angular for the frontend, and Postgres for the database. It adheres to modern web standards and best practices, using Sass, TypeScript, and Python 3.11 with strict typing.

## Features

- User Registration and Authentication
- User Profile Creation and Management
- Integration with LinkedIn and Other Services
- Resume Upload Feature
- Job Matching and Indexing System
- Job Scoring Algorithm
- Automated Application Process
- Application History and Management
- Auto-Apply Feature
- Job Board Crawling
- Pause Indexing
- AI Integration for Job Evaluation
- Security and Privacy

## Getting Started

1. Clone the repository:

```
git clone https://github.com/yourusername/resumate.git
```

2. Install the required dependencies:

```
cd resumate
pip install -r requirements.txt
```

3. Set up the database:

```
python manage.py makemigrations
python manage.py migrate
```

4. Run the development server:

```
python manage.py runserver
```

5. Navigate to the frontend directory and install the required dependencies:

```
cd resumate/frontend
npm install
```

6. Run the Angular development server:

```
ng serve
```

7. Open your browser and navigate to `http://localhost:4200` to access the application.

## Contributing

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
