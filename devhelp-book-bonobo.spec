Summary:	DevHelp book: bonobo
Summary(pl.UTF-8):	Książka do DevHelpa o bonobo
Name:		devhelp-book-bonobo
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/bonobo.tar.gz
# Source0-md5:	378f8d9cbae0b84e25552c680395e9d7
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about bonobo.

%description -l pl.UTF-8
Książka do DevHelpa o bonobo.

%prep
%setup -q -c -n bonobo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/bonobo,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/bonobo.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/bonobo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
