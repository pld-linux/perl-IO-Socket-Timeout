#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Socket-Timeout
Summary:	IO::Socket::Timeout - IO::Socket with read/write timeout
#Summary(pl.UTF-8):
Name:		perl-IO-Socket-Timeout
Version:	0.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	93d978bb7f8360a215b646cf339b4559
# generic URL, check or change before uncommenting
#URL:		https://metacpan.org/release/IO-Socket-Timeout
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(PerlIO::via::Timeout) >= 0.32
BuildRequires:	perl-Test-TCP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Socket provides a way to set a timeout on the socket, but the
timeout will be used only for connection, not for reading / writing
operations.

This module provides a way to set a timeout on read / write operations
on an IO::Socket instance, or any IO::Socket::* modules, like
IO::Socket::INET.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Socket/*.pm
%{_mandir}/man3/*
