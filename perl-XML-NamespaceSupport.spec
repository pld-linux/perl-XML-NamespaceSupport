#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	NamespaceSupport
Summary:	XML::NamespaceSupport perl module
Summary(pl.UTF-8):	Moduł perla XML::NamespaceSupport
Name:		perl-XML-NamespaceSupport
Version:	1.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b0867d7b599d8a63ba630fa6227936fe
URL:		http://search.cpan.org/dist/XML-NamespaceSupport/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module offers a simple to process namespaced XML names
(unames) from within any application that may need them. It also helps
maintain a prefix to namespace URI map, and provides a number of basic
checks.

%description -l pl.UTF-8
Ten moduł Perla oferuje proste do przetworzenia, uwzględniające
przestrzenie nazw, nazwy XML, dostępne z każdej aplikacji, która ich
potrzebuje. Pomaga także prowadzić mapowanie prefiksów na przestrzenie
nazw i udostępnia wiele możliwości podstawowej kontroli poprawności.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/NamespaceSupport.pm
%{_mandir}/man3/*
