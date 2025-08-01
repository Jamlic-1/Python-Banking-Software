# Python-Banking-Software


# 🏦 Banking Management System (Python + SQLite + Tkinter)

A desktop-based banking system developed in **Python**, with **SQLite** as the database and **Tkinter** for the graphical user interface (GUI). The system is designed to simulate real-world banking operations and provide secure, role-based access for different categories of users. This project aims to demonstrate full-stack software development skills in a desktop environment, including database modeling, UI design, and secure user authentication.

> 🚧 **Status**: Under active development — several modules are functional, while others are being incrementally added. Expect frequent updates and structural changes.

---

## 🎯 Project Objectives

This system is built to:
- Support multiple **user roles** with distinct permissions
- Perform basic and advanced **banking operations**
- Simulate a **real-world** banking workflow (from account creation to audits)
- Apply **OOP principles** for clean, scalable code
- Offer a responsive and user-friendly **Tkinter GUI**

---

## 👥 User Roles & Permissions

Each role has access to specific operations tailored to their responsibilities in a typical banking institution.

| Role               | Access & Functionalities                                                                 |
|--------------------|-------------------------------------------------------------------------------------------|
| **Admin**          | - Manage all user accounts (create, edit, delete)  
                    - Assign/revoke user roles  
                    - Monitor system activity logs  
                    - Configure global settings (interest rates, security)  
| **Manager**        | - Approve large transactions and loan applications  
                    - Oversee staff activity  
                    - Access performance dashboards  
                    - Generate branch-level reports  
| **Sales Officer**  | - Onboard new customers  
                    - Open/check account types  
                    - Handle KYC processes  
                    - Upsell financial products (loans, savings)  
| **Accountant**     | - Record deposits/withdrawals/transfers  
                    - Generate ledgers and reconciliations  
                    - View financial reports (P&L, trial balance)  
                    - Flag irregular activity  
| **Inventory Clerk**| - Manage ATM cash and checkbook issuance  
                    - Track physical assets (cards, PINs)  
                    - Log inventory audits  
| **Customer Support** | - View basic customer account info (read-only)  
                       - Reset user credentials  
                       - Log and resolve support tickets  
                       - Track complaint resolution  

> 🔐 Each role will only see functionality relevant to them via dynamic menu generation in the sidebar.

---

## 🧰 Technologies Used

- **Python 3.10+**
- **Tkinter** for the desktop GUI
- **SQLite3** for local database storage
- **CSV/JSON** (optional import/export capabilities)
- **OOP (Object-Oriented Programming)** structure
- **Custom decorators** for error logging and validation
- **Tkinter.ttk** for enhanced widgets
- **File Dialogs & Messageboxes** for user interaction

---

## 🏗️ System Architecture

- `main.py` – App entry point
- `auth.py` – Login, registration, session handling
- `gui.py` – Main GUI layout, window switching
- `db.py` – SQLite functions (CRUD operations, queries)
- `roles/` – Folder containing role-specific classes or screens
- `utils/` – Utility functions and decorators (e.g., error logging)

---

## 🖼️ Sample Features (Implemented or In Progress)

- [x] Login and Logout system with session tracking
- [x] Sidebar menu with dynamic role-based button rendering
- [x] Admin account creation and user role assignment
- [x] SQLite database schema initialization
- [x] CSV export for logs and transactions
- [ ] Dashboard with real-time stats per role
- [ ] Transaction modules: deposit, withdraw, transfer
- [ ] Customer onboarding and KYC
- [ ] Full audit trail for critical actions
- [ ] Dark mode & improved UI theming

---

## 📈 Roadmap

| Feature                        | Status       |
|-------------------------------|--------------|
| Role-based login system       | ✅ Complete   |
| Sidebar menu + permissions    | ✅ Complete   |
| Admin management dashboard    | 🟡 In progress |
| Basic transaction system      | 🟡 In progress |
| Sales & KYC module            | 🔜 Planned    |
| Accountant financial module   | 🔜 Planned    |
| Logging and audit trail       | 🔜 Planned    |
| Report generation (PDF/CSV)   | 🔜 Planned    |
| UI enhancements & theming     | 🟡 Partial    |

---

## 🔍 Known Limitations

- UI responsiveness is fixed to window size (Tkinter limitation)
- No real-time server/database — single-user local environment only
- Currently supports English only (no localization)
- Some features (e.g., multi-factor auth, encryption) are not implemented yet

---

## 🧪 Sample Screenshots

> *Coming soon:

---

## 🤝 Contributing

While this is a solo development project for portfolio purposes, contributions or suggestions are welcome. Please feel free to:
- Open an issue (bug reports, feature requests)
- Submit a pull request (after forking the repo)
- Suggest UI/UX improvements

---

## 📄 License

This project will be released under the **MIT License** once the first stable version is complete.

---

## 📫 Contact

- **Developer**: [Jamlic Kariuki(Jamlic-1)](https://github.com/Jamlic-1)
- **Email**: [jamlicnicksonkariuki4@gmail.com]
- **GitHub Repo**: [https://github.com/Jamlic-1/Python-Banking-Software](https://github.com/Jamlic-1/Python-Banking-Software)

---

> ⭐ If you find this project useful or inspiring, consider giving it a ⭐ on GitHub.
