Summary:	DevHelp book: bonobo
Summary(pl):	Ksi±¿ka do DevHelp'a o bonobo
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

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about bonobo

%description -l pl
Ksi±¿ka do DevHelp o bonobo

%prep
%setup -q -c bonobo -n bonobo

%build
mv -f book bonobo
mv -f book.devhelp bonobo.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/bonobo
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install bonobo.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install bonobo/* $RPM_BUILD_ROOT%{_prefix}/books/bonobo

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
