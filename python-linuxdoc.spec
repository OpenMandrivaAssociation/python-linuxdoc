Name:		python-linuxdoc
Version:	20260504
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/l/linuxdoc/linuxdoc-%{version}.tar.gz
Summary:	Sphinx extensions for C and C++ documentation comments
URL:		https://pypi.org/project/linuxdoc/
License:	AGPL-3.0-or-later
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(hatchling)
BuildSystem:	python
BuildArch:	noarch

%description
Sphinx extensions and tools that extract documentation from
C and C++ source comments.

%files
%{_bindir}/linuxdoc.*
%{py_sitedir}/linuxdoc
%{py_sitedir}/linuxdoc-*.*-info
