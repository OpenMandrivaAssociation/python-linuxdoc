Name:		python-linuxdoc
Version:	20260504
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/l/linuxdoc/linuxdoc-%{version}.tar.gz
Summary:	Sphinx-doc extensions & tools to extract documentation from C/C++ source file comments.
URL:		https://pypi.org/project/linuxdoc/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildSystem:	python
BuildArch:	noarch

%description
Sphinx-doc extensions & tools to extract documentation from C/C++ source file comments.

%files
%{_bindir}/linuxdoc.*
%{py_sitedir}/linuxdoc
%{py_sitedir}/linuxdoc-*.*-info
