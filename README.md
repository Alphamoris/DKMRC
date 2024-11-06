# 🏥 Hospital Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A streamlined hospital management system that efficiently handles patient records, doctor availability, and departmental organization. Built with Python and MySQL, this system provides a robust solution for managing patient-doctor relationships and departmental workflows.

## 🚀 Features

- **Patient Management**
  - Unique ID generation for each patient
  - Department-wise patient sorting
  - Comprehensive patient information storage
  - Quick patient lookup system

- **Doctor Management**
  - Real-time doctor availability tracking
  - Department-wise doctor organization
  - Doctor-patient association tracking
  - Schedule management

- **Department Organization**
  - Systematic patient categorization
  - Department-wise statistics
  - Efficient patient distribution

## 💻 Technology Stack

- **Backend**: Python 3.8+
- **Database**: MySQL 8.0+
- **Connector**: mysql-connector-python
- **Data Processing**: Native Python libraries

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/hospital-management-system.git
cd hospital-management-system
```

2. Install required dependencies
```bash
pip install mysql-connector-python
```

3. Configure MySQL database
```bash
mysql -u root -p < database/schema.sql
```

4. Update database configuration
```python
# config.py
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'hospital_management'
}
```


## 🔑 Key Features Explained

1. **Unique ID System**
   - Automated ID generation for patients
   - Format: P{YYYY}{MM}{Sequential Number}
   - Ensures zero collisions and easy tracking

2. **Department Management**
   - Automated patient sorting
   - Real-time department statistics
   - Efficient resource allocation

3. **Doctor-Patient Association**
   - Foreign key relationships for data integrity
   - Quick lookup capabilities
   - Comprehensive relationship tracking

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 📬 Contact

Email - [@Alphamoris](alpahamoris45@gmail.com)


## 🙏 Acknowledgments

- All contributors who have helped evolve this system
- MySQL documentation for database best practices
- Python community for excellent libraries and support
