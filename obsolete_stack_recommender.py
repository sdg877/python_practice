import random

frontends = [
    "Adobe Flash", "jQuery Mobile", "Silverlight", "Framesets", "XAML", "AngularJS (v1)",
    "Dojo Toolkit", "Bootstrap 2", "FrontPage Extensions"
]

backends = [
    "ColdFusion", "Perl CGI", "PHP 4", "ASP Classic", "Lotus Notes", "Zope", "Cobalt RaQ",
    "Delphi", "FoxPro"
]

databases = [
    "Access", "dBase", "MyISAM", "IBM DB2 (2002 edition)", "Flat files", "CSV over FTP",
    "Lotus 1-2-3", "Oracle 7", "Indexed .INI files"
]

def generate_stack():
    return {
        "frontend": random.choice(frontends),
        "backend": random.choice(backends),
        "database": random.choice(databases)
    }

if __name__ == "__main__":
    print("Recommended (Obsolete) Tech Stack:\n")
    for _ in range(3):
        stack = generate_stack()
        print(f"Frontend: {stack['frontend']}")
        print(f"Backend : {stack['backend']}")
        print(f"Database: {stack['database']}\n")
