%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	NamespaceSupport
Summary:	XML::NamespaceSupport perl module
Summary(pl):	Modu³ perla XML::NamespaceSupport
Name:		perl-%{pdir}-%{pnam}
Version:	1.08
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module offers a simple to process namespaced XML names
(unames) from within any application that may need them. It also helps
maintain a prefix to namespace URI map, and provides a number of basic
checks.

%description -l pl
Ten modu³ Perla oferuje proste do przetworzenia, uwzglêdniaj±ce
przestrzenie nazw, nazwy XML, dostêpne z ka¿dej aplikacji, która ich
potrzebuje. Pomaga tak¿e prowadziæ mapowanie prefiksów na przestrzenie
nazw i udostêpnia wiele mo¿liwo¶ci podstawowej kontroli poprawno¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/NamespaceSupport.pm
%{_mandir}/man3/*
