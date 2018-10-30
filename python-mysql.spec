%define pre %{nil}

Summary:	Python interface to MySQL
Name:		python-mysql
Version:	1.2.5
Release:	6
License:	GPLv2
Group:		Development/Python
Url:		http://sourceforge.net/projects/mysql-python/
Source0:	http://prdownloads.sourceforge.net/mysql-python/MySQL-python-%{version}%{pre}.zip
BuildRequires:  python2-devel
BuildRequires:	python2-distribute
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
%setup -qn MySQL-python-%{version}%{pre}

%build
env CFLAGS="%{optflags} %{?ldflags}" python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc doc/*
%{python2_sitearch}/*

