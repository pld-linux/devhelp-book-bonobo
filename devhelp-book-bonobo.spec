Summary:	DevHelp book: bonobo
Summary(pl):	Ksi±¿ka do DevHelpa o bonobo
Name:		devhelp-book-bonobo
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/bonobo.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DevHelp book about bonobo.

%description -l pl
Ksi±¿ka do DevHelpa o bonobo.

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
