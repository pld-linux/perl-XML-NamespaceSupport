%include	/usr/lib/rpm/macros.perl

%define	pdir	XML
%define	pnam	NamespaceSupport

Summary:	XML-NamespaceSupport perl module
Summary(pl):	Modu³ perla XML-NamespaceSupport
Name:		perl-%{pdir}-%{pnam}
Version:	1.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl >= 5.6.1
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/XML/NamespaceSupport.pm
%{_mandir}/man3/*
