%define pre c1

Summary:	Python interface to MySQL
Name:		python-mysql
Version:	1.2.3
Release:	%mkrel 0.%{pre}.6
License:	GPL
Group:		Development/Python
URL:		http://sourceforge.net/projects/mysql-python/
Source0:	http://prdownloads.sourceforge.net/mysql-python/MySQL-python-%{version}%{pre}.tar.gz
%py_requires -d
BuildRequires:	python-setuptools
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
Provides:	MySQL-python = %{version}-%{release}
Obsoletes:	MySQL-python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n MySQL-python-%{version}%{pre}

%build
env CFLAGS="%{optflags} %{?ldflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README doc/*
%{python_sitearch}/*
