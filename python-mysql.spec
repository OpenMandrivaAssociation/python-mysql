%define pre c1

Summary:	Python interface to MySQL
Name:		python-mysql
Version:	1.2.3
Release:	%mkrel 0.%{pre}.7
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


%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-0.c1.7mdv2011.0
+ Revision: 645858
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-0.c1.6mdv2011.0
+ Revision: 627274
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-0.c1.5mdv2011.0
+ Revision: 626555
- rebuilt against mysql-5.5.8 libs

* Wed Dec 29 2010 Colin Guthrie <cguthrie@mandriva.org> 1.2.3-0.c1.4mdv2011.0
+ Revision: 625877
- Rebuild for MySQL 5.5

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2.3-0.c1.3mdv2011.0
+ Revision: 591928
- rebuild for python 2.7

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Oct 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.3-0.c1.1mdv2010.0
+ Revision: 455454
- new version

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-6mdv2010.0
+ Revision: 442319
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 1.2.2-5mdv2009.1
+ Revision: 320138
- rebulid for new python

* Sun Dec 07 2008 Funda Wang <fwang@mandriva.org> 1.2.2-4mdv2009.1
+ Revision: 311539
- do not record files
- build requires python-setuptools

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-4mdv2009.0
+ Revision: 259718
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-3mdv2009.0
+ Revision: 247520
- rebuild

* Mon Feb 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdv2008.1
+ Revision: 174798
- 1.2.2

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2.1-0.p2.3mdv2008.1
+ Revision: 136452
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 05 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.2.1-0.p2.3mdv2007.0
+ Revision: 90999
- Rebuild against new python
- import python-mysql-1.2.1-0.p2.2mdv2007.0

* Mon Sep 11 2006 David Walluck <walluck@mandriva.org> 1.2.1-0.p2.2mdv2007.0
- own directory

* Sun Jul 30 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-0.p2.1mdv2007.0
- 1.2.1_p2
- renamed from MySQL-python to python-mysql (fixes #21675)

* Wed Jun 21 2006 Lenny Cartier <lenny@mandriva.com> 1.2.0-3mdv2007.0
- rebuild

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdk
- rebuilt against openssl-0.9.8a

* Wed May 18 2005 Frederic Lepied <flepied@mandriva.com> 1.2.0-1mdk
- New release 1.2.0

* Wed Dec 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.0-1mdk
- 1.0.0

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.9.2-5mdk
- Rebuild for new python

* Tue Jun 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.2-4mdk
- added P0 (from fedora)
- misc spec file fixes

* Tue Apr 06 2004 Michael Scherer <misc@mandrake.org> 0.9.2-3mdk 
- remove invalid Tags
- provides python-mysql

