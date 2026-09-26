# CampusFind — Smart Lost & Found Matching System

## 1. Overview

CampusFind is a simple Python application for managing lost and found items on a college campus. Unlike a basic record-management system, it includes a rule-based matching engine that compares lost and found reports and produces a match score.

## 2. Features

- Report lost items
- Report found items
- Search and filter reports
- Compare lost and found records
- Calculate a 0–100 match score
- Explain why a match was suggested
- View basic statistics
- Store records in JSON
- Input validation and error handling

## 3. Technologies

- Python 3
- JSON
- `dataclasses`
- `unittest`
- Git/GitHub

No external packages are required.

## 4. Installation

```bash
git clone <your-repository-url>
cd CampusFind
python main.py
```

## 5. Testing

Run:

```bash
python -m unittest -v
```

## 6. Project Structure

```text
CampusFind/
├── main.py
├── models.py
├── storage.py
├── matching.py
├── task_manager.py
├── validators.py
├── utils.py
├── test_project.py
├── data/
│   └── items.json
├── statement.md
├── report.md
├── requirements.txt
└── README.md
```

## 7. Matching Logic

The matching engine uses weighted rules:

| Criterion | Weight |
|---|---:|
| Category | 30 |
| Color | 15 |
| Location similarity | 20 |
| Description/name similarity | 25 |
| Same date | 10 |
| **Maximum** | **100** |

A match is displayed when the score reaches the configured threshold.

## 8. Limitations

The project uses rule-based text similarity rather than machine learning. It is intended as a simple academic project and does not provide real authentication, online notifications, or cloud deployment.

## 9. Future Enhancements

- Web interface using Flask
- User authentication
- Image-based item matching
- Email notifications
- Database support with SQLite
- Admin dashboard
