%define pre %{nil}

Summary:	Python interface to MySQL
Name:		python-mysql
Version:	1.4.6
Release:	1
License:	GPLv2
Group:		Development/Python
Url:		https://pypi.org/project/mysqlclient/
Source0:	https://files.pythonhosted.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
BuildRequires:  pkgconfig(python3)
BuildRequires:	python3.9dist(setuptools)
BuildRequires:	mariadb-devel
BuildRequires:	pkgconfig(zlib)

%description
Python interface to MySQL-3.2 and beyond

MySQLdb is an interface to the popular MySQL database server for Python.
The design goals are:

-     Compliance with Python database API version 2.0 
-     Thread-safety 
-     Thread-friendliness (threads will not block each other) 
-     Compatibility with MySQL-3.23 and later

This module should be mostly compatible with an older interface written by Joe
Skinner and others. However, the older version is a) not thread-friendly, b)
written for MySQL 3.21, c) apparently t actively maintained. No code from that
version is used in MySQLdb. MySQLdb is free software.

%prep
%autosetup -p1 -n mysqlclient-%{version}%{pre}

%build
CFLAGS="%{optflags} %{?ldflags}" LDFLAGS="%{ldflags} -lpython3.9" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc doc/*
%{python_sitearch}/*

